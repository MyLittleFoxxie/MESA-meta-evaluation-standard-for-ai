/* MESA fillable PDF export
 * Renders the already-parsed form (window.MesaForm.getBlocks(), stamped with
 * control ids by mesa-form.js) into a real interactive PDF using pdf-lib:
 * text fields, checkboxes, radio groups and dropdowns as actual AcroForm
 * fields, pre-filled from window.MesaForm.getAnswers(). This is a from-scratch
 * page layout (pdf-lib has no HTML/flow layout of its own), not a rasterized
 * copy of the web page — see the plan notes for the known simplifications
 * (no rich inline markdown, no dynamically-added "+ Add row" rows, no
 * rasterized mermaid/code blocks).
 */
(function () {
  "use strict";

  var PAGE_W = 595.28, PAGE_H = 841.89; // A4, points
  var MARGIN = 48;
  var CONTENT_W = PAGE_W - 2 * MARGIN;

  var HEADING_STYLE = {
    1: { size: 20, bold: true, color: "navy", gapAfter: 14, forceBreak: true },
    2: { size: 15, bold: true, color: "navy", gapAfter: 10, forceBreak: true, rule: true },
    3: { size: 12, bold: true, color: "navy", gapAfter: 6 },
    4: { size: 10.5, bold: true, color: "ink", gapAfter: 5 },
    5: { size: 9.5, bold: true, color: "ink", gapAfter: 4 },
    6: { size: 9.5, bold: true, color: "ink", gapAfter: 4 }
  };

  /* ---------- status (own copy, matching the pattern used by the other modules) ---------- */
  function setStatus(msg) {
    var s = document.getElementById("mesa-status");
    if (s) s.textContent = msg || "";
  }

  /* ---------- text helpers ---------- */
  function mdToPlain(text) {
    var s = String(text == null ? "" : text);
    s = s.replace(/```[\s\S]*?```/g, "");
    s = s.replace(/`([^`]+)`/g, "$1");
    s = s.replace(/\[([^\]]+)\]\(([^)]+)\)/g, "$1 ($2)");
    s = s.replace(/\*\*([^*]+)\*\*/g, "$1");
    s = s.replace(/__([^_]+)__/g, "$1");
    s = s.replace(/\*([^*]+)\*/g, "$1");
    s = s.replace(/_([^_]+)_/g, "$1");
    return s.replace(/\s+/g, " ").trim();
  }

  // Splits "Capability-domain" into ["Capability-", "domain"] -- each piece
  // keeps its trailing hyphen so pieces can be rejoined without extra spaces.
  function splitAfterHyphens(w) {
    var parts = [];
    var cur = "";
    for (var i = 0; i < w.length; i++) {
      cur += w[i];
      if (w[i] === "-") { parts.push(cur); cur = ""; }
    }
    if (cur) parts.push(cur);
    return parts;
  }

  function wrapText(font, size, text, maxWidth) {
    var words = String(text || "").split(/\s+/).filter(Boolean);
    var lines = [];
    var line = "";
    words.forEach(function (w) {
      var test = line ? line + " " + w : w;
      if (font.widthOfTextAtSize(test, size) <= maxWidth) {
        line = test;
        return;
      }
      if (line) lines.push(line);
      if (font.widthOfTextAtSize(w, size) <= maxWidth) {
        line = w;
        return;
      }
      // single word wider than the column: prefer breaking right after a
      // hyphen (e.g. "Capability-domain" -> "Capability-" / "domain") over an
      // arbitrary mid-word character break.
      var pieces = w.indexOf("-") === -1 ? [w] : splitAfterHyphens(w);
      var chunk = "";
      pieces.forEach(function (piece) {
        var test = chunk + piece;
        if (chunk && font.widthOfTextAtSize(test, size) > maxWidth) {
          lines.push(chunk);
          chunk = "";
        }
        if (font.widthOfTextAtSize(piece, size) <= maxWidth) {
          chunk += piece;
          return;
        }
        // even this piece doesn't fit on its own: hard-break it character by character
        for (var i = 0; i < piece.length; i++) {
          var t2 = chunk + piece[i];
          if (chunk && font.widthOfTextAtSize(t2, size) > maxWidth) {
            lines.push(chunk);
            chunk = piece[i];
          } else {
            chunk = t2;
          }
        }
      });
      line = chunk;
    });
    if (line) lines.push(line);
    if (!lines.length) lines.push("");
    return lines;
  }

  // Draws lines top-down starting just below `topY`, without touching the
  // page-flow cursor (used for content already allotted its own box).
  function placeTextLines(page, lines, x, topY, font, size, color, lineHeight) {
    var y = topY;
    lines.forEach(function (line) {
      y -= lineHeight;
      if (line) page.drawText(line, { x: x, y: y, size: size, font: font, color: color });
    });
    return y;
  }

  /* ---------- page-flow cursor ---------- */
  function newPage(state) {
    state.page = state.doc.addPage([PAGE_W, PAGE_H]);
    state.y = PAGE_H - MARGIN;
  }
  function isPageDirty(state) {
    return state.y < PAGE_H - MARGIN - 1;
  }
  function forceNewPageIfDirty(state) {
    if (isPageDirty(state)) newPage(state);
  }
  // Reserves `needed` points of vertical space, starting a new page first if
  // it wouldn't fit. Returns true if a page break happened.
  function ensureSpace(state, needed) {
    if (state.y - needed < MARGIN) { newPage(state); return true; }
    return false;
  }

  /* ---------- block renderers ---------- */
  function renderHeading(state, block) {
    var lvl = Math.min(Math.max(block.level, 1), 6);
    var st = HEADING_STYLE[lvl];
    var text = mdToPlain(block.text);
    if (!text) return;
    var font = st.bold ? state.bold : state.font;
    if (st.forceBreak) forceNewPageIfDirty(state);
    var lineHeight = st.size * 1.3;
    var lines = wrapText(font, st.size, text, CONTENT_W);
    var blockH = lines.length * lineHeight + (st.rule ? 6 : 0);
    ensureSpace(state, blockH + st.gapAfter);
    var topY = state.y;
    state.y -= blockH;
    placeTextLines(state.page, lines, MARGIN, topY, font, st.size, state.colors[st.color], lineHeight);
    if (st.rule) {
      var ruleY = topY - blockH + 3;
      state.page.drawLine({ start: { x: MARGIN, y: ruleY }, end: { x: MARGIN + CONTENT_W, y: ruleY }, thickness: 1.2, color: state.colors.accent });
    }
    state.y -= st.gapAfter;
  }

  function renderProseBlock(state, rawText, opts) {
    opts = opts || {};
    var font = opts.font || state.font;
    var size = opts.size || 10;
    var color = opts.color || state.colors.ink;
    var indent = opts.indent || 0;
    var lineHeight = size * 1.35;
    var gapAfter = opts.gapAfter != null ? opts.gapAfter : 6;
    var plain = mdToPlain(rawText);
    if (!plain) return;
    var lines = wrapText(font, size, plain, CONTENT_W - indent);
    var blockH = lines.length * lineHeight;
    ensureSpace(state, blockH + gapAfter);
    var topY = state.y;
    state.y -= blockH;
    placeTextLines(state.page, lines, MARGIN + indent, topY, font, size, color, lineHeight);
    state.y -= gapAfter;
  }

  function renderHr(state) {
    ensureSpace(state, 14);
    state.y -= 10;
    state.page.drawLine({ start: { x: MARGIN, y: state.y }, end: { x: MARGIN + CONTENT_W, y: state.y }, thickness: 0.5, color: state.colors.line });
    state.y -= 4;
  }

  function renderCheckboxBlock(state, block, answers) {
    if (!block.id) return;
    var label = mdToPlain(block.label);
    var size = 10, lineHeight = size * 1.3;
    var boxSize = 11, textX = MARGIN + boxSize + 8;
    var lines = wrapText(state.font, size, label, CONTENT_W - boxSize - 8);
    var blockH = Math.max(boxSize + 4, lines.length * lineHeight);
    ensureSpace(state, blockH + 4);
    var topY = state.y;
    state.y -= blockH;
    var boxY = topY - boxSize - 1;
    var cb = state.form.createCheckBox(block.id);
    cb.addToPage(state.page, { x: MARGIN, y: boxY, width: boxSize, height: boxSize, borderWidth: 1, borderColor: state.colors.line });
    if (answers[block.id]) cb.check();
    placeTextLines(state.page, lines, textX, topY, state.font, size, state.colors.ink, lineHeight);
    state.y -= 4;
  }

  function renderRatingBlock(state, block, answers) {
    if (!block.id) return;
    var opts = block.options && block.options.length ? block.options : ["n/a", "0", "1", "2", "3", "4"];
    // Each option is a small radio-button widget with its label drawn just to
    // the right of it -- NOT inside/behind the widget's rect. A PDF radio
    // widget always paints its own appearance (a circle, filled when selected)
    // over whatever is on the page underneath its rect, so any text placed
    // inside that rect would be invisibly covered.
    var size = 9, widgetSize = 11, labelGap = 4, itemGap = 16;
    var font = state.font;
    var rows = [[]];
    var cursorW = 0;
    opts.forEach(function (opt) {
      var labelW = font.widthOfTextAtSize(opt, size);
      var w = widgetSize + labelGap + labelW;
      if (cursorW + w > CONTENT_W && rows[rows.length - 1].length) {
        rows.push([]);
        cursorW = 0;
      }
      rows[rows.length - 1].push({ opt: opt, w: w });
      cursorW += w + itemGap;
    });
    var rowH = Math.max(widgetSize, size * 1.2);
    var rowStep = rowH + 8;
    var blockH = rows.length * rowStep;
    ensureSpace(state, blockH + 4);
    var rg = state.form.createRadioGroup(block.id);
    var selected = answers[block.id];
    var topY = state.y;
    rows.forEach(function (row, ri) {
      var x = MARGIN;
      var rowY = topY - ri * rowStep - rowH;
      row.forEach(function (item) {
        rg.addOptionToPage(item.opt, state.page, { x: x, y: rowY, width: widgetSize, height: widgetSize });
        state.page.drawText(item.opt, { x: x + widgetSize + labelGap, y: rowY + (widgetSize - size) / 2.6, size: size, font: font, color: state.colors.ink });
        x += item.w + itemGap;
      });
    });
    if (selected && opts.indexOf(selected) !== -1) rg.select(selected);
    state.y -= blockH;
  }

  function renderPromptBlock(state, block, answers) {
    if (!block.id) return;
    var label = block.label_clean || mdToPlain(String(block.label || "").replace(/:\s*$/, ""));
    var fieldH = block.big ? 90 : 40;
    var labelSize = 10, labelLineHeight = labelSize * 1.3;
    var totalH = labelLineHeight + 4 + fieldH;
    ensureSpace(state, totalH + 8);
    var topY = state.y;
    state.y -= labelLineHeight;
    state.page.drawText(label + ":", { x: MARGIN, y: state.y, size: labelSize, font: state.bold, color: state.colors.ink });
    var fieldTop = topY - labelLineHeight - 4;
    state.y = fieldTop - fieldH;
    var tf = state.form.createTextField(block.id);
    tf.addToPage(state.page, { x: MARGIN, y: fieldTop - fieldH, width: CONTENT_W, height: fieldH, borderWidth: 1, borderColor: state.colors.line, backgroundColor: state.colors.white });
    tf.enableMultiline();
    tf.setFontSize(9.5);
    var v = answers[block.id];
    if (v != null) tf.setText(String(v));
    state.y -= 8;
  }

  /* ---------- tables ---------- */
  function computeColWidths(header, contentWidth, kind, ratingCol) {
    var n = header.length;
    var widths = new Array(n);
    var fixed = 0;
    var i;
    for (i = 0; i < n; i++) {
      if (kind === "summary" && i === ratingCol) { widths[i] = 70; fixed += 70; }
      else if ((header[i] || "").trim().length <= 3) { widths[i] = 30; fixed += 30; }
    }
    var remaining = Math.max(contentWidth - fixed, 60);
    var flexIdx = [];
    for (i = 0; i < n; i++) if (widths[i] == null) flexIdx.push(i);
    if (flexIdx.length === 1) {
      widths[flexIdx[0]] = remaining;
    } else if (flexIdx.length > 1) {
      var firstW = Math.min(Math.max(remaining * 0.32, 140), remaining * 0.45);
      widths[flexIdx[0]] = firstW;
      var restRemaining = remaining - firstW;
      var restCount = flexIdx.length - 1;
      for (i = 1; i < flexIdx.length; i++) widths[flexIdx[i]] = restRemaining / restCount;
    }
    return widths;
  }

  function classifyCell(block, cell, colIdx, ratingCol) {
    if (block.kind === "checkbox" && /\[( |x|X)\]/.test(cell)) return "checkbox";
    if (block.kind === "fill" && /^_\(.*\)_$/.test(cell.trim())) return "fill";
    if (block.kind === "summary" && colIdx === ratingCol) return "dropdown";
    return "text";
  }

  var SUMMARY_OPTS = ["n/a", "0", "1", "2", "3", "4"];

  function renderTableBlock(state, block, answers) {
    var header = block.header;
    var n = header.length;
    var kind = block.kind;
    var ratingCol = -1;
    if (kind === "summary") {
      header.forEach(function (h, i) { if (/overall rating/i.test(h)) ratingCol = i; });
      if (ratingCol === -1) ratingCol = n - 1;
    }
    var colWidths = computeColWidths(header, CONTENT_W, kind, ratingCol);
    var headerFont = state.bold, headerSize = 9;
    var cellFont = state.font, cellSize = 9;
    var padding = 5;
    var maxRowH = PAGE_H - 2 * MARGIN - 30;

    function drawRowBorders(topY, rowH, widths) {
      state.page.drawRectangle({ x: MARGIN, y: topY - rowH, width: CONTENT_W, height: rowH, borderWidth: 0.75, borderColor: state.colors.line });
      var x = MARGIN;
      widths.forEach(function (w) {
        x += w;
        if (x < MARGIN + CONTENT_W - 0.5) {
          state.page.drawLine({ start: { x: x, y: topY }, end: { x: x, y: topY - rowH }, thickness: 0.75, color: state.colors.line });
        }
      });
    }

    function headerLines() {
      return header.map(function (h, i) { return wrapText(headerFont, headerSize, mdToPlain(h), colWidths[i] - 2 * padding); });
    }

    function drawHeaderRow() {
      var lines = headerLines();
      var maxLines = lines.reduce(function (m, l) { return Math.max(m, l.length); }, 1);
      var rowH = Math.max(18, maxLines * headerSize * 1.25 + padding * 2);
      ensureSpace(state, rowH);
      var topY = state.y;
      state.y -= rowH;
      state.page.drawRectangle({ x: MARGIN, y: topY - rowH, width: CONTENT_W, height: rowH, color: state.colors.headerBg });
      var x = MARGIN;
      lines.forEach(function (colLines, i) {
        placeTextLines(state.page, colLines, x + padding, topY, headerFont, headerSize, state.colors.navy, headerSize * 1.25);
        x += colWidths[i];
      });
      drawRowBorders(topY, rowH, colWidths);
    }

    ensureSpace(state, 20 + 18);
    drawHeaderRow();

    block.body.forEach(function (cells, rowIdx) {
      var types = cells.map(function (c, i) { return classifyCell(block, c, i, ratingCol); });
      var rowH = 18;
      types.forEach(function (t, i) {
        if (t === "text") {
          var lines = wrapText(cellFont, cellSize, mdToPlain(cells[i]), colWidths[i] - 2 * padding);
          rowH = Math.max(rowH, lines.length * cellSize * 1.25 + padding * 2);
        } else if (t === "fill") {
          rowH = Math.max(rowH, 26);
        } else {
          rowH = Math.max(rowH, 20);
        }
      });
      rowH = Math.min(rowH, maxRowH);

      var broke = ensureSpace(state, rowH);
      if (broke) drawHeaderRow();
      var topY = state.y;
      state.y -= rowH;
      var x = MARGIN;
      var fieldRow = block.fieldIds[rowIdx];

      cells.forEach(function (cell, c) {
        var w = colWidths[c];
        var t = types[c];
        var fid = fieldRow ? fieldRow[c] : null;
        if (t === "checkbox" && fid) {
          var boxSize = 11;
          var cb = state.form.createCheckBox(fid);
          cb.addToPage(state.page, { x: x + w / 2 - boxSize / 2, y: topY - rowH + (rowH - boxSize) / 2, width: boxSize, height: boxSize, borderWidth: 1, borderColor: state.colors.line });
          if (answers[fid]) cb.check();
        } else if (t === "fill" && fid) {
          var tf = state.form.createTextField(fid);
          tf.addToPage(state.page, { x: x + 2, y: topY - rowH + 2, width: Math.max(w - 4, 4), height: Math.max(rowH - 4, 4), borderWidth: 0.75, borderColor: state.colors.line, backgroundColor: state.colors.white });
          tf.enableMultiline();
          tf.setFontSize(8.5);
          var v = answers[fid];
          if (v != null) tf.setText(String(v));
        } else if (t === "dropdown" && fid) {
          var dd = state.form.createDropdown(fid);
          var ddH = Math.min(rowH - 4, 18);
          dd.addToPage(state.page, { x: x + 2, y: topY - rowH + (rowH - ddH) / 2, width: Math.max(w - 4, 4), height: ddH, borderWidth: 0.75, borderColor: state.colors.line, backgroundColor: state.colors.white });
          dd.addOptions(SUMMARY_OPTS);
          var dv = answers[fid];
          if (dv != null && SUMMARY_OPTS.indexOf(dv) !== -1) dd.select(dv);
        } else {
          var lines = wrapText(cellFont, cellSize, mdToPlain(cell), w - 2 * padding);
          placeTextLines(state.page, lines, x + padding, topY, cellFont, cellSize, state.colors.ink, cellSize * 1.25);
        }
        x += w;
      });
      drawRowBorders(topY, rowH, colWidths);
    });

    state.y -= 8;
  }

  function renderBlock(state, block, answers) {
    switch (block.type) {
      case "heading": renderHeading(state, block); break;
      case "paragraph": renderProseBlock(state, block.text, {}); break;
      case "grouplabel": renderProseBlock(state, block.text, { font: state.bold, gapAfter: 4 }); break;
      case "bullet": renderProseBlock(state, "• " + block.text, { indent: 12, gapAfter: 3 }); break;
      case "anchor": renderProseBlock(state, block.text, { font: state.oblique, size: 9, color: state.colors.muted, indent: 12, gapAfter: 4 }); break;
      case "checkbox": renderCheckboxBlock(state, block, answers); break;
      case "rating": renderRatingBlock(state, block, answers); break;
      case "prompt": renderPromptBlock(state, block, answers); break;
      case "table": renderTableBlock(state, block, answers); break;
      case "mermaid":
      case "code":
        renderProseBlock(state, "[Figure/code omitted from PDF export]", { font: state.oblique, size: 9, color: state.colors.muted });
        break;
      case "hr": renderHr(state); break;
      // "heading"'s ctx.path bookkeeping, DOM-only concerns, etc. have no PDF equivalent.
    }
  }

  /* ---------- document assembly ---------- */
  function makeColors(rgb) {
    return {
      navy: rgb(0, 0.278, 0.443),
      accent: rgb(0.824, 0.412, 0.118),
      ink: rgb(0.11, 0.153, 0.2),
      muted: rgb(0.353, 0.42, 0.482),
      line: rgb(0.847, 0.871, 0.902),
      headerBg: rgb(0.933, 0.949, 0.968),
      white: rgb(1, 1, 1)
    };
  }

  function buildPdfDocument(blocks, answers) {
    var PDFLib = window.PDFLib;
    var PDFDocument = PDFLib.PDFDocument, StandardFonts = PDFLib.StandardFonts, rgb = PDFLib.rgb;
    return PDFDocument.create().then(function (doc) {
      return Promise.all([
        doc.embedFont(StandardFonts.Helvetica),
        doc.embedFont(StandardFonts.HelveticaBold),
        doc.embedFont(StandardFonts.HelveticaOblique)
      ]).then(function (fonts) {
        var state = {
          doc: doc,
          form: doc.getForm(),
          page: null,
          y: 0,
          font: fonts[0],
          bold: fonts[1],
          oblique: fonts[2],
          colors: makeColors(rgb)
        };
        newPage(state);
        blocks.forEach(function (block) { renderBlock(state, block, answers); });
        state.form.updateFieldAppearances(state.font);
        return doc.save();
      });
    });
  }

  function todayStamp() {
    var d = new Date();
    function p(n) { return (n < 10 ? "0" : "") + n; }
    return d.getFullYear() + "-" + p(d.getMonth() + 1) + "-" + p(d.getDate());
  }

  function downloadPdfBytes(bytes) {
    var blob = new Blob([bytes], { type: "application/pdf" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    var kind = (window.MesaForm && window.MesaForm.builtFor && window.MesaForm.builtFor() === "scorecard")
      ? "mesa-scorecard-" : "mesa-review-";
    a.download = kind + todayStamp() + ".pdf";
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
  }

  /* ---------- entry point ---------- */
  function exportPdf() {
    if (!window.PDFLib) {
      setStatus("PDF export is unavailable: the pdf-lib library failed to load.");
      return;
    }
    if (!window.MesaForm) {
      setStatus("PDF export is unavailable: the form module failed to load.");
      return;
    }
    setStatus("Generating PDF… this may take a few seconds.");
    // yield two frames/ticks so the status message actually paints before the
    // synchronous layout work (several hundred fields) blocks the main thread.
    window.requestAnimationFrame(function () {
      setTimeout(function () {
        window.MesaForm.ready()
          .then(function () {
            var blocks = window.MesaForm.getBlocks();
            var answers = window.MesaForm.getAnswers();
            return buildPdfDocument(blocks, answers);
          })
          .then(downloadPdfBytes)
          .then(function () { setStatus(""); })
          .catch(function (err) {
            console.error(err);
            setStatus("PDF generation failed: " + err.message);
          });
      }, 0);
    });
  }

  // Reads a MESA-exported fillable PDF back into an { id: value } answers map.
  // Field names in that PDF are exactly the app's controlId()-generated ids
  // (see buildPdfDocument above), so this is a lookup, not a re-parse.
  function importAnswers(arrayBuffer) {
    if (!window.PDFLib) return Promise.reject(new Error("the pdf-lib library failed to load"));
    var PDFLib = window.PDFLib;
    return PDFLib.PDFDocument.load(arrayBuffer).then(function (doc) {
      var fields = doc.getForm().getFields();
      var out = {};
      fields.forEach(function (f) {
        var name = f.getName();
        if (f instanceof PDFLib.PDFTextField) {
          var text = f.getText();
          if (text) out[name] = text;
        } else if (f instanceof PDFLib.PDFCheckBox) {
          if (f.isChecked()) out[name] = true;
        } else if (f instanceof PDFLib.PDFRadioGroup) {
          var selected = f.getSelected();
          if (selected) out[name] = selected;
        } else if (f instanceof PDFLib.PDFDropdown) {
          var options = f.getSelected();
          if (options && options.length) out[name] = options[0];
        }
      });
      return out;
    });
  }

  window.MesaPdf = { exportPdf: exportPdf, importAnswers: importAnswers };
})();
