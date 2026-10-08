/* MESA site shell
 * Lightweight hash router that turns the single review form into a multi-tab
 * static site: Home (README), Review Template (the interactive form built by
 * mesa-form.js), Survey (MESA-25 questions and examples), and Case Studies.
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
  var viewToken = 0; // prevents a late fetch from replacing a newer tab

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
  function showDoc(url, intro, resolveLinks) {
    var doc = $("mesa-doc");
    if (!doc) return;
    var token = viewToken;

    function paint(md) {
      if (token !== viewToken) return;
      renderMarkdownInto(doc, md);
      if (resolveLinks) {
        doc.querySelectorAll("a[href]").forEach(function (link) {
          var href = link.getAttribute("href");
          var routes = { "designqa-example.md": "#survey/designqa-report", "designqa-comparison.md": "#survey/designqa-comparison", "questionnaire.md": "#survey" };
          if (routes[href]) link.href = routes[href];
          else if (href && href[0] !== "#") link.href = new URL(href, new URL(url, location.href)).href;
        });
      }
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
        if (token !== viewToken) return;
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

  function showSurvey(completed) {
    var doc = $("mesa-doc");
    var token = viewToken;
    doc.replaceChildren();
    buildToc(null, []);
    setStatus("Loading survey…");
    var files = ["questions.json", "introduction.json"];
    if (completed) files.push("designqa-example.json");
    Promise.all(files.map(function (name) {
      return fetch("proposals/mesa-25/" + name, { cache: "no-store" })
        .then(function (response) {
          if (!response.ok) throw new Error("HTTP " + response.status);
          return response.json();
        });
    }))
      .then(function (data) {
        var questions = data[0];
        var introduction = data[1];
        var worked = completed ? data[2] : null;
        if (token !== viewToken) return;
        if (!Array.isArray(questions) || questions.length !== 25 ||
            !questions.every(function (q, i) {
              return q.id === i + 1 && typeof q.domain === "string" &&
                typeof q.question === "string" && typeof q.example === "string" &&
                typeof q.explanation === "string" &&
                q.kind === (i < 5 ? "description" : "evaluation");
            })) throw new Error("The survey data is incomplete.");

        if (!Array.isArray(introduction) || !introduction.length ||
            !introduction.every(function (item) {
              return typeof item.term === "string" && typeof item.meaning === "string";
            })) throw new Error("The survey introduction is incomplete.");

        if (completed && (!worked || !Array.isArray(worked.answers) || worked.answers.length !== 25 ||
            !worked.answers.every(function (a, i) {
              return a.id === i + 1 && ["Yes", "Partly", "No", "Not sure", "Not applicable"].indexOf(a.answer) !== -1 &&
                typeof a.comment === "string" && typeof a.sources === "string";
            }))) throw new Error("The completed example is incomplete.");

        doc.appendChild(el("h1", null, completed ? "DesignQA — completed Survey example" : "Survey — MESA-25"));
        var surveyNav = el("p");
        [["Colleague survey: ARC-AGI-2 and HLE", "surveys/colleague-review/survey.html"], ["Blank questionnaire", "#survey"], ["Completed DesignQA example", "#survey/designqa"], ["Comparison with original reviews", "#survey/designqa-comparison"], ["Detailed sources and report", "#survey/designqa-report"]].forEach(function (item, i) {
          if (i) surveyNav.appendChild(document.createTextNode(" · "));
          var link = el("a", null, item[0]);
          link.href = item[1];
          surveyNav.appendChild(link);
        });
        doc.appendChild(surveyNav);
        if (worked) {
          doc.appendChild(el("p", "mesa-doc-note", worked.status + ". " + worked.date));
          doc.appendChild(el("p", null, worked.scope));
          doc.appendChild(el("p", null, worked.method));
          doc.appendChild(el("p", null, worked.conclusion));
          doc.appendChild(el("p", null, "This saved example is read-only. The blank questionnaire remains available for your own answers. Source IDs in the comments are explained in Detailed sources and report."));
        }
        doc.appendChild(el("p", null, "25 questions in six domains: five descriptive questions and twenty evaluative questions."));
        doc.appendChild(el("p", "mesa-doc-note mesa-doc-note-draft", "Experimental draft 0.2. This short form has not been validated: it has not yet been shown to produce dependable review judgments."));
        doc.appendChild(el("h2", null, "Before you begin"));
        introduction.forEach(function (item) {
          var paragraph = el("p");
          paragraph.appendChild(el("strong", null, item.term + ". "));
          paragraph.appendChild(document.createTextNode(item.meaning));
          doc.appendChild(paragraph);
        });
        doc.appendChild(el("p", null, "This review concerns one version of a benchmark and one intended use. Q1–Q5 ask whether the test is described. Q6–Q25 ask about its methods and claims."));

        var sources = el("p");
        var sourceLink = el("a", null, "Example sources and qualifications");
        sourceLink.href = "proposals/mesa-25/example-sources.md";
        sources.appendChild(sourceLink);
        doc.appendChild(sources);

        var answers = el("details");
        answers.open = true;
        answers.appendChild(el("summary", null, "Answer guide"));
        var list = el("ul");
        [
          "Yes: the question is satisfied.",
          "Partly: some parts are satisfied, but not all.",
          "No: the question is not satisfied.",
          "Not sure: there is not enough information to decide.",
          "Not applicable: the issue does not apply to this benchmark."
        ].forEach(function (text) { list.appendChild(el("li", null, text)); });
        answers.appendChild(list);
        answers.appendChild(el("p", null, "Choose one answer per question. No written explanation, evidence, citations or closing summary is required. Missing information alone does not mean No. For questions about whether a check was performed, Yes means it was performed, not that its result was favourable. No total score is calculated. Comments are optional. Answers and comments are not saved after leaving or reloading this page."));
        doc.appendChild(answers);

        var domain = null;
        questions.forEach(function (q) {
          if (q.domain !== domain) {
            domain = q.domain;
            doc.appendChild(el("h2", null, domain));
          }
          doc.appendChild(el("h3", null, "Q" + q.id + ". " + q.question));
          doc.appendChild(el("p", "mesa-survey-explanation", q.explanation));
          var example = el("p");
          example.appendChild(el("em", null, "Example: " + q.example));
          doc.appendChild(example);
          var options = el("fieldset", "mesa-survey-options");
          options.appendChild(el("legend", null, "Answer to Q" + q.id));
          ["Yes", "Partly", "No", "Not sure", "Not applicable"].forEach(function (answer) {
            var label = el("label");
            label.style.display = "inline-block";
            label.style.margin = "0 1rem 0.5rem 0";
            var input = el("input");
            input.type = "radio";
            input.name = "survey-q" + q.id;
            input.value = answer;
            if (worked) {
              input.checked = worked.answers[q.id - 1].answer === answer;
              input.disabled = true;
            }
            label.appendChild(input);
            label.appendChild(document.createTextNode(" " + answer));
            options.appendChild(label);
          });
          var response = el("div", "mesa-survey-response");
          response.appendChild(options);
          var comments = el("div", "mesa-survey-comments");
          var commentLabel = el("label", null, "Comments (optional)");
          commentLabel.htmlFor = "survey-comments-" + q.id;
          var commentInput = el("textarea");
          commentInput.id = commentLabel.htmlFor;
          commentInput.name = "survey-comments-" + q.id;
          commentInput.rows = worked ? 12 : 3;
          if (worked) {
            commentInput.value = worked.answers[q.id - 1].comment + "\n\nSources: " + worked.answers[q.id - 1].sources;
            commentInput.readOnly = true;
          }
          comments.appendChild(commentLabel);
          comments.appendChild(commentInput);
          response.appendChild(comments);
          doc.appendChild(response);
        });
        tocForDoc();
        window.scrollTo({ top: 0 });
        setStatus("");
      })
      .catch(function (err) {
        if (token !== viewToken) return;
        doc.replaceChildren();
        buildToc(null, []);
        setStatus("Could not load the survey (" + err.message + "). Reload the page to try again.");
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
    var paper = $("mesa-paper-frame");
    var caseNav = $("mesa-case-nav");
    var showForm = view === "template" || view === "scorecard";
    if (form) form.hidden = !showForm;
    if (doc) doc.hidden = showForm || view === "paper";
    if (paper) paper.hidden = view !== "paper";
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
    if (head === "scorecard") return { view: "scorecard" };
    if (head === "survey") return { view: "survey", page: parts[1] || "" };
    if (head === "paper") return { view: "paper" };
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
    viewToken++;
    var r = parseHash();
    setView(r.view);
    switch (r.view) {
      case "template":
      case "scorecard":
        // hand off to the form; it rebuilds the TOC via the mesa-form-built event
        if (window.MesaForm) window.MesaForm.mount(r.view);
        break;
      case "case":
        showCase();
        break;
      case "survey":
        if (r.page === "designqa-comparison" || r.page === "designqa-report") {
          showDoc("proposals/mesa-25/" + (r.page === "designqa-comparison" ? "designqa-comparison.md" : "designqa-example.md"),
            '<p><a href="#survey">Blank questionnaire</a> · <a href="#survey/designqa">Completed DesignQA example</a> · <a href="#survey/designqa-comparison">Comparison</a> · <a href="#survey/designqa-report">Sources and report</a></p>', true);
        } else showSurvey(r.page === "designqa");
        break;
      case "paper":
        buildToc(null, []);
        setStatus("");
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

    var exportPdf = $("btn-print");
    if (exportPdf) exportPdf.addEventListener("click", function () {
      if (window.MesaPdf) window.MesaPdf.exportPdf();
    });
  }

  function init() {
    buildCaseNav();
    wireTabs();
    // when the form finishes (re)building, refresh the sidebar TOC if it's active
    window.addEventListener("mesa-form-built", function () {
      var v = document.body.getAttribute("data-view");
      if (v === "template" || v === "scorecard") tocForForm();
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
