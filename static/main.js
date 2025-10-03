// static/main.js

// --- 1) Niemals automatisch irgendwohin springen
(function hardCancelAutoScroll() {
  try {
    if ('scrollRestoration' in history) {
      history.scrollRestoration = 'manual';
    }
    // Hash entfernen (z.B. wenn extern mit #map verlinkt wurde)
    if (location.hash) {
      history.replaceState({}, document.title, location.pathname + location.search);
    }
  } catch (e) {}

  // Mehrfach oben halten, falls irgendwas später reinfunkt (iframes/fonts)
  let ticks = 0;
  const stopper = setInterval(() => {
    window.scrollTo(0, 0);
    if (++ticks > 30) clearInterval(stopper); // ~1.5s
  }, 50);
})();

// --- 2) Karte nur "on demand" einfügen (kein Fokus, kein Jump)
(function lazyMountMap() {
  const mount = document.getElementById('map-mount');
  if (!mount) return;

  const src = mount.getAttribute('data-src');
  let mounted = false;

  function injectIframe() {
    if (mounted) return;
    mounted = true;

    // iFrame erstellen
    const ifr = document.createElement('iframe');
    ifr.src = src;
    ifr.loading = 'lazy';
    ifr.setAttribute('title', 'Interaktive Karte');
    ifr.setAttribute('tabindex', '-1');         // nicht fokussieren
    ifr.setAttribute('aria-hidden', 'true');     // der Fokus soll oben bleiben
    ifr.style.width = '100%';
    ifr.style.height = '100%';
    ifr.style.border = '0';
    ifr.addEventListener('load', () => {
      try { ifr.blur(); } catch (e) {}
    });

    mount.innerHTML = ''; // Platzhalter entfernen
    mount.appendChild(ifr);
  }

  // Button-Click
  const btn = document.getElementById('map-manual-load');
  if (btn) btn.addEventListener('click', injectIframe);

  // Auto laden, wenn in Sicht
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        injectIframe();
        obs.disconnect();
      }
    });
  }, { rootMargin: '200px 0px' });
  obs.observe(mount);
})();
