// Uso: node medir-piezas.js urtz.html salida.json  -> palabras y caracteres de cada pieza, con categoría, subsección y zona (URS/URIM).
let chromium;
try { ({ chromium } = require('playwright')); } catch (e) { ({ chromium } = require('/opt/node-tools/node_modules/playwright')); }
(async () => {
  const browser = await chromium.launch({ args:['--no-sandbox'] });
  const page = await browser.newPage();
  await page.goto('file://' + process.argv[2]);
  const out = await page.evaluate(() => {
    const front = document.getElementById('go-informes');
    const els = [...document.querySelectorAll('[data-nivel], details.pieza')];
    let cat='', sub='', rows=[];
    for (const e of els) {
      const nv = e.getAttribute('data-nivel');
      if (e.matches('details.pieza')) {
        const t = e.textContent; 
        const sum = (e.querySelector('summary')||{}).textContent||'';
        const inUrim = front ? !!(front.compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING) : null;
        rows.push({cat, sub, zone: inUrim?'URIM':'URS', title: sum.replace(/\s+/g,' ').trim().slice(0,70), words: t.split(/\s+/).filter(Boolean).length, chars: t.length, excl: !!e.closest('[data-excluir-total]')});
      } else if (nv==='categoria') { cat = (e.textContent||'').replace(/\s+/g,' ').trim().slice(0,60); sub=''; }
      else if (nv==='sub') { sub = (e.textContent||'').replace(/\s+/g,' ').trim().slice(0,60); }
    }
    return rows;
  });
  require('fs').writeFileSync(process.argv[3], JSON.stringify(out,null,1));
  console.log(out.length);
  await browser.close();
})();
