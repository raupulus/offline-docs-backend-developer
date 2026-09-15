/* ═══════════════════════════════════════════════════════════════════
   Visor de documentación offline

   RESTRICCIÓN CLAVE: este sitio se abre desde file://, donde el
   navegador bloquea fetch() y XMLHttpRequest por política de origen.
   Sí permite cargar <script src="...">, así que el índice de búsqueda
   se distribuye como JavaScript que declara window.DOCS_INDEX, y aquí
   se carga inyectando una etiqueta script bajo demanda.

   Cambiar esto a fetch() rompería el buscador sin servidor.
   ═══════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ── Tema ──────────────────────────────────────────────────────── */

  var root = document.documentElement;

  function currentTheme() {
    var set = root.getAttribute('data-theme');
    if (set === 'light' || set === 'dark') return set;
    return window.matchMedia('(prefers-color-scheme: dark)').matches
      ? 'dark' : 'light';
  }

  document.addEventListener('click', function (ev) {
    var button = ev.target.closest('[data-theme-toggle]');
    if (!button) return;
    var next = currentTheme() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('docs-theme', next); } catch (e) {}
  });

  /* ── Menú lateral ──────────────────────────────────────────────── */

  document.addEventListener('click', function (ev) {
    var toggle = ev.target.closest('[data-nav-toggle]');
    if (toggle) {
      var nav = document.querySelector('[data-nav]');
      if (!nav) return;
      var open = nav.classList.toggle('is-visible');
      toggle.setAttribute('aria-expanded', String(open));
      return;
    }

    // Los títulos de sección pliegan y despliegan su lista
    var title = ev.target.closest('.nav-section-title');
    if (title && title.parentElement) {
      title.parentElement.classList.toggle('is-open');
    }
  });

  /* ── Carga del índice de búsqueda ──────────────────────────────── */

  var loading = {};

  function loadIndex(url) {
    if (loading[url]) return loading[url];

    loading[url] = new Promise(function (resolve) {
      var script = document.createElement('script');
      script.src = url;
      // Sin rechazo: si el índice falta, el buscador queda inerte pero
      // la página sigue siendo perfectamente navegable.
      script.onload = function () { resolve(true); };
      script.onerror = function () { resolve(false); };
      document.head.appendChild(script);
    });

    return loading[url];
  }

  /* ── Buscador ──────────────────────────────────────────────────── */

  // Sin acentos y en minúsculas, para que "sesion" encuentre "sesión".
  // El rango va escrito con escapes y no con los caracteres literales:
  // son marcas combinantes invisibles y cualquier recodificación del
  // fichero las estropearía sin dejar rastro.
  var DIACRITICOS = new RegExp('[\\u0300-\\u036f]', 'g');

  function normalize(text) {
    return text
      .toLowerCase()
      .normalize('NFD')
      .replace(DIACRITICOS, '');
  }

  function entriesFor(tech) {
    var store = window.DOCS_INDEX || {};
    if (tech !== '*') return store[tech] || [];

    var all = [];
    Object.keys(store).forEach(function (key) {
      all = all.concat(store[key] || []);
    });
    return all;
  }

  function score(entry, terms) {
    var title = normalize(entry.t || '');
    var section = normalize(entry.s || '');
    var body = normalize(entry.b || '');
    var total = 0;

    for (var i = 0; i < terms.length; i++) {
      var term = terms[i];
      if (title.indexOf(term) === 0) total += 100;
      else if (title.indexOf(term) !== -1) total += 60;
      else if (section.indexOf(term) !== -1) total += 20;
      else if (body.indexOf(term) !== -1) total += 8;
      else return 0;  // todos los términos deben aparecer
    }
    return total;
  }

  function setup(box) {
    var input = box.querySelector('.search-input');
    var panel = box.querySelector('.search-results');
    var tech = box.getAttribute('data-tech');
    var indexUrl = box.getAttribute('data-index');
    var base = indexUrl.replace(/[^/]*$/, '');
    var active = -1;

    function close() {
      panel.hidden = true;
      panel.innerHTML = '';
      active = -1;
    }

    function render(hits) {
      if (!hits.length) {
        panel.innerHTML = '<p class="search-empty">Sin resultados</p>';
        panel.hidden = false;
        return;
      }

      panel.innerHTML = '';

      hits.forEach(function (hit) {
        var link = document.createElement('a');
        link.className = 'search-hit';
        link.href = base + hit.u;

        var title = document.createElement('strong');
        var label = document.createElement('small');

        // textContent y no innerHTML: nada de lo que venga del
        // contenido de la documentación debe interpretarse como HTML.
        title.textContent = hit.t;
        label.textContent = hit.s
          ? (hit.n ? hit.n + ' · ' + hit.s : hit.s)
          : (hit.n || '');

        link.appendChild(title);
        link.appendChild(label);
        panel.appendChild(link);
      });

      panel.hidden = false;
    }

    function search() {
      var raw = input.value.trim();
      if (raw.length < 2) { close(); return; }

      var terms = normalize(raw).split(/\s+/).filter(Boolean);

      var hits = entriesFor(tech)
        .map(function (entry) { return { e: entry, s: score(entry, terms) }; })
        .filter(function (item) { return item.s > 0; })
        .sort(function (a, b) { return b.s - a.s; })
        .slice(0, 25)
        .map(function (item) { return item.e; });

      render(hits);
    }

    input.addEventListener('focus', function () { loadIndex(indexUrl); });

    input.addEventListener('input', function () {
      loadIndex(indexUrl).then(search);
    });

    input.addEventListener('keydown', function (ev) {
      var hits = panel.querySelectorAll('.search-hit');

      if (ev.key === 'Escape') { close(); input.blur(); return; }
      if (!hits.length) return;

      if (ev.key === 'ArrowDown' || ev.key === 'ArrowUp') {
        ev.preventDefault();
        active += (ev.key === 'ArrowDown' ? 1 : -1);
        if (active < 0) active = hits.length - 1;
        if (active >= hits.length) active = 0;
        hits.forEach(function (h, i) {
          h.classList.toggle('is-active', i === active);
        });
        hits[active].scrollIntoView({ block: 'nearest' });
      } else if (ev.key === 'Enter' && active >= 0) {
        ev.preventDefault();
        hits[active].click();
      }
    });

    document.addEventListener('click', function (ev) {
      if (!box.contains(ev.target)) close();
    });
  }

  document.querySelectorAll('[data-search]').forEach(setup);

  /* ── Atajos: / ó Ctrl+K / Cmd+K enfocan el buscador ───────────── */

  document.addEventListener('keydown', function (ev) {
    var isSlash = (ev.key === '/' && !ev.ctrlKey && !ev.metaKey && !ev.altKey);
    var isCmdK = ((ev.key === 'k' || ev.key === 'K') && (ev.ctrlKey || ev.metaKey));
    if (!isSlash && !isCmdK) return;

    var tag = (ev.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || ev.target.isContentEditable) return;

    var input = document.querySelector('.search-input');
    if (!input) return;
    ev.preventDefault();
    input.focus();
    input.select();
  });


  /* ── PWA: Service Worker (solo sobre HTTPS o localhost) ────────── */

  if ('serviceWorker' in navigator && (location.protocol === 'https:' || location.hostname === 'localhost' || location.hostname === '127.0.0.1')) {
    window.addEventListener('load', function () {
      var manifest = document.querySelector('link[rel="manifest"]');
      var swUrl = manifest ? manifest.getAttribute('href').replace(/manifest\.json$/, 'sw.js') : 'sw.js';
      navigator.serviceWorker.register(swUrl).catch(function () {
        // En caso de fallo de registro no afecta la navegación estándar
      });
    });
  }
})();
