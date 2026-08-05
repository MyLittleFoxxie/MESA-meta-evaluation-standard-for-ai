/* MESA interactive form
 * Reads the canonical MESA template Markdown at load time and builds a fillable
 * form from it. The parser keys off the template's authoring conventions, so new
 * template versions are picked up automatically with no code change.
 *
 * Conventions relied on (keep these in the .md for auto-pickup to work):
 *   - Headings `#`..`######`; numeric prefixes (e.g. "2.1", "6.1.1") define IDs.
 *   - Checkbox options:        `- [ ] Label`
 *   - Rating items:            `- Rating: [n/a | 0 | 1 | 2 | 3 | 4]`  (anchor in `- Excellent: ...`)
 *   - Free-text prompts:       a standalone line ending in `:` (e.g. "Reviewer comments:", "Free Text:")
 *   - Fill-in tables:          body cells containing `_(placeholder)_`
 *   - Checkbox-matrix tables:  body cells containing `[ ]`
 *   - Reference tables:        all other tables (rating scale, guidance, etc.)
 *   - Figures:                 ```mermaid fenced blocks
 */
(function () {
  "use strict";

  var TEMPLATE_URL = "MESA EFPA template official.md";
  var STORAGE_KEY = "mesa-form-answers-v1";
  var RATING_FALLBACK = ["n/a", "0", "1", "2", "3", "4"];

  var state = { answers: loadAnswers() };
  var usedIds = Object.create(null);
  var blocks = [];

  /* ---------- persistence ---------- */
  function loadAnswers() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
    } catch (e) {
      return {};
    }
  }
  function saveAnswers() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state.answers));
    } catch (e) {
      /* storage may be unavailable (private mode); ignore */
    }
    updateProgress();
  }
  function setAnswer(id, value) {
    if (value === "" || value === false || value == null) {
      delete state.answers[id];
    } else {
      state.answers[id] = value;
    }
    saveAnswers();
  }

  /* ---------- helpers ---------- */
  function slug(s) {
    return String(s)
      .toLowerCase()
      .replace(/`|\*|_|\[|\]|\(|\)|<[^>]*>/g, "")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "")
      .slice(0, 60) || "x";
  }
  function uniqueId(base) {
    var id = base, n = 2;
    while (usedIds[id]) {
      id = base + "-" + n++;
    }
    usedIds[id] = true;
    return id;
  }
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function inlineMD(text) {
    try {
      return window.marked.parseInline(text);
    } catch (e) {
      return text;
    }
  }
  function blockMD(text) {
    try {
      return window.marked.parse(text);
    } catch (e) {
      return "<p>" + text + "</p>";
    }
  }
  // pull leading numeric path like "6.1.1" from a heading, else null
  function headingNumber(text) {
    var m = text.match(/^(?:Section\s+|Appendix\s+)?(\d+(?:\.\d+)*)\b/);
    if (m) return m[1];
    return null;
  }

  /* ---------- parser ---------- */
  function parseTable(tlines) {
    var rows = tlines.map(function (l) {
      var s = l.trim().replace(/^\|/, "").replace(/\|$/, "");
      return s.split("|").map(function (c) {
        return c.trim();
      });
    });
    var header = rows[0];
    var body = rows.slice(2); // row 1 is the |:--|:--| separator
    var hasCheckbox = body.some(function (r) {
      return r.some(function (c) { return /\[( |x|X)\]/.test(c); });
    });
    var hasFill = body.some(function (r) {
      return r.some(function (c) { return /^_\(.*\)_$/.test(c.trim()); });
    });
    var kind = "ref";
    if (hasCheckbox) kind = "checkbox";
    else if (hasFill) kind = "fill";
    else if (/overall rating/i.test(header.join(" "))) kind = "summary";
    var repeatable =
      kind === "fill" &&
      body.length > 0 &&
      body.every(function (r) {
        return r.every(function (c) {
          return c === "" || /^_\(.*\)_$/.test(c);
        });
      });
    return { type: "table", header: header, body: body, kind: kind, repeatable: repeatable };
  }

  function parse(md) {
    var lines = md.replace(/\r\n/g, "\n").split("\n");
    var blocks = [];
    var i = 0;
    while (i < lines.length) {
      var line = lines[i];
      if (line.trim() === "") { i++; continue; }

      // fenced code / mermaid
      if (/^```/.test(line.trim())) {
        var lang = line.trim().replace(/^```/, "").trim();
        var code = [];
        i++;
        while (i < lines.length && !/^```/.test(lines[i].trim())) { code.push(lines[i]); i++; }
        i++; // closing fence
        blocks.push({ type: lang === "mermaid" ? "mermaid" : "code", lang: lang, code: code.join("\n") });
        continue;
      }

      // heading
      var h = line.match(/^(#{1,6})\s+(.*)$/);
      if (h) { blocks.push({ type: "heading", level: h[1].length, text: h[2].trim() }); i++; continue; }

      // horizontal rule
      if (/^---+$/.test(line.trim())) { blocks.push({ type: "hr" }); i++; continue; }

      // table
      if (line.trim().indexOf("|") === 0) {
        var tbl = [];
        while (i < lines.length && lines[i].trim().indexOf("|") === 0) { tbl.push(lines[i]); i++; }
        if (tbl.length >= 2) { blocks.push(parseTable(tbl)); }
        else { blocks.push({ type: "paragraph", text: tbl.join(" ") }); }
        continue;
      }

      // checkbox option
      var cb = line.match(/^\s*-\s*\[( |x|X)\]\s*(.*)$/);
      if (cb) {
        blocks.push({ type: "checkbox", checked: cb[1].toLowerCase() === "x", label: cb[2].trim() });
        i++;
        continue;
      }

      // bullet line: rating / excellent anchor / other prose bullet
      var bl = line.match(/^\s*-\s+(.*)$/);
      if (bl) {
        var content = bl[1].trim();
        var rm = content.match(/^Rating:\s*\[(.*)\]\s*$/i);
        if (rm) { blocks.push({ type: "rating", raw: rm[1] }); i++; continue; }
        if (/^Excellent:/i.test(content)) { blocks.push({ type: "anchor", text: content }); i++; continue; }
        blocks.push({ type: "bullet", text: content });
        i++;
        continue;
      }

      // paragraph: accumulate consecutive plain text lines
      var para = [line];
      i++;
      while (i < lines.length) {
        var l = lines[i];
        if (l.trim() === "") break;
        if (/^(#{1,6})\s/.test(l)) break;
        if (/^```/.test(l.trim())) break;
        if (l.trim().indexOf("|") === 0) break;
        if (/^\s*-\s/.test(l)) break;
        if (/^---+$/.test(l.trim())) break;
        para.push(l);
        i++;
      }
      var text = para.join(" ").trim();

      // a standalone single line ending in ":" is either a free-text prompt
      // or a label introducing a checkbox/table group
      if (para.length === 1 && /:\s*$/.test(text)) {
        // explicit free-text prompts are always input fields, whatever follows
        if (/^(reviewer comments|free text)\b/i.test(text)) {
          blocks.push({ type: "prompt", label: text });
          continue;
        }
        var j = i;
        while (j < lines.length && lines[j].trim() === "") j++;
        var next = j < lines.length ? lines[j] : "";
        if (/^\s*-\s*\[( |x|X)\]/.test(next) || next.trim().indexOf("|") === 0) {
          blocks.push({ type: "grouplabel", text: text });
        } else if (/^\s*-\s/.test(next)) {
          blocks.push({ type: "paragraph", text: text });
        } else {
          blocks.push({ type: "prompt", label: text });
        }
      } else {
        blocks.push({ type: "paragraph", text: text });
      }
    }
    return blocks;
  }

  /* ---------- rendering ---------- */
  var ctx = { path: "intro", mount: null, root: null, mermaidNodes: [] };

  function controlId(parts) {
    return uniqueId(parts.filter(Boolean).map(slug).join("::"));
  }

  function bindInput(input, id, kind) {
    input.dataset.mesaId = id;
    var saved = state.answers[id];
    if (kind === "check") {
      if (saved) input.checked = true;
      input.addEventListener("change", function () { setAnswer(id, input.checked); });
    } else if (kind === "rating") {
      // handled per-radio in renderRating
    } else {
      if (saved != null) input.value = saved;
      input.addEventListener("input", function () {
        setAnswer(id, input.value);
        autoGrow(input);
      });
    }
  }

  function autoGrow(ta) {
    if (ta.tagName !== "TEXTAREA") return;
    ta.style.height = "auto";
    ta.style.height = Math.max(ta.scrollHeight, 32) + "px";
  }

  function makeTextarea(id, placeholder, big) {
    var ta = el("textarea", "mesa-text" + (big ? " mesa-text-big" : ""));
    if (placeholder) ta.placeholder = placeholder;
    ta.rows = big ? 4 : 2;
    bindInput(ta, id, "text");
    return ta;
  }

  function renderCheckbox(block) {
    var wrap = el("label", "mesa-check");
    var input = el("input");
    input.type = "checkbox";
    var id = controlId([ctx.path, block.label]);
    block.id = id;
    bindInput(input, id, "check");
    var span = el("span");
    span.innerHTML = inlineMD(block.label);
    wrap.appendChild(input);
    wrap.appendChild(span);
    ctx.mount.appendChild(wrap);
  }

  function renderRating(block) {
    var opts = block.raw.split("|").map(function (s) { return s.trim(); }).filter(Boolean);
    if (!opts.length) opts = RATING_FALLBACK.slice();
    var id = controlId([ctx.path, "rating"]);
    block.id = id;
    block.options = opts;
    var wrap = el("div", "mesa-rating");
    wrap.dataset.mesaRating = id;
    var saved = state.answers[id];
    opts.forEach(function (opt) {
      var lab = el("label", "mesa-rating-opt");
      var r = el("input");
      r.type = "radio";
      r.name = id;
      r.value = opt;
      if (saved === opt) { r.checked = true; lab.classList.add("is-selected"); }
      r.addEventListener("change", function () {
        setAnswer(id, opt);
        wrap.querySelectorAll(".mesa-rating-opt").forEach(function (n) { n.classList.remove("is-selected"); });
        lab.classList.add("is-selected");
      });
      lab.appendChild(r);
      lab.appendChild(el("span", null, opt));
      wrap.appendChild(lab);
    });
    ctx.mount.appendChild(wrap);
  }

  function renderTable(block) {
    var tableEl = el("table", "mesa-table mesa-table-" + block.kind);
    var thead = el("thead");
    var htr = el("tr");
    block.header.forEach(function (hcell) {
      var th = el("th");
      th.innerHTML = inlineMD(hcell);
      htr.appendChild(th);
    });
    thead.appendChild(htr);
    tableEl.appendChild(thead);

    var tbody = el("tbody");
    var ratingCol = -1;
    if (block.kind === "summary") {
      block.header.forEach(function (hc, idx) { if (/overall rating/i.test(hc)) ratingCol = idx; });
      if (ratingCol === -1) ratingCol = block.header.length - 1;
    }
    // fieldIds mirrors block.body: fieldIds[rowIdx][colIdx] = the control id of that
    // cell's input, or null for static cells. Only covers the base template rows —
    // rows added at runtime via "+ Add row" are not back-filled here.
    block.fieldIds = block.body.map(function (r) { return r.map(function () { return null; }); });

    function buildRow(cells, rowIdx) {
      var tr = el("tr");
      var rowKey = cells[0] && !/^_\(.*\)_$/.test(cells[0].trim()) ? cells[0] : "row" + rowIdx;
      cells.forEach(function (cell, c) {
        var td = el("td");
        var colKey = block.header[c] || "c" + c;
        if (block.kind === "checkbox" && /\[( |x|X)\]/.test(cell)) {
          var input = el("input");
          input.type = "checkbox";
          var cid = controlId([ctx.path, rowKey, colKey]);
          if (block.fieldIds[rowIdx]) block.fieldIds[rowIdx][c] = cid;
          if (/\[x\]/i.test(cell)) { /* default checked in source */ }
          bindInput(input, cid, "check");
          td.className = "mesa-cell-check";
          td.appendChild(input);
        } else if (block.kind === "fill" && /^_\(.*\)_$/.test(cell.trim())) {
          var ph = (cell.trim().match(/^_\((.*)\)_$/) || [, ""])[1];
          var tid = controlId([ctx.path, rowKey, colKey]);
          if (block.fieldIds[rowIdx]) block.fieldIds[rowIdx][c] = tid;
          td.appendChild(makeTextarea(tid, ph, false));
        } else if (block.kind === "summary" && c === ratingCol) {
          var sid = controlId([ctx.path, "summary", rowKey]);
          if (block.fieldIds[rowIdx]) block.fieldIds[rowIdx][c] = sid;
          var sel = el("select", "mesa-select");
          sel.dataset.mesaId = sid;
          ["", "n/a", "0", "1", "2", "3", "4"].forEach(function (o) {
            var op = el("option", null, o === "" ? "—" : o);
            op.value = o;
            sel.appendChild(op);
          });
          if (state.answers[sid] != null) sel.value = state.answers[sid];
          sel.addEventListener("change", function () { setAnswer(sid, sel.value); });
          td.appendChild(sel);
        } else {
          td.innerHTML = inlineMD(cell);
        }
        tr.appendChild(td);
      });
      return tr;
    }

    block.body.forEach(function (cells, idx) { tbody.appendChild(buildRow(cells, idx)); });
    tableEl.appendChild(tbody);
    ctx.mount.appendChild(tableEl);

    if (block.repeatable) {
      var btn = el("button", "mesa-addrow", "+ Add row");
      btn.type = "button";
      var added = 0;
      btn.addEventListener("click", function () {
        added++;
        var tr = buildRow(block.body[0].slice(), "extra" + added);
        tbody.appendChild(tr);
      });
      ctx.mount.appendChild(btn);
    }
  }

  function renderHeading(block) {
    var num = headingNumber(block.text);
    if (num) ctx.path = num;
    else if (block.level <= 2) ctx.path = slug(block.text);

    if (block.level === 1) {
      var banner = el("h1", "mesa-part");
      banner.innerHTML = inlineMD(block.text);
      ctx.root.appendChild(banner);
      ctx.mount = ctx.root;
      ctx.currentSection = null;
      return;
    }
    if (block.level === 2) {
      var details = el("details", "mesa-section");
      details.open = true;
      var summary = el("summary");
      summary.innerHTML = inlineMD(block.text);
      details.appendChild(summary);
      var body = el("div", "mesa-section-body");
      details.appendChild(body);
      ctx.root.appendChild(details);
      ctx.mount = body;
      ctx.currentSection = details;
      return;
    }
    var hTag = "h" + Math.min(block.level, 6);
    var hEl = el(hTag, "mesa-h mesa-h" + block.level);
    hEl.innerHTML = inlineMD(block.text);
    (ctx.mount || ctx.root).appendChild(hEl);
  }

  function renderMermaid(block) {
    var holder = el("div", "mesa-figure");
    var node = el("div", "mermaid");
    node.textContent = block.code;
    holder.appendChild(node);
    (ctx.mount || ctx.root).appendChild(holder);
    ctx.mermaidNodes.push(node);
  }

  function renderBlock(block) {
    var mount = ctx.mount || ctx.root;
    switch (block.type) {
      case "heading": renderHeading(block); break;
      case "paragraph": {
        var p = el("div", "mesa-prose");
        p.innerHTML = blockMD(block.text);
        mount.appendChild(p);
        break;
      }
      case "grouplabel": {
        var gl = el("div", "mesa-grouplabel");
        gl.innerHTML = inlineMD(block.text);
        mount.appendChild(gl);
        break;
      }
      case "bullet": {
        var b = el("div", "mesa-bullet");
        b.innerHTML = inlineMD(block.text);
        mount.appendChild(b);
        break;
      }
      case "anchor": {
        var a = el("div", "mesa-anchor");
        a.innerHTML = inlineMD(block.text);
        mount.appendChild(a);
        break;
      }
      case "prompt": {
        var label = block.label.replace(/:\s*$/, "");
        var wrap = el("div", "mesa-field");
        wrap.appendChild(el("div", "mesa-field-label", label + ":"));
        var big = /free text/i.test(label) || /evaluative report|conclusion|recommendation/i.test(label);
        var id = controlId([ctx.path, /free text/i.test(label) ? "freetext" : /reviewer comments/i.test(label) ? "comments" : label]);
        block.id = id;
        block.label_clean = label;
        block.big = big;
        wrap.appendChild(makeTextarea(id, "", big));
        mount.appendChild(wrap);
        break;
      }
      case "checkbox": renderCheckbox(block); break;
      case "rating": renderRating(block); break;
      case "table": renderTable(block); break;
      case "mermaid": renderMermaid(block); break;
      case "code": {
        var pre = el("pre", "mesa-code");
        pre.textContent = block.code;
        mount.appendChild(pre);
        break;
      }
      case "hr": mount.appendChild(el("hr", "mesa-sep")); break;
    }
  }

  /* ---------- progress ---------- */
  function updateProgress() {
    var pe = document.getElementById("mesa-progress");
    if (!pe) return;
    var groups = document.querySelectorAll("[data-mesa-rating]");
    var total = groups.length;
    var done = 0;
    groups.forEach(function (g) {
      if (state.answers[g.dataset.mesaRating] != null) done++;
    });
    pe.textContent = total ? "Ratings: " + done + " / " + total : "";
  }

  /* ---------- build ---------- */
  function build(md) {
    usedIds = Object.create(null);
    var root = document.getElementById("mesa-form");
    root.innerHTML = "";
    ctx = { path: "intro", mount: root, root: root, mermaidNodes: [], currentSection: null };

    blocks = parse(md);
    blocks.forEach(renderBlock);

    // grow restored textareas
    root.querySelectorAll("textarea").forEach(autoGrow);

    // render figures
    if (window.mermaid && ctx.mermaidNodes.length) {
      try {
        window.mermaid.initialize({ startOnLoad: false, securityLevel: "loose" });
        window.mermaid.run({ nodes: ctx.mermaidNodes });
      } catch (e) {
        ctx.mermaidNodes.forEach(function (n) {
          var pre = el("pre", "mesa-code");
          pre.textContent = n.textContent;
          n.replaceWith(pre);
        });
      }
    }

    flagOrphans(root);
    updateProgress();
    setStatus("");
    built = true;
    // let the site shell (router) rebuild the sidebar TOC from the form
    try { window.dispatchEvent(new CustomEvent("mesa-form-built")); } catch (e) { /* older browsers */ }
  }

  // warn if saved answers no longer map to anything in the current template
  function flagOrphans(root) {
    var live = {};
    root.querySelectorAll("[data-mesa-id]").forEach(function (n) { live[n.dataset.mesaId] = true; });
    root.querySelectorAll("[data-mesa-rating]").forEach(function (n) { live[n.dataset.mesaRating] = true; });
    var orphans = Object.keys(state.answers).filter(function (k) {
      return !live[k] && !document.querySelector('[data-mesa-id="' + cssEscape(k) + '"]');
    });
    var note = document.getElementById("mesa-orphan-note");
    if (note) {
      if (orphans.length) {
        note.textContent =
          orphans.length + " saved answer(s) from a previous template version no longer match the current template (kept in storage, not shown).";
        note.style.display = "";
      } else {
        note.style.display = "none";
      }
    }
  }
  function cssEscape(s) { return String(s).replace(/["\\]/g, "\\$&"); }

  /* ---------- status / toolbar ---------- */
  function setStatus(msg) {
    var s = document.getElementById("mesa-status");
    if (s) s.textContent = msg;
  }

  function wireToolbar() {
    // Note: the Print button is wired by the site shell (mesa-site.js) so it
    // works on every tab, not just the Review Template form.
    var expand = document.getElementById("btn-expand");
    if (expand) expand.addEventListener("click", function () {
      var open = expand.dataset.state !== "collapsed";
      document.querySelectorAll("details.mesa-section").forEach(function (d) { d.open = !open; });
      expand.dataset.state = open ? "collapsed" : "";
      expand.textContent = open ? "Expand all" : "Collapse all";
    });

    var reset = document.getElementById("btn-reset");
    if (reset) reset.addEventListener("click", function () {
      if (confirm("Clear all answers saved in this browser? This cannot be undone.")) {
        state.answers = {};
        saveAnswers();
        location.reload();
      }
    });

    var loader = document.getElementById("file-loader");
    if (loader) loader.addEventListener("change", function () {
      var f = loader.files[0];
      if (!f) return;
      var reader = new FileReader();
      reader.onload = function () { build(String(reader.result)); };
      reader.readAsText(f);
    });

    window.addEventListener("beforeprint", function () {
      document.querySelectorAll("details.mesa-section").forEach(function (d) { d.open = true; });
      document.querySelectorAll("textarea").forEach(autoGrow);
    });
  }

  /* ---------- mount (invoked by the site shell / router) ---------- */
  var built = false;
  var toolbarWired = false;

  // Build the interactive form the first time the Review Template tab is shown.
  // Safe to call repeatedly: the fetch + build only run once.
  function mount() {
    if (!toolbarWired) { wireToolbar(); toolbarWired = true; }
    if (built) {
      // already built once — re-announce so the router can restore the TOC
      try { window.dispatchEvent(new CustomEvent("mesa-form-built")); } catch (e) {}
      return;
    }
    setStatus("Loading template…");
    fetch(TEMPLATE_URL, { cache: "no-store" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.text();
      })
      .then(build)
      .catch(function (err) {
        setStatus(
          "Could not load the template automatically (" + err.message +
            "). If you opened this file directly, use “Load template file…” to pick MESA EFPA template official.md, or serve the folder over http."
        );
        try { window.dispatchEvent(new CustomEvent("mesa-form-error", { detail: { message: err.message } })); } catch (e) {}
      });
  }

  // Resolves once the template has been fetched and built (ids stamped onto
  // blocks), triggering mount() if it hasn't run yet — lets other modules
  // (e.g. the PDF exporter) use the parsed form without visiting its tab first.
  var readyPromise = null;
  function ready() {
    if (built) return Promise.resolve();
    if (readyPromise) return readyPromise;
    readyPromise = new Promise(function (resolve, reject) {
      function onBuilt() { cleanup(); resolve(); }
      function onError(e) { cleanup(); reject(new Error((e.detail && e.detail.message) || "template failed to load")); }
      function cleanup() {
        window.removeEventListener("mesa-form-built", onBuilt);
        window.removeEventListener("mesa-form-error", onError);
      }
      window.addEventListener("mesa-form-built", onBuilt);
      window.addEventListener("mesa-form-error", onError);
      mount();
    });
    return readyPromise;
  }

  window.MesaForm = {
    mount: mount,
    isBuilt: function () { return built; },
    ready: ready,
    getBlocks: function () { return blocks; },
    getAnswers: function () { return state.answers; }
  };
})();
