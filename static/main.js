// Verhindert, dass der Browser beim Reload/Zurück automatisch weit nach unten springt
try {
  if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
  }
} catch(e){}

// Falls ein Hash in der URL ist (#karte usw.), verhindern wir Sprung direkt beim Laden
document.addEventListener('DOMContentLoaded', () => {
  // Workaround: id "karte" kurz entfernen, danach wieder setzen
  const mapSec = document.getElementById('karte');
  let restoreId = false;
  if (mapSec) {
    mapSec.id = '';
    restoreId = true;
  }

  // Immer beim ersten Laden ganz nach oben
  if (!sessionStorage.getItem('landedOnce')) {
    window.scrollTo({top: 0, left: 0, behavior: 'instant'});
    sessionStorage.setItem('landedOnce', '1');
  }

  // id zurücksetzen nach minimaler Verzögerung
  setTimeout(() => {
    if (restoreId && mapSec) mapSec.id = 'karte';
  }, 60);
});
