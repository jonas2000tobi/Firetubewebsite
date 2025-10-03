// static/main.js

// Verhindert Sprung/Autoscroll (z.B. zur Karte) nach dem Laden
(function () {
  try {
    if ('scrollRestoration' in history) {
      history.scrollRestoration = 'manual';
    }
    // Falls die Seite mit #hash geladen wurde -> Hash entfernen, sonst scrollt der Browser dorthin
    if (location.hash) {
      history.replaceState({}, document.title, location.pathname + location.search);
    }
    // Sicher oben bleiben
    window.scrollTo(0, 0);
  } catch (e) {}
})();

// iFrames nicht fokussieren (manche Browser springen sonst zum iFrame)
window.addEventListener('load', () => {
  document.querySelectorAll('iframe').forEach(f => {
    f.setAttribute('tabindex', '-1');
    try { f.blur(); } catch(e) {}
  });
});
