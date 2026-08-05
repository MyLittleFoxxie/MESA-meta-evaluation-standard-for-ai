/* MESA site shell
 * Lightweight hash router that turns the single review form into a multi-tab
 * static site: Home (README), Review Template (the interactive form built by
 * mesa-form.js), Case Studies (the pilot reviews under reviews/), and About.
 *
 * Read-only tabs reuse the vendored marked.js + mermaid.js already loaded for
 * the form, so there are no new dependencies. Everything is fetched with
 * relative paths so it works unchanged under a GitHub Pages project subpath.
 */
(function () {
  "use strict";

  var BENCHMARKS = [
    { id: "Humanitys-Last-Exam", label: "Humanity's Last Exam" },
    { id: "ARC-AGI-2", label: "ARC-AGI-2" },
    { id: "DesignQA", label: "DesignQA" }
  ];
  var REVIEWERS = [
    { id: "gemini_supervising_editor", label: "Reconciled — Supervising Editor", model: "Gemini", featured: true },
    { id: "chatgpt_reviewer1", label: "Reviewer 1", model: "ChatGPT" },
    { id: "claude_reviewer2", label: "Reviewer 2", model: "Claude" }
  ];
  var DEFAULT_BENCHMARK = BENCHMARKS[0].id;
  var DEFAULT_REVIEWER = REVIEWERS[0].id; // featured reconciled review

  // remembered Case Studies selection (so clicking the tab restores it).
  // benchmark === null means the Overview (About) is shown.
  var caseSel = { benchmark: null, reviewer: DEFAULT_REVIEWER };

  var docCache = Object.create(null); // url -> raw markdown text

  /* ---------- small DOM helpers ---------- */
  function $(id) { return document.getElementById(id); }
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function setStatus(msg) { var s = $("mesa-status"); if (s) s.textContent = msg || ""; }
  function known(list, id) {
    for (var i = 0; i < list.length; i++) if (list[i].id === id) return list[i];
    return null;
  }

  /* ---------- table of contents (shared by all views) ---------- */
  // selectorMap: array of { sel: CSS, level: 1|2|3 } in document order priority
  function buildToc(container, selectorMap) {
    var toc = $("mesa-toc");
    if (!toc) return;
    toc.innerHTML = "";
    if (!container) return;
    var seen = 0;

    // collect headings in document order with their level
    var wantSel = selectorMap.map(function (m) { return m.sel; }).join(",");
    var nodes = container.querySelectorAll(wantSel);
    nodes.forEach(function (node) {
      var level = 3;
      for (var i = 0; i < selectorMap.length; i++) {
        if (node.matches(selectorMap[i].sel)) { level = selectorMap[i].level; break; }
      }
      var text = (node.textContent || "").replace(/\s+/g, " ").trim();
      if (!text) return;
      if (!node.id) node.id = "toc-" + (seen++);
      var a = el("a", "mesa-toc-l" + level, text);
      a.href = "#" + node.id; // visual only; click handled below to avoid route change
      a.addEventListener("click", function (e) {
        e.preventDefault();
        var det = node.closest ? node.closest("details.mesa-section") : null;
        if (det) det.open = true;
        node.scrollIntoView({ behavior: "smooth", block: "start" });
      });
      toc.appendChild(a);
    });
  }

  function tocForForm() {
    buildToc($("mesa-form"), [
      { sel: ".mesa-part", level: 1 },
      { sel: "details.mesa-section > summary", level: 2 },
      { sel: ".mesa-h3", level: 3 }
    ]);
  }
  function tocForDoc() {
    buildToc($("mesa-doc"), [
      { sel: "h1", level: 1 },
      { sel: "h2", level: 2 },
      { sel: "h3", level: 3 }
    ]);
  }

  /* ---------- read-only markdown rendering ---------- */
  function renderMarkdownInto(container, md) {
    var html;
    try { html = window.marked.parse(md); }
    catch (e) { html = "<pre>" + md.replace(/[&<>]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c];
    }) + "</pre>"; }
    container.innerHTML = html;

    // upgrade ```mermaid fences (marked -> <pre><code class="language-mermaid">)
    var mnodes = [];
    container.querySelectorAll("code.language-mermaid").forEach(function (code) {
      var holder = el("div", "mesa-figure");
      var node = el("div", "mermaid");
      node.textContent = code.textContent; // decoded source
      holder.appendChild(node);
      var pre = code.closest("pre") || code;
      pre.replaceWith(holder);
      mnodes.push(node);
    });
    if (mnodes.length && window.mermaid) {
      try {
        window.mermaid.initialize({ startOnLoad: false, securityLevel: "loose" });
        window.mermaid.run({ nodes: mnodes });
      } catch (e) {
        mnodes.forEach(function (n) {
          var pre = el("pre", "mesa-code");
          pre.textContent = n.textContent;
          n.replaceWith(pre);
        });
      }
    }
  }

  // Render markdown fetched from `url` into #mesa-doc. `intro` is optional HTML
  // inserted above the rendered content (used to feature the editor review).
  function showDoc(url, intro) {
    var doc = $("mesa-doc");
    if (!doc) return;

    function paint(md) {
      renderMarkdownInto(doc, md);
      if (intro) doc.insertAdjacentHTML("afterbegin", intro);
      doc.scrollTop = 0;
      window.scrollTo({ top: 0 });
      tocForDoc();
      setStatus("");
    }

    if (docCache[url] != null) { paint(docCache[url]); return; }

    setStatus("Loading…");
    fetch(url, { cache: "no-store" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.text();
      })
      .then(function (md) { docCache[url] = md; paint(md); })
      .catch(function (err) {
        doc.innerHTML = "";
        setStatus(
          "Could not load “" + url + "” (" + err.message + "). " +
          "The Home, Case Studies and About tabs need the site to be served over http " +
          "(e.g. GitHub Pages, or run a local static server from the repo root). " +
          "They do not work when the page is opened directly from disk (file://)."
        );
        buildToc(null, []);
      });
  }

  function showAbout() {
    var doc = $("mesa-doc");
    var tpl = $("mesa-about-md");
    if (!doc || !tpl) return;
    renderMarkdownInto(doc, tpl.innerHTML);
    window.scrollTo({ top: 0 });
    tocForDoc();
    setStatus("");
  }

  /* ---------- view switching ---------- */
  function setView(view) {
    document.body.setAttribute("data-view", view);
    // toolbar/progress visibility is driven by [data-view] in CSS
    var form = $("mesa-form");
    var doc = $("mesa-doc");
    var caseNav = $("mesa-case-nav");
    var showForm = view === "template";
    if (form) form.hidden = !showForm;
    if (doc) doc.hidden = showForm;
    if (caseNav) caseNav.hidden = view !== "case";
    // active tab styling
    document.querySelectorAll(".mesa-tab").forEach(function (b) {
      b.classList.toggle("is-active", b.dataset.route === view);
    });
  }

  /* ---------- Case Studies secondary nav ---------- */
  function buildCaseNav() {
    var bWrap = $("mesa-case-benchmarks");
    var rWrap = $("mesa-case-reviewers");
    if (!bWrap || !rWrap) return;
    bWrap.innerHTML = "";
    rWrap.innerHTML = "";

    // Overview (About) pill — leads the case-study row and is the default view
    var ov = el("button", "mesa-pill mesa-pill-overview", "Overview");
    ov.type = "button";
    ov.dataset.id = "overview";
    ov.addEventListener("click", function () {
      caseSel.benchmark = null;
      location.hash = caseHash();
    });
    bWrap.appendChild(ov);

    BENCHMARKS.forEach(function (b) {
      var btn = el("button", "mesa-pill", b.label);
      btn.type = "button";
      btn.dataset.id = b.id;
      btn.addEventListener("click", function () {
        caseSel.benchmark = b.id;
        location.hash = caseHash();
      });
      bWrap.appendChild(btn);
    });

    REVIEWERS.forEach(function (rv) {
      var label = rv.label + (rv.model ? " (" + rv.model + ")" : "");
      var btn = el("button", "mesa-pill" + (rv.featured ? " mesa-pill-featured" : " mesa-pill-draft"), label);
      btn.type = "button";
      btn.dataset.id = rv.id;
      if (rv.featured) btn.appendChild(el("span", "mesa-badge", "authoritative"));
      btn.addEventListener("click", function () {
        caseSel.reviewer = rv.id;
        location.hash = caseHash();
      });
      rWrap.appendChild(btn);
    });
  }

  function syncCaseNavActive() {
    var isOverview = !caseSel.benchmark;
    document.querySelectorAll("#mesa-case-benchmarks .mesa-pill").forEach(function (b) {
      var active = isOverview ? b.dataset.id === "overview" : b.dataset.id === caseSel.benchmark;
      b.classList.toggle("is-active", active);
    });
    document.querySelectorAll("#mesa-case-reviewers .mesa-pill").forEach(function (b) {
      b.classList.toggle("is-active", b.dataset.id === caseSel.reviewer);
    });
    // the Reviewer row only applies once a specific case study is chosen
    var rrow = $("mesa-case-reviewer-row");
    if (rrow) rrow.hidden = isOverview;
  }

  function caseHash() {
    if (!caseSel.benchmark) return "case/overview";
    return "case/" + caseSel.benchmark + "/" + caseSel.reviewer;
  }

  function reviewUrl(benchmark, reviewer) {
    return "reviews/" + reviewer + "/" + benchmark + ".md";
  }

  function showCase() {
    syncCaseNavActive();

    // Overview (no specific case study selected) → render the About explanation
    if (!caseSel.benchmark) {
      showAbout();
      return;
    }

    var rv = known(REVIEWERS, caseSel.reviewer);
    var b = known(BENCHMARKS, caseSel.benchmark);
    var model = rv && rv.model ? rv.model : "an AI model";
    var intro = "";
    if (rv && rv.featured) {
      intro =
        '<div class="mesa-doc-note mesa-doc-note-editor">' +
        "<strong>AI model: " + model + ".</strong> Reconciled review by the Supervising Editor — " +
        "the authoritative, source-grounded evaluation of <em>" + (b ? b.label : caseSel.benchmark) +
        "</em>, reconciling the two independent reviewer drafts. Use the Reviewer selector above to inspect those drafts." +
        "</div>";
    } else if (rv) {
      intro =
        '<div class="mesa-doc-note mesa-doc-note-draft">' +
        "<strong>AI model: " + model + ".</strong> Independent reviewer draft (" + rv.label + "), shown for " +
        "transparency. The authoritative version is the reconciled <em>Supervising Editor</em> review." +
        "</div>";
    }
    showDoc(reviewUrl(caseSel.benchmark, caseSel.reviewer), intro);
  }

  /* ---------- router ---------- */
  function parseHash() {
    var raw = (location.hash || "").replace(/^#/, "");
    var parts = raw.split("/").filter(Boolean);
    var head = parts[0] || "home";
    if (head === "template") return { view: "template" };
    // legacy #about now lands on the Case Studies Overview
    if (head === "about" || head === "case") {
      if (head === "case" && known(BENCHMARKS, parts[1])) {
        caseSel.benchmark = parts[1];
        if (known(REVIEWERS, parts[2])) caseSel.reviewer = parts[2];
      } else {
        caseSel.benchmark = null; // overview
      }
      return { view: "case" };
    }
    return { view: "home" };
  }

  function route() {
    var r = parseHash();
    setView(r.view);
    switch (r.view) {
      case "template":
        // hand off to the form; it rebuilds the TOC via the mesa-form-built event
        if (window.MesaForm) window.MesaForm.mount();
        break;
      case "case":
        showCase();
        break;
      default: // home
        showDoc("README.md", null);
    }
  }

  /* ---------- tabs + wiring ---------- */
  function wireTabs() {
    document.querySelectorAll(".mesa-tab").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var route = btn.dataset.route;
        if (route === "case") location.hash = caseHash();
        else location.hash = route;
      });
    });

    var print = $("btn-print");
    if (print) print.addEventListener("click", function () { window.print(); });

    var exportPdf = $("btn-export-pdf");
    if (exportPdf) exportPdf.addEventListener("click", function () {
      if (window.MesaPdf) window.MesaPdf.exportPdf();
    });
  }

  function init() {
    buildCaseNav();
    wireTabs();
    // when the form finishes (re)building, refresh the sidebar TOC if it's active
    window.addEventListener("mesa-form-built", function () {
      if (document.body.getAttribute("data-view") === "template") tocForForm();
    });
    window.addEventListener("hashchange", route);
    route(); // initial view from the current hash (defaults to Home)
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
