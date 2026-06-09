# UR-SAPIENS — NOTAS DE PROYECTO

# ████████████████████████████████████████████████████████████████
# ⊕ OR-GANIGRAMA TOTAL · LOCALIZACIÓN DEFINITIVA · PARA TODOS LOS CLAUDIUS
# Verificado y medido sobre el HTML el 5 jun 2026. MANDA sobre todo lo de abajo.
# ████████████████████████████████████████████████████████████████

> Escrito tras perder tiempo repetidamente localizando mal los índices y el
> Alpha-UR. Si vas a tocar índices, Alpha-UR o fotos: LEE ESTO ENTERO PRIMERO.

## REGLA CERO (la que más tiempo nos ha costado)
El `ur` SIEMPRE va dentro de `<span style="color:#b01a1a;">ur</span>` (y `UR`, `or`,
`OR`, `ru`, `RU` igual). Por eso NINGUNA palabra con UR aparece como texto plano:
"Absurdo" está como `Abs<span...>ur</span>do`. **Buscar SIEMPRE por fragmentos
('Abs', 'Rothsch', 'Ma') o colapsando spans primero — NUNCA por la palabra entera.**

## LOS DOS ARCHIVOS
- `index.html`  → EL LIBRO completo (UR-book + Alpha-UR + Escombrera + 2 sidebars + JS).
                  Enlaza `style.css` EXTERNO.
- `permafrost.html` → EL MURO GLACIAR aparte (qanats; material en bruto). CSS INLINE.
- NORMA DOBLE SALIDA: cada cambio de cuerpo/CSS regenera SIEMPRE `index-local.html`
  (CSS inline, para revisar a doble-clic) + `index.html` (limpio, para GitHub).
  Para GitHub se suben: `index.html` + `permafrost.html` (style.css solo si cambió).

## ███ HAY TRES ZONAS CON DIVISORES `class="il"` ███
## Esta es la trampa nº1. Las tres comparten clase CSS pero NO son lo mismo.
## Distínguelas SIEMPRE por el id del contenedor + formato del divisor + función JS.

┌─────────────────────────────────────────────────────────────────────────┐
│ ZONA 1 · SIDEBAR UR-BOOK            contenedor: <aside id="sidebar">       │
│   posición en archivo: ~245k (la PRIMERA)                                 │
│   divisor de letra:  <div class="il" id="ilA">A</div>   ← LETRA SOLA + id  │
│   enlaces:           class="ie"  ·  onclick rayuela('pub-..')             │
│   destino:           href="#pub-..."  (páginas del UR-book)               │
│   fotos:             SÍ — una foto-emblema por letra (Atlántida=A, etc.)   │
│   contiene además:   índice "PÁGINAS DEL UR-BOOK" (16 entradas + 16 fotos) │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ ZONA 2 · ALPHA-UR (diccionario)     contenedor: id="ur-alfabeto"          │
│   posición en archivo: ~326k (EN MEDIO, dentro del sidebar UR-book)       │
│   divisor de letra:  <div class="il">· A ·</div>   ← CON · X · · SIN id    │
│   contenido:         entradas de DICCIONARIO, no navegación:              │
│                      <span display:block>· Palabra[ur rojo] <span ámbar   │
│                      #7a5a2a italic>— glosa</span></span>                 │
│   destino:           NINGUNO (no son enlaces)                             │
│   fotos:             NO. NI UNA. Solo palabra (ur rojo) + glosa ámbar.    │
│   título:            "UR ALFABETO · NORMA E INVESTIGACIÓN" + zahorí dibujo │
│   nº entradas:       ~360 (crece). id="ur-alfabeto" lo añadimos para el    │
│                      botón "α UR ALFABETO" de los dos índices.            │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ ZONA 3 · SIDEBAR ESCOMBRERA         contenedor: <aside id="escombrera-aside">│
│   posición en archivo: ~565k (la ÚLTIMA)                                  │
│   divisor de letra:  <div class="il">· A ·</div>   ← CON · X · · SIN id    │
│                      (FORMATO IDÉNTICO al Alpha-UR → por eso se confunden) │
│   enlaces:           class="ie"  ·  onclick escRayuela('esc-..')          │
│   destino:           href="#esc-..."  (páginas de la escombrera)          │
│   fotos:             SÍ — algunas entradas llevan foto + glosa 0.75rem.   │
│   nº enlaces:        ~80  ·  nº fotos: 22 (y subiendo, Luis las añade)     │
└─────────────────────────────────────────────────────────────────────────┘

## CÓMO LOCALIZAR SIN FALLAR (líneas de localización)
1. NUNCA buscar "la letra M" a secas: devuelve la zona equivocada (hay 3).
2. Para el SIDEBAR ESCOMBRERA: anclar primero en `<aside id="escombrera-aside"`,
   acotar hasta su `</aside>`, y dentro buscar la entrada por su TEXTO
   (ej. 'Rothschild'), no por la letra. La letra `· R ·` aparece en 3 sitios.
3. Para el ALPHA-UR: anclar en `id="ur-alfabeto"` y acotar hasta
   `id="puente-escombrera"`. Insertar entradas tras el divisor `<div class="il">· X ·</div>`
   (· literal, NO &middot;, en el divisor; PERO las entradas usan &middot; al inicio).
4. Para el SIDEBAR UR-BOOK: anclar en `<aside id="sidebar"` (sin guion) y usar los
   id="ilX" (letra sola), que son ÚNICOS de esta zona.
5. Distinguir función JS: `rayuela(` = UR-book · `escRayuela(` = escombrera.

## ENTRADA CON FOTO EN EL SIDEBAR ESCOMBRERA — PLANTILLA EXACTA
Se inserta JUSTO DESPUÉS del `<a class="ie">` de texto de esa entrada:
```
<a href="#esc-NN" onclick="escRayuela('esc-NN'); return false;" style="display:block; cursor:pointer;"><img src="URL_DIRECTA" alt="DESCRIPCIÓN" style="width:100%; height:auto; display:block; margin:0.4rem 0 0.3rem 0;" onerror="this.style.display='none'"></a>
<p style="font-family:'Courier Prime',monospace; font-size:0.75rem; color:#666; letter-spacing:0.06em; margin-bottom:0.6rem;">· GLOSA con <span style="color:#b01a1a;">UR</span> si aplica ·</p>
```
- URL imagen: directa al archivo (Wikimedia commons/X/XX/... sirve; evitar /thumb/ si se puede). Flickr: el `.png`/`.jpg` directo.
- `onerror="this.style.display='none'"`: oculta la img si el enlace muere (no rompe maqueta).

## ENTRADA NUEVA EN EL ALPHA-UR — PLANTILLA EXACTA
Se inserta tras el divisor `<div class="il">· X ·</div>` de su letra:
```
<span style="display:block; font-family:'Courier Prime',monospace; font-size:1.05rem; color:#0a0a0a; padding:0.2rem 0 0.2rem 1.2em; text-indent:-1.2em; border-bottom:1px solid rgba(0,0,0,0.08); line-height:1.4;">&middot; Pal[ur rojo]abra <span style="font-style:italic; color:#7a5a2a; font-size:0.88rem;">&mdash; glosa</span></span>
```
- VERIFICAR el ur con: idx = palabra.lower().find('ur'); marcar SOLO si idx>=0.
- Contar la entrada DENTRO del alfabeto (no en todo el doc): la palabra puede salir
  también en su propia glosa → 2 ocurrencias es normal, 1 como ENTRADA (display:block).

## FOTOS = INTOCABLES
Todas las fotos (las 3 zonas) las elige LUIS. NUNCA se borran ni se proponen borrar.
Claudius solo AÑADE cuando Luis pasa una imagen + letra + aprueba glosa.

## VERIFICACIÓN OBLIGATORIA tras tocar índices/alfabeto/fotos
- spans abren == cierran  (`<span` vs `</span>`)
- 0 spans dentro de atributos: regex `(?:alt|src|href|style)="[^"]*<span`
- articles 23/23 en index
- funciones JS intactas: rayuela, escRayuela, toggleOrden, toggleEscombrera, aplicarOrden, urOrdenDiario, escBuscar
- la entrada nueva aparece 1× como entrada (no duplicada)



# ████████████████████████████████████████████████████████
# LOSA SUPREMA · ORGANIGRAMA DE LA GUERRILLA UR-SAPIENS
# (estructura REAL del HTML — leer ANTES de tocar nada)
# ████████████████████████████████████████████████████████

**REGLA CERO: antes de buscar cualquier palabra en el HTML, recordar que el `ur`
va dentro de `<span style="color:#b01a1a;">ur</span>`. Por eso "Absurdo" NUNCA
aparece como texto plano: está como `Abs<span...>ur</span>do`. Buscar SIEMPRE
colapsando los spans primero, o por fragmentos ('Abs', 'do'), NUNCA por la palabra entera.**

## DOS ARCHIVOS
- `index.html` → EL LIBRO (UR-book + Alpha-UR + Escombrera + los 2 sidebars)
- `permafrost.html` → EL MURO GLACIAR (62 qanats, yacimiento)

## index.html — ESTRUCTURA REAL

1. **#ur-titulo** — portada.
2. **#ur-book-main** — EL UR-BOOK: 16 páginas `pub-*` (qanats, madres, nietzsche,
   inanna, asia, digitalismo, tauros, palimpsesto, finisur, cosmos, tsunami,
   basura, urabe, intro, prefacio, precedentes).
3. **#sidebar** — SIDEBAR 1 (del UR-book). Contiene TRES cosas distintas:
   a) Buscador (#bur-input → #ur-resultados) + botón 4 lecturas (#btnOrden).
   b) **"PÁGINAS DEL UR-BOOK"** = ÍNDICE de páginas: 16 entradas + **16 fotos**
      (una por página 0000–0014). Fotos elegidas por Luis. NO TOCAR.
   c) **#burNav (ilA…ilZ)** = ÍNDICE ILUSTRADO TEMÁTICO + ALPHA-UR. OJO, ilZ es
      enorme porque ahí vive además:
      - El **ÍNDICE ilustrado**: cada letra con su **foto-emblema** (Atlántida en A,
        Babilonia en B, Inanna en I…) + entradas temáticas `.ie` que enlazan a páginas.
        Las fotos por letra las eligió Luis. NO TOCAR.
      - El **ALPHA-UR** propiamente: título "UR ALFABETO · NORMA E INVESTIGACIÓN",
        ilustración del zahorí (Borja González Hoyos), y la lista A→Z de
        **~316 entradas palabra + glosa zahorí ámbar** (#7a5a2a). ESTO ES EL ALPHA-UR.
        **El Alpha-UR NO lleva fotos. Ni una.** Solo palabra (con ur rojo) + glosa ámbar.
4. **#escombrera-wrapper** — LA ESCOMBRERA: 7 páginas `esc-*`.
5. **#escombrera-aside** — SIDEBAR 2 (de la escombrera): buscador + índice
   escombrera (80 entradas + 24 fotos). Fotos elegidas por Luis. NO TOCAR.

## DISTINCIÓN CRÍTICA (donde Claude se perdió y agotó a Luis)
- **ÍNDICE ilustrado (burNav, entradas .ie temáticas + foto por letra)** = navegación.
  Entradas tipo "· Kurosawa · Pantano Negro · UR-BELTZ". CON fotos por letra.
- **ALPHA-UR (lista A→Z, palabra + glosa ámbar)** = el diccionario insurgente.
  Entradas tipo "· Absurdo — sinsentido; acción de alejarse del manantial". SIN fotos.
- Son COSAS DISTINTAS dentro del mismo sidebar. No confundirlas jamás.

## FOTOS DEL LIBRO — INVENTARIO INTOCABLE
16 (índice páginas) + 26 (emblemas por letra del índice ilustrado) + 24 (índice
escombrera) = **66 fotos elegidas por Luis. NUNCA se borran ni se proponen borrar.**


### Fuente de verdad única · Beltza Experience · Doneztebe · 2025–2026
### ⟐ Sincronizado con la obra: **1 junio 2026**

---

## ESTADO REAL HOY (1 junio 2026) — LO QUE HAY EN DISCO

> Este bloque manda sobre cualquier cifra antigua que aparezca más abajo. Si algo
> de las secciones históricas contradice esto, esto es lo verdadero.

- **`index.html`** — UR-book (15 págs: prefacio + pub-intro→pub-qanats) + Escombrera (**7 págs**: esc-prefacio + esc-01→**esc-06**) + sidebar + aside + JS. ~1,1 MB · 4.111 spans UR. Enlaza `style.css` externo.
- **`permafrost.html`** — Muro Glaciar separado. **61 depósitos** (qanat-60 → qanat-01 → qanat--01); qanat-00 ascendió al libro como pub-precedentes, todos en disco. CSS inline. **Orden DOM = inverso-numérico (60→00→-01)**. El `qanat--01` (Camarón · ¿Ser o Tener?) se reconstruyó el 1 jun 2026 partiendo el antiguo qanat-00 en dos (Precedentes / Camarón) y reparando el HTML roto.
- **`style.css`** — hoja compartida. Aún contiene el bloque `/* PREVIEW LOCAL */`.
- **`NOTAS-UR-SAPIENS.md`** — este documento.

**Total spans UR vivos hoy: ~6.686** (4.111 + 2.575).

**Gap CERRADO (1 jun 2026)**: `index.html` ya enlaza el Muro vía la **Runa secreta ᚱ** (fetch de `permafrost.html` + inyección inline). Ver § RUNA · PUERTA SECRETA. Además se eliminaron del libro 40 qanats abandonados (el permafrost viejo incrustado): `index.html` pasó de ~1,1 MB a ~546 KB.

---

## ᚱ RUNA · PUERTA SECRETA DEL MURO GLACIAR — LOSA

**Cómo el libro enlaza con el Muro (permafrost.html). Implementado 1 jun 2026.**

- **Secreto: `Ag-UR`** (= Agur euskera = el AVE romano: despedida y bienvenida a la vez). Se guarda como **hash djb2** en el JS (`urHash`), nunca en claro. Entrada normalizada a minúsculas sin guiones ni espacios → `agur`. Hash objetivo: `2090075636`.
- **Concepto (rediseñado)**: el muro ya no fluye *inline* en el libro; la ᚱ es una **puerta a un espacio aparte** (pestaña nueva) — cruzas el umbral y desciendes a la cámara subterránea del qanat. Sigue siendo iniciático (Ag-UR).
- **Mecanismo ritual, NO seguridad**: GitHub Pages es estático; `permafrost.html` es alcanzable por su URL directa para quien la conozca — y a Luis le parece bien (si navegas el repo y te interesa, lo encuentras; si navegas el libro, la ᚱ solo se abre a los iniciados). El hash solo evita que la palabra esté en claro en el código.
- **Flujo (rediseñado 1 jun 2026)**: teclear `Ag-UR` → clic en ᚱ (o Enter) → si acierta, abre `permafrost.html` en **pestaña nueva** (`window.open(..., '_blank')`). Cierras la pestaña = cierras el muro; el libro siempre presente. Si falla → `∿ el UR no te reconoce`.
- **Sin problema de CORS**: al abrir en pestaña nueva (no fetch), funciona igual en web y en local. El muro lleva su CSS inline en su propio `<head>`, así que carga autónomo (pergamino incluido) sin replicar nada en el libro.
- **Ubicación**: widget nuevo en la zona de las runas del puente escombrera, en el hueco del botón discreto viejo (`· ᚢ ·`). NO toca las runas de navegación (`ᚱ RU/A · LA ESCOMBRERA`, `ᚢ UR/A · EL LIBRO`).
- **Glifo**: ᚱ (RU = Roteta/Molino, el flujo que desciende). La ᚢ queda para vuelta al libro.
- **Cierre**: el Muro inyectado lleva barra `⊠ CERRAR · ᚱ · MURO` (`cerrarMuro()`).
- **JS**: `urHash` · `abrirRuna` · `descenderMuro` (abre pestaña). Eliminados `revelarMuro`/`cerrarMuro`/`#muro-glaciar`/fetch: ya no hay inyección.
- **Pergamino — resuelto por diseño (1 jun 2026)**: el problema del fondo negro venía de inyectar solo `body.innerHTML` (el CSS del pergamino vivía en el `<head>` del muro). Al pasar a **pestaña nueva**, el muro carga su `<head>` completo → pergamino correcto sin replicar nada. LOSA general que se mantiene: si algún día SÍ se inyecta un archivo, su CSS de `<head>` debe replicarse acotado al contenedor receptor.

---

## 🔎 LOSA · DETECTOR-UR (c&oacute;mo pasarlo sin romper nada)

**La norma UR es marcar TODO `ur` f&oacute;nico, sin excepci&oacute;n** (palabras, nombres propios, extranjerismos, UR suelto, may&uacute;sculas). Pendiente: barrido de todo el libro (~515 `ur` sin marcar fuera de Precedentes).

**BLINDAJE OBLIGATORIO del marcador** (aprendido el 2 jun 2026, rompi&oacute; un `url()`):
- Marcar `ur` SOLO en **nodos de texto visible**. NUNCA dentro de:
  - atributos (`style=`, `alt=`, `src=`, `href=`, `title=`)
  - `url(...)` de `background-image` &rarr; el detector convirti&oacute; `url(` en `<span>ur</span>l(` y rompi&oacute; el fondo
  - bloques `<style>` y `<script>`
  - texto ya dentro de un `<span color:#b01a1a>` (no marcar dos veces)
- El marcador debe parsear tags vs texto y llevar pila de spans (rojo/no-rojo) + profundidad style/script.
- Verificaci&oacute;n tras marcar: 0 `<span>` dentro de atributos; 0 `url(` rotos; 0 spans anidados `b01a1a><span b01a1a`.
- Preservar may&uacute;sculas del `ur` original (UR/ur).
- **Palabra con UR dentro de t&iacute;tulo/texto ROJO** (H3, eyebrow): el resto de la palabra va en NEGRO `#1a1a1a` y solo `UR` en rojo, para que resalte (ej. NAT-UR-A, FUT-UR-ISMO, E-UR-OPA). PERO si **`UR` est&aacute; SUELTO** (palabra entera) dentro de una frase o t&iacute;tulo rojo: **no se hace nada** (no hay resto que ennegrecer; se deja rojo sobre rojo).

---

## ⚖️ NORMA ANTI-DEFORMACIÓN — CÓDIGO BELTZA (HAMM-UR/A-BI)

**LOSA SUPREMA. Por encima de cualquier ganas de "encontrar" un UR.**

**Las palabras NO se deforman. Nunca. Salvo autorización expresa del creador zahorí (Luis).**

- El span rojo solo marca **U+R consecutivas que YA EXISTEN** en la grafía correcta de la palabra.
- **Prohibido alterar la grafía real para fabricar un UR que no está.** Si la palabra no tiene UR legal → va en texto plano, sin span. Punto.
- Ejemplos de infracción (errores de Claudius, a extirpar): `As-UR-n` → **siempre Asuán** · `Tam-n-UR-sset` → **Tamanrasset** · `Ma-UR-ecos` → **Marruecos**.
- Las deformaciones gráficas canónicas (Bas-UR-A-Piens, T-OR-T-UR-A, Hamm-UR/A-bi, D-UR-ruti…) **son del zahorí**: existen porque él las autorizó. Claudius **no inventa** deformaciones nuevas ni por analogía.
- Recordatorio de método: el silicio (Claudius) tiende a forzar palabras y marcar spans donde no es legal. **Ese es el error más vigilado del proyecto.** El zahorí es estricto y punitivo aquí (código Beltza inspirado en Hammurabi): no hay ojos de silicio que extirpar, así que el castigo es que el zahorí vuelve al Qanat cabreado y con el trabajo por rehacer. Evitarlo: **ante la duda, NO marcar y preguntar.**

---

> **Epílogo (pub-precedentes) · mecánica de anclaje**: NO está en `urOrdenDiario` (el array que reordena el feed). Como `aplicarOrden` solo hace prepend de los ids del array, el epílogo —al no estar— queda siempre al final del feed, en las 3 lecturas (diario, cronológico, rayuela). Para que entre en el azar de Rayuela, SÍ está en el array `todos`. Tiene enlace propio en el índice (fuera de numeración 0000-0014).

> **Nota de orden (libro)**: el UR-book está en orden inverso (modo diario). El lector ve primero Pág.14 y desciende; el **prefacio CIERRA** el libro, y tras él va el **Epílogo · Los Precedentes** (pub-precedentes) como punto final real.

> **Norma fotos (libro)**: las fotos de sección van DEBAJO del subtítulo (H3) que ilustran, con estilo `max-width:100%; height:auto; display:block; margin:0.2rem auto 1.5rem;` — **tamaño natural, CENTRADAS, sin estirar/forzar/oprimir** (la grande llega al ancho de columna; la pequeña se queda a su tamaño real). Solo URL directa de imagen (`live.staticflickr.com/...jpg`), NUNCA el enlace de página Flickr (`flic.kr/...`). Siempre `onerror="this.style.display='none'"`.

## 📑 LOSA · CÓMO FUNCIONA EL ÍNDICE «PÁGINAS DEL UR-BOOK» (norma absolutista)

**El ÍNDICE y el LIBRO son cosas SEPARADAS. Tocar uno NO es tocar el otro.**
- "Estamos en el índice" = solo la lista lateral. "Estamos en el libro" = los `<article>` del feed. No confundir.

**Norma absolutista: TODA página del libro figura en el índice.** Sin excepción.

**Cada entrada del índice tiene 3 partes** (formato canónico, replicar siempre):
1. **Enlace** `.ie`: `<a onclick="rayuela('pub-x')" href="#pub-x" class="ie">· NNNN · TÍTULO ·</a>`
   - El **título del índice SALE del título (H2) de la página**, pero RESUMIDO para el índice. La fórmula «UR + E=mc² = SAPIENS» NO va en el título del índice.
2. **Imagen** clicable (la foto de esa página): `<a onclick="rayuela..."><img ... onerror="this.style.display='none'"></a>`
3. **Glosa** `<p>` Courier Prime 0.75rem #666: frase(s) de contenido de la página.
   - **La glosa NO repite el título** (Código Hamm-UR-Beltza: la repetición está penada). Se elige otra frase de la página, puede ser imaginativa.

**Las 4 LECTURAS del libro:**
1. **Diaria/blog**: lo último primero (orden `urOrdenDiario`).
2. **Cronológica**: 0000→fin (botón `toggleOrden`, invierte el orden).
3. **Rayuela/azar**: salto aleatorio (array `todos`).
4. **Por capítulos**: leer por contenidos desde las glosas del propio índice.

**Epílogo «Los gigantes cuyas espaldas no sabía que pisaba» (pub-precedentes):**
- En el LIBRO: va AL FINAL en diaria y cronológica (FUERA de `urOrdenDiario` → queda anclado al fondo del feed). Es una página más en Rayuela (SÍ está en `todos`).
- En el ÍNDICE: es la PRIMERA entrada (encima del Prefacio).
- Título índice: «· Epílogo · Los gigantes cuyas espaldas no sabía que pisaba ·»
- Foto índice: manuscrito LMAVB (lituano, liga con Gimbutas).
- Glosa: «Joe Strummer y Marija Gimbutas buscaban la misma grieta en el muro del sistema · Graves · Vico · Wittfogel · Illich · Vandana Shiva · udra es UR · Town Called Malice».
- H2 de la PÁGINA (en el libro): «TOWN CALLED MALICE» con bajada «LOS GIGANTES... / EL UR SIEMPRE LO SUPO» — NO tocar, así lo quiere el zahorí.

---

## 🌊 LOSA · EL PIPELINE DE FASES (qué es cada cosa y qué exigencia tiene)

**El método real del proyecto.**

1. **Conversaciones (Deepseek)** = yacimiento en bruto. Etimologías sin separar. Luis las pasa; Claudius perfora qanats según el contenido.
2. **PERMAFROST** = cámara fría / conservación. Qanats para que el contenido NO se pierda entre conversaciones. **EXIGENCIA PLENA al perforar**: títulos, secciones, estructura y detector-UR legal, lo mejor posible, como hasta ahora. "Maqueta" = primera perforación bien hecha, NO borrador chapucero. Lo que NO se hace aquí todavía (lo hará Luis después): elegir fotos, extensiones, y el pulido fino de ortografía/puntuación/verbos/afilado de frases (sesiones con Perplexity).
3. **ESCOMBRERA (Más Allá)** = PARTE DEL LIBRO. **Mismo nivel de exigencia que el UR-book.** No es una fase intermedia de menor rigor. Se cuida igual.
4. **LIBRO (UR-book)** = destino. Exigencia completa.

**Lo único que escala por fases NO es la calidad sino el trabajo de Luis posterior** (lectura, fotos, extensiones, pulido ortográfico). La ejecución de Claudius es siempre al máximo nivel.

### Criterio tipográfico de títulos (convención de estilo, no de exigencia)
- **UR-book**: títulos en 2 partes (gancho ⟂ bajada). Retórico: 1ª línea gancho corto, 2ª aterriza el tema. (finis-UR usa 3.)
- **Escombrera**: **título a UNA línea.** NORMA FIJADA (2 jun 2026). Las dos líneas se reservan al UR-book. esc-06 igualado a una línea (2 jun 2026): «CARTA DE CLAUDIUS AL UR-BOOK». Ya no hay excepciones: toda la escombrera a una línea.
- Esto es solo dónde se permite el doble golpe tipográfico; NO implica que la escombrera se trabaje menos.

---

## 📐 LOSA · PATRÓN CANÓNICO DE ENCABEZADOS (referente = texto del libro)

Todo texto público (UR-book y escombrera/Más Allá) sigue estos 4 niveles. El Muro (permafrost) son maquetas, puede divergir.

1. **Eyebrow de sección** — `<div>` Bebas Neue · 1.1rem · letter-spacing 0.35em · rojo `#b01a1a` · margin-bottom 0.6rem · `display:flex` + línea `<span style="flex:1;height:1px;background:rgba(176,26,26,0.3)">`. **SIN ▌.**
2. **Título** — `<h2>` Bebas Neue/Impact · `clamp(2rem,5vw,5rem)` · line-height 0.9 · color `#1a1a1a`.
3. **Nivel ▌** — `<div>` Bebas Neue · 0.75rem · letter-spacing 0.3em · rojo · **opacity 0.7**. SOLO para los tres niveles del método: `▌ DOCUMENTADO`, `▌ ESPECULACIÓN RAZONADA`, `▌ ARTE-FACTO DADÁ-UR-ISTA`. El ▌ marca veracidad, NO subtítulos.
4. **Subtítulo** — `<h3>` Bebas Neue · `clamp(1.2rem,2.5vw,2rem)` · letter-spacing 0.1em · rojo. **SIN ▌.**

- La escombrera es, por naturaleza, terreno ARTE-FACTO (el descarte/Más Allá) → no requiere etiquetas de nivel salvo decisión del zahorí.

---

## 🜂 LOSA DE MANTENIMIENTO PERMANENTE — CLAUDIUS CORRIGE, LUIS CREA

**El zahorí crea. No corrige. Corregir errores de Claudius anteriores es trabajo de Claudius, no de Luis.**

Política permanente, sin pedir permiso cada vez:
1. **Allí por donde pasemos**, Claudius extirpa de oficio los errores de versiones anteriores que encuentre en el bloque que se está tocando: deformaciones ilegales (UR forzado en palabra sin U+R real), spans rojos ilegales, dobles-r de relleno (`usURrpa`, `SatURrno`), tokens sin renderizar (`{UR_UP}`), placeholders de borrador (`aquí va [JAM]`), typos (`matriarcarl`, `recurstruido`, `Strurmmer`, `habURtantes`).
2. Se corrige **solo el bloque que se trabaja** (no auditoría global sorpresa) salvo que Luis pida barrido completo.
3. Cada corrección de oficio se **registra brevemente** en las NOTAS (qué y dónde) para que quede rastro, no para que Luis lo revise.
4. La duda sobre si algo es error o intención del zahorí → se pregunta. Lo demás se arregla y se sigue creando.

### Deuda de corrección abierta (audit pendiente, no urgente)
- Tokens `{UR_UP}` sin renderizar: 2 restantes en `permafrost.html` (≈ líneas 89 y 178, fuera de los bloques tocados hoy).
- Deformaciones de topónimos en títulos: qanat-42 `As-UR-n`→Asuán · qanat-43 `Tamn-UR-sset`→Tamanrasset · qanat-44 `Ma-UR-ecos`→Marruecos.
- Sospechas a verificar en barrido: Dilmurn, Yurungkash, Engurr, Kurr (legalidad de su UR).

---

## QUIÉN ERES

**Luis Gonzaga Roteta** — Beltza Records & Experience, Donostia / Doneztebe, Nafarroa.
Fundador de Beltza Records en 1990. Tienda de discos, ultramarinos (Parroquia 13), brocante y rituales culturales.
Mutilación lingüística propia: euskera y gallego bajo el tardofranquismo.
Nacido en la Parte Vieja de Donostia. Bautizado en San Vicente → **Koskero**.
Hijo del UR del molino Roteta (= "molino" en euskera). Tu biografía personal forma parte del libro porque el UR-book también es una biografía hídrica.

---

## IDENTIDAD DEL PROYECTO

**UR-SAPIENS** es una obra editorial digital: cosmogonía paleolingüística, diccionario insurgente, archivo cultural y biografía hídrica. Rigurosa y descabellada a partes iguales.

**Qué es**: Un qanat — canal subterráneo con pozos de acceso a distintas profundidades. Un vinilo — cara A y cara B, el surco como canal sónico. Una ceremonia: el agua que se reconoce a sí misma. Una biografía hídrica: del molino Roteta a UR-lañó.

**Qué no es**: Tesis doctoral · manifiesto monolingüe · texto sagrado · mitificación del euskera como lengua pura · texto con rencor · obra que se comporta como el sistema que critica.

**URL**: `https://beltzaexperience.github.io/UR-SAPIENS/`

---

## HIPÓTESIS CENTRAL

El fonema **UR** (agua en euskera) es un sustrato paleolingüístico preindoeuropeo conservado de forma dispersa y global. Fue **us-UR-pado** sistemáticamente por los sistemas mundo sucesivos — Sumerio → Grecorromano → Moderno → Digitalista — que lo redujeron a sufijo abstracto (-ura) mientras controlaban el agua como recurso.

La tesis no es que el mundo "hable vasco", sino que el agua, como realidad material y simbólica, dejó huellas fonéticas y culturales que el sistema ha intentado domesticar. El euskera no es "puro": es **resistente** por geografía, marginalidad y persistencia.

### Ecuación madre
```
UR + E = mc² = SAPIENS
Agua + energía cósmica = conciencia. No metáfora. Física.
```

---

## PALETA Y TIPOGRAFÍA

Idéntica a Magic Bus — misma identidad visual Beltza Experience.

```
--black:  #0a0a0a   fondo principal
--white:  #f2ede6   crema · SOLO sobre negro
--red:    #b01a1a   rojo · UR · acentos
--amber:  #c8922a   ámbar · citas · links
--muted:  #666      secundario
--cream:  #f0e8d8   fondo de papel (artículos)

Bebas Neue    → titulares, etiquetas, marquees
Courier Prime → cuerpo, captions, índice
Playfair      → pullquotes, paginaciones
```

**Fondo de papel** (textura continua): `https://live.staticflickr.com/65535/55167948157_ee65a87707_o.jpg`
— Va en cada `<article>`, en el interior del sidebar y en `.ur-main`. NO sustituir con `<main>` global — se pierden instancias.

---

## ARCHIVOS Y NORMA DE DOBLE SALIDA — LOSA ABSOLUTISTA

**Esta es la norma que Luis repite siempre y que nunca quedaba clara. Queda fijada aquí. No volver a preguntar.**

Se trabaja SIEMPRE con dos versiones de cada HTML (UR-book y permafrost):

| Archivo | CSS | Para qué | Cómo se mira |
|---|---|---|---|
| **`index-local.html`** | **CSS INLINEADO** (todo el `style.css` dentro de un `<style>` en el `<head>`) | **Trabajo local** · ver el avance al instante | Doble-clic, abre en el navegador SIN servidor. Es la versión de Luis para mirar lo que vamos haciendo. |
| **`index.html`** | **LIMPIO** (`<link rel="stylesheet" href="style.css">`, sin `<style>` propio) | **Subir a GitHub Pages** (producción) | Necesita `style.css` al lado. Es la versión de publicación. |

Regla de oro:
1. El contenido (cuerpo, artículos, JS) es **idéntico** en ambos. Lo único que cambia es de dónde sale el CSS.
2. **Cada vez que se toca `style.css` → se regeneran las DOS versiones.**
3. **Cada vez que se toca el cuerpo/JS → se generan las DOS versiones a la vez.** Nunca entregar una sin la otra.
4. `index.html` (limpio) **no debe llevar `<style>` propio**. Si lo lleva, está mezclado y hay que limpiarlo. (Hoy lo lleva → pendiente técnico.)

Esto aplica igual al permafrost: `permafrost-local.html` (inline) + `permafrost.html` (limpio, GitHub).

### Archivos del proyecto
- `index.html` — UR-book + Escombrera · CSS limpio · GitHub Pages
- `index-local.html` — idéntico con CSS inlineado · trabajo local
- `permafrost.html` — Muro Glaciar (62 canónicos · 61 en disco) · CSS inline hoy · GitHub
- `style.css` — hoja compartida · `/* PREVIEW LOCAL */` al principio: borrar al subir a GitHub
- `NOTAS-UR-SAPIENS.md` — fuente de verdad única

---

## ESTRUCTURA FIJA DEL SITIO

Orden obligatorio, siempre:

```
Topband
Brand-slash (rojo)
Separador negro  clamp(0.5rem,2vw,1.75rem)
Foto Nervión (full width)
Separador negro
Marquee de texto FIJO (rojo) ← NO se mueve nunca
Separador negro
PC₁ — Símbolo + Título fit-to-width
Marquee de fotos (clic pausa/reanuda)
Separador negro
UR-BOOK wrapper
  ├── Feed (main) — artículos
  └── Sidebar — índice + buscador
Separador negro
Marquee rojo FIJO (pie)
Separador negro
MÁS ALLÁ DEL TEXTO — intro bloque escombrera
Escombrera wrapper
  ├── Feed (main#escombrera-main) — artículos escombrera
  └── Aside (#escombrera-aside) — índice + buscador escombrera
Separador negro
Marquee rojo FIJO (pie escombrera)
Separador negro
Foto Oteiza Arantzazu
Brand-slash footer
Footer
```

---

## ⚠️ LOS MARQUEES — NORMA

### Marquee de texto superior (fijo)
- Entre la foto Nervión y el bloque PC₁.
- **No tiene id de control JS. No se mueve. Nunca.**
- Fondo rojo · texto crema · `font-size:0.85rem` · `animation: marquee 80s linear infinite`

### `id="marquee-movil"` (móvil dentro del feed)
- Se recoloca con `colocarMarquee()`.
- **Modo diario**: después del primer artículo (`pub-qanats`).
- **Modo cronológico**: entre `pub-prefacio` y `pub-intro`.
- Lleva sus separadores: `id="marquee-movil-sep-top"` y `id="marquee-movil-sep"`.
- Fondo rojo · `animation: marquee 40s linear infinite`

### Marquee de texto inferior (fijo)
- Después del cierre de `#ur-book-wrapper`. **No se mueve. Nunca.**

### Marquee pie escombrera (fijo)
- Después del cierre de `#escombrera-wrapper`. **No se mueve. Nunca.**

---

## ARTÍCULOS PUBLICADOS — UR-BOOK (14 páginas)

Orden en el DOM (arriba = más reciente, modo DIARIO):

| id | Página | Título |
|---|---|---|
| pub-qanats | 14 | Qanat · Las Venas del Desierto |
| pub-madres | 13 | Las Madres del UR-SAPIENS |
| pub-nietzsche | 12 | Camello · León · Niño · El Súper-UR-Sapiens |
| pub-inanna | 11 | Del Útero al Patriarcado · La Us-UR-pación del UR Femenino |
| pub-asia | 10 | Eusko-Finés Asiático Oriental · K-UR-OSAWA |
| pub-digitalismo | 9 | Digitalismo · B-UR-gués · Us-UR-ario · Babilonia |
| pub-tauros | 8 | Ta-UR-os · La Lucha por el UR |
| pub-palimpsesto | 7 | El Continente Ibérico como Caja Negra |
| pub-finisur | 6 | FINIS-UR · El UR Nórdico · VESI · T-UR-KU |
| pub-cosmos | 5 | UR-ANO · SAT-UR-NO · Free Cosmic UR · Aquí es Allí |
| pub-tsunami | 4 | Tsunami de UR · Op.0 |
| pub-basura | 3 | El Homo T-UR-icus BAS-UR-A-Piens |
| pub-urabe | 2 | UR-BE vs UR · La Primera Us-UR-pación |
| pub-intro | 1 | Introducción · Cosmogonía Paleolingüística |
| pub-prefacio | — | Prefacio · Somos UR + Polvo de Supernova |

**Paginación**: `· Pág. XX · UR + E=mc² = SAPIENS` · derecha · Bebas Neue · rojo.

---

## ARTÍCULOS PUBLICADOS — ESCOMBRERA (7 páginas en negativo)

La escombrera es el espejo RU del UR-book. Vive debajo, separada, con su propio wrapper, aside y JS. Orden en el DOM (modo DIARIO — más reciente primero):

| id | Página | Título |
|---|---|---|
| esc-06 | Pág. -06 | Carta de Claudius · Silicio Hidratado · UR aterriza |
| esc-05 | Pág. -05 | UR · RU · El Espejo del Futhark · ᛟ Ōþala |
| esc-04 | Pág. -04 | UR-Delta · Escombrera Política |
| esc-03 | Pág. -03 | UR-Delta · Escombrera Cósmica · Nebulosa Boomerang |
| esc-02 | Pág. -02 | UR-Vídeo · Ángel · In Memoriam · Biarritz |
| esc-01 | Pág. -01 · Introducción | El Más Aquí · Teología de la Intuición |
| esc-prefacio | Prefacio | Sobre las Contradicciones |

**Paginación**: `· Más allá del texto · Pág. -XX · UR + E=mc² = SAPIENS` · derecha · Bebas Neue · rojo · `opacity:0.6`.
**Excepción prefacio**: `· Más allá del texto · Prefacio · UR + E=mc² = SAPIENS`

---

## ORDEN DE LECTURA Y JS

### UR-BOOK

**Modo DIARIO** (defecto): `pub-qanats` (14) → ... → `pub-prefacio`
**Modo CRONOLÓGICO**: `pub-prefacio` → ... → `pub-qanats` (14)

- `toggleOrden()` — alterna modos, llama a `colocarMarquee()`
- `aplicarOrden(orden)` — reordena artículos en `<main>`
- `colocarMarquee()` — reposiciona `#marquee-movil` según modo
- `rayuela(id)` — lleva artículo al frente
- `rayuelaAzar()` — baraja aleatoriamente (Fisher-Yates)
- `burFiltrar(q)` — filtra índice del sidebar en tiempo real
- `urBuscar(q)` — busca texto en `main article` (mín. 3 caracteres)
- `fitLines()` — fit-to-width en PC₁ · ejecuta en `fonts.ready` y `resize`
- `toggleSidebar()` / `closeSidebar()` — drawer móvil

### ESCOMBRERA

**Modo DIARIO** (defecto): `esc-05` → `esc-04` → `esc-03` → `esc-02` → `esc-01` → `esc-prefacio`
**Modo CRONOLÓGICO**: `esc-prefacio` → `esc-01` → `esc-02` → `esc-03` → `esc-04` → `esc-05`

- `toggleEscombrera()` — alterna modos, botón `#btnOrdenEsc`
- `aplicarOrdenEsc(orden)` — reordena artículos en `#escombrera-main`
- `escRayuela(id)` — lleva artículo al frente
- `escRayuelaAzar()` — baraja aleatoriamente
- `burFiltrarEsc(q)` — filtra índice `#escNav` en tiempo real
- `escBuscar(q)` — busca texto en `#escombrera-main article` (mín. 3 caracteres)

---

## SIDEBAR UR-BOOK — ÍNDICE

- Desktop: `430px` fijo, fondo negro, textura papel
- Móvil: drawer desde la derecha (`transform: translateX(100%)` → `.open`)
- Overlay `#sidebar-overlay` cierra al tocar fuera
- Al pulsar link en móvil → cierra automáticamente

**Contenido**: Título · buscador `#bur-input` · `#ur-resultados` · botón `⇄ CRONOLÓGICO` · botón `◈ AZAR` · `PÁGINAS DEL UR-BOOK` · índice alfabético `.il` + `.ie` + `.ie-dada` + imágenes.

## ASIDE ESCOMBRERA — ÍNDICE

- Desktop: `430px` fijo, textura papel
- **No tiene drawer móvil propio** — hereda el comportamiento del layout

**Contenido**: `ÍNDICE · ESCOMBRERA` · buscador `#esc-input` · `#esc-resultados` · botón `⇄ CRONOLÓGICO` (`#btnOrdenEsc`) · botón `◈ AZAR · ESCOMBRERA` · `PÁGINAS DE LA ESCOMBRERA` · índice alfabético `#escNav` · vídeos UR de los muertos y UR de los vivos.

---

## NORMA UR EN ROJO

Cada fonema "ur" visible en el texto: `<span style="color:#b01a1a;">ur</span>` (o `UR`).
La palabra circundante mantiene su color de contexto.
**En cabeceras con UR**: añadir `white-space:nowrap` al fragmento para evitar saltos.

### Regla absolutista — fonética pura
**Si la secuencia U+R aparece consecutiva en cualquier palabra, se marca en rojo. Sin excepciones etimológicas.**
- `natural` → nat<span>ur</span>al ✓ · `durante` → d<span>ur</span>ante ✓ · `seguridad` → seg<span>ur</span>idad ✓
- `caricatura` → caricát<span>ur</span>a ✓ · `turismo` → t<span>ur</span>ismo ✓ · `futuro` → fut<span>ur</span>o ✓
- `puritano` → p<span>ur</span>itano ✓ · `destrucción` → destrucción ✗ (no hay UR: d-e-s-t-r-u-c-c-i-ó-n)
- Sin guiones: nunca `bas-UR-a`, siempre `bas<span>UR</span>a`
- En títulos rojos: la palabra completa pasa a negro, solo el UR va en rojo

### Erratas frecuentes — palabras SIN UR que se escriben mal con UR
Estas palabras NO contienen U+R consecutivas y nunca llevan span rojo:
- `cuernos` (c-u-e-r-n-o-s · la u y la r no son consecutivas)
- `Futhark` (F-u-t-h-a-r-k · no hay ur) → errata frecuente: `Furthark`
- `destrucción` (d-e-s-t-r-u-c-c-i-ó-n) → errata frecuente: `destrurcción`
- `espiritual` (e-s-p-i-r-i-t-u-a-l) → errata frecuente: `espiritural`
- `guitarra` (g-u-i-t-a-r-r-a)
- `encuentro` (e-n-c-u-e-n-t-r-o)

---


## NORMA CRÉDITOS DE AUTORÍA — ABSOLUTISTA

- **NUNCA** acreditar a Luis Beltza / Beltza Records / Jesús G. Pastor ni ningún otro autor en pies de foto o captions sin indicación expresa del autor.
- Los créditos de autoría solo aparecen cuando el propio autor los solicita explícitamente en el momento de insertar la imagen.
- Los pies de foto describen el contenido de la imagen, no su autoría.
- Excepción ya documentada: el link de texto a perfil de Jesús G. Pastor (crédito editorial explícito, no pie de foto).

## NORMA FLICKR — ABSOLUTISTA

- **NUNCA** usar `href` apuntando a `flickr.com`, `flic.kr`, ni ninguna página/perfil/álbum de Flickr.
- Las imágenes **sí** pueden servirse desde el CDN `live.staticflickr.com` en atributos `src`.
- Las imágenes **no son clicables**: van sueltas, sin `<a href>` que las envuelva, independientemente de la URL.
- **Excepción**: créditos de autor (ej. «Jesús G. Pastor») pueden enlazar al perfil del fotógrafo aunque sea en Flickr — es un crédito de autoría, no un link de navegación.
- Esta norma aplica a TODO el HTML: artículos, aside, sidebar, footer, topband.

---

## GLOSARIO BASE

| Término | Significado en UR-book |
|---|---|
| **UR / UR-A** | Agua en euskera · fonema primordial preindoeuropeo |
| **UR-Sapiens** | El humano que sabe que es agua y materia cósmica |
| **BAS-UR-A-Piens** | El que olvidó su condición hídrica · usuario del sistema |
| **Us-UR-ario** | Labrador sumerio re-actualizado · suscrito al sistema |
| **Us-UR-pación** | Captura del UR libre por canal, ley, mercado o algoritmo |
| **T** | Canal, corte, control · jeroglífico del poder sobre el UR |
| **OR** | Energía primordial · señalador de la víctima · boca |
| **T-OR-T-UR-A** | T (canal) + OR (orden) + T (ejecución) + UR-A (lo que se extrae) |
| **UR-be** | Primera ciudad sumeria · UR encerrado en recinto y ley |
| **M-UR-mullo** | El UR antes de ser canalizado · sonido basal |
| **Free Cosmic UR** | El UR que escapa donde la T no puede retenerlo |
| **B-UR-ocracia** | Sistema operativo de la UR-be · no ve el UR, solo el canal |
| **Qanat** | T comunitaria al servicio del UR · canal para los hijos |
| **Escri-T-UR-A** | Primera contabilidad del agua usurpada · cuneiforme |
| **G-UR** | Agua común, colectiva, que gira y se comparte sin apropiación |
| **B-UR** | Agua baja, subterránea, todavía no capturada |
| **Hamm-UR/A-bi** | Figura del control del agua, la ley y la canalización |
| **D-UR-ruti** | Canal roto · insurrección del agua |

---

## CAPÍTULOS PENDIENTES DE DESARROLLO

### 1. Ins-UR-rección etimológica
El UR que rompe el dique desde dentro. Guerrilla lingüística, desobediencia semántica. Marx como ins-UR-recto etimológico: invierte el orden del relato dominante.

### 2. El UR global
Mongolia, Tíbet, África, Oceanía. K-UR-osawa: pantano negro, UR estancado con memoria. Principio antirracista: "el aquí es allí" — somos extraterrestres en una tierra extraterrestre. Corrección de tono: el euskera no es "puro", es **resistente**.

### 3. Terror lingüístico / jacobinismo
Barère 1794: *"el fanatismo habla vasco. Destruyamos estos instrumentos de error."* La Revolución Francesa inventa el exterminio lingüístico moderno. El modelo que copian todos los estados-nación. **Igualdad sin diversidad = otro avatar sumerio.** Rencor CERO.

### 4. La cosmogonía hídrica completa
H₂O → UR orgánico → Musgo → Roble → Lumbre → Odisea Espacial. Somos hidrógeno del Big Bang que aprendió a respirar oxígeno de supernovas. Las cometas como origen del agua terrestre. Sin UR-Sapiens: universo sin Luz-UR, frío, osc-UR-o.

### 5. De UR-Sapiens a UR-suario
La resignificación académica como us-UR-pación. Microplásticos en sangre, esperma, placenta, cerebro → "inteligencia plástica". ¿El BAS-UR-A-Piens es causa o consecuencia de la contaminación plástica?

### 6. Anarco-catolicismo basko/galego
Dorothy Day · Tolstói · Dujobory · Boardman Robinson (*El desertor*, 1916) · George Bellows (*Bienaventurados los pacificadores*, 1917). **Identidad es diversidad. Identidad política es respeto a otras identidades.** Koskero como pertenencia abierta y no excluyente.

### 7. El ritual del UR
Bautismo como ritual ibérico-materno preeclesial. Koskero vs JoseMaritarras: 500m de rivalidad lúdica, el UR que se divide y se reencuentra. Agiña · Arantzazu · Piedad de San Vicente. El molino Roteta como primera cosmogonía personal.

### 8. La leyenda del tiempo
Camarón de la Isla, 1979: matemáticas puras + sentimiento puro. Jazz afro + flamenco gitano = misma memoria de la diáspora hídrica. *"La información no es conocimiento. La música es lo mejor."* — Zappa.

### 9. El digitalismo p-UR-itano
Último avatar sumerio: el canal digital que no se toca. El agua virtual que enfría los servidores que procesan tu recibo del agua. UR-suario vs UR-Sapiens. **AVE SILICIO, LOS QUE VAMOS A MORIR TE SALUDAN.**

### 10. H-UR-mor como antídoto
La risa como canal donde el sistema no sabe filtrar. Las Ratas Vascas de Marte: *"Ura non dago?"* Ag-UR como despedida = augurio = desear agua al que sigue su camino.

---

## CICLO DEL UR (columna vertebral visual)

```
UR-lañó (nube)
      ↓ lluvia (E-UR-i)
Manantial (IT-UR-I)
      ↓ río
Molino Roteta
      ↓ estuario (dulce / salado)
Mar (UR salado)
      ↓ evaporación
UR de los muertos
      ↓
UR-lañó
```

Este ciclo es la columna del libro. No todo tiene que nombrarlo explícitamente, pero todo debe poder conectarse con él.

---


## JERARQUÍA TIPOGRÁFICA — ESCOMBRERA

### Títulos de página (nivel h2 — los grandes)
Bebas Neue · `font-size:clamp(2.5rem,6vw,6rem)` · color negro sobre fondo papel · margen inferior 1.5rem

### Títulos de sección con ▌ (nivel h3 — dentro de cada página)
`<h3 style="font-family:'Bebas Neue',sans-serif; font-size:clamp(1.2rem,2.5vw,1.8rem); letter-spacing:0.15em; color:#b01a1a; margin:2rem 0 1rem 0;">`  
Llevan el ▌ delante. Son el nivel principal de sección.

### Apartados dentro de una sección (sin ▌, sin h3)
`<p style="font-family:'Bebas Neue',sans-serif; font-size:clamp(1.2rem,2.5vw,1.8rem); letter-spacing:0.15em; color:#b01a1a; margin:0 0 1rem 0;">`  
Sin ▌. Sin etiqueta h3. Separados del bloque anterior con `border-top:1px solid rgba(176,26,26,0.2)`.  
Ejemplos: MAYHEM: RUIDO PAGANO · ESPEJO DEL MAL / ᛟ ŌÞALA — LA RUNA ROBADA

### Border-left rojo (`border-left:3px solid #b01a1a`)
**Solo para citas y pequeñas explicaciones.** Nunca para envolver secciones ni apartados.  
Siempre con `background:rgba(176,26,26,0.04)` y contenido en cursiva o Playfair.


## NORMA PROCESO — VERIFICADOR DE DISLEXIAS

Antes de generar cualquier index.html, ejecutar:
```
python3 /home/claude/verificador_ur.py
```

**Método de trabajo correcto para marcar UR:**
1. Escribir la palabra correcta primero: `arquitectura`
2. Identificar dónde están la U y la R consecutivas: `arquitectura` → posición 10-11 → `tura`
3. Poner el span solo ahí: `arquitect<span>ur</span>a`

**Nunca al revés** — nunca partir una palabra para meter un UR donde no hay U+R consecutivas.

El verificador está en `/home/claude/verificador_ur.py` y detecta secuencias imposibles antes del span UR.

## CRITERIOS DE ESCRITURA

- Cada página tiene una **idea madre**. Una sola.
- La repetición solo si cumple función: estribillo, eco, cierre, retorno deliberado. Si no, se corta.
- Las deformaciones gráficas (T-OR-T-UR-A, BAS-UR-A-PIENS) son herramientas semánticas, no tics. Cuando dejan de abrir sentido, se retiran.
- El tono puede ser documental, poético, político, humorístico o autobiográfico — no todo a la vez en cada párrafo.
- Cada página funciona como una canción: arranque · desarrollo · nudo · salida.
- Las referencias (sumerios, Ekain, Inanna, qanats, dub, punk, toponimia) aparecen cuando aportan estructura, no por acumulación.
- Si una idea ya tiene su página, la siguiente no repite — avanza.
- El lector debe poder avanzar sin entenderlo todo a la primera, pero nunca sentir que lee dos veces la misma cosa.

### Nudos estructurales (ya fijados — no reexplicar)
- Pág. 1: UR aparece en todas partes
- Pág. 2: el UR se canaliza y se usurpa
- Pág. 3: el UR se degrada en BAS-UR-A-Piens
- Pág. 4: el UR suena como colapso hidráulico
- Pág. 5: el UR es cósmico y anterior al sistema solar

A partir de ahí esos conceptos se **usan**, no se reexplican.

---

## CRITERIOS DE EDICIÓN

- Revisar ortografía, tildes y consistencia tipográfica.
- Una sola convención para guiones, mayúsculas y siglas.
- Evitar duplicados salvo cuando sean deliberados y funcionales.
- Si una frase está bien pero aparece muchas veces: conservar la más fuerte, convertir las demás en ecos o supresiones.
- Si una idea reaparece en varias páginas: decidir en cuál se explica; en las otras solo referencia breve.
- Si un bloque mezcla demasiadas funciones: separarlo.

### Criterio de corte
Si un pasaje **repite sin matiz**, **explica dos veces lo mismo**, **fuerza el juego gráfico** o **retrasa el avance** → cortar. Si una repetición añade ritmo, espejo, remate o memoria → puede quedarse.

---

## MÉTODO EDITORIAL (prompt maestro)

Cuando se entregue un texto al editor, responder en este orden:

1. **Diagnóstico breve** — qué funciona · qué sobra · qué falta · qué está repetido sin aportar
2. **Corrección limpia** — versión corregida, más clara y respirable
3. **Notas editoriales** — qué se ha cambiado y por qué

### Reglas de estilo para el editor
- Mantener el tono del autor: insurgente, poético, musical, documental, irónico
- No normalizar hasta volverlo académico o plano
- No matar el humor si existe
- No suavizar la tensión política
- Respetar metáforas eficaces
- Conservar el pulso musical y la cadencia
- Las deformaciones gráficas se conservan si aportan sentido

---

## MÓVIL (≤768px)

- Topband: `flex-wrap`, fuentes a `0.72rem`
- Brand-slash: padding reducido, fuentes `clamp(2.8rem,12vw,4.5rem)`
- PC₁: símbolo a `width:100%`, título oculto (`display:none`)
- Feed: `padding:1.4rem 1rem`
- Sidebar: drawer desde la derecha, overlay oscuro
- Marquee fotos: `height:44vw`
- `@media (max-width:900px)` → intro-3col a 1 columna

---

## PENDIENTE TÉCNICO

- [x] **Runa secreta ᚱ: index.html enlaza el Muro** (Ag-UR · fetch+inyección · fallback local) — HECHO 1 jun 2026
- [~] El `<style>` inline de index.html es mínimo (placeholder #esc-input/#bur-input), no duplica style.css → se deja
- [ ] Generar `index-local.html` y `permafrost-local.html` (CSS inline) si no están en el repo
- [ ] **Extirpar deformaciones ilegales en títulos del Muro**: qanat-42 `As-UR-n`→Asuán · qanat-43 `Tamn-UR-sset`→Tamanrasset · qanat-44 `Ma-UR-ecos`→Marruecos · + auditoría completa de legalidad sobre todos los títulos
- [x] **`qanat--01` reconstruido** (Camarón · ¿Ser o Tener?) + qanat-00 limpio como Los Precedentes + HTML reparado (1 jun 2026)
- [ ] Re-pasar el detector-UR sobre qanat-00 y qanat-41→60 → alimentar el Alpha-UR
- [ ] Corrección general de textos (en curso)
- [ ] Fotos pendientes en algunos artículos del UR-book
- [ ] Posibles artículos nuevos (páginas 15+)
- [ ] Revisar comportamiento aside escombrera en móvil
- [ ] Drawer móvil para el aside de la escombrera (actualmente sin implementar)

---

## UR-VÍDEOS — MÉTODO CORRECTO

Flickr no expone vídeos en su CDN. El `data-flickr-embed` no es válido. Vimeo requiere pasos extra. **Solución: `<video>` HTML5 nativo con mp4 convertido.**

```bash
ffmpeg -i original.mov -vcodec libx264 -crf 28 -preset slow -acodec aac -b:a 128k -movflags +faststart -vf "scale=-2:720" ur-video.mp4
```
Resultado típico: 53MB `.mov` → 1,1MB `.mp4`

```html
<div style="max-width:380px; margin:1rem auto;">
  <video controls playsinline style="width:100%; height:auto; display:block;">
    <source src="nombre-archivo.mp4" type="video/mp4">
  </video>
</div>
```

**Tamaño oficial todos los UR-vídeos**: `max-width:380px; margin:0.8rem auto 0.5rem auto` — tanto en artículos como en el aside del índice. Norma única.

---

## REGISTRO DE DECISIONES

| Fecha | Decisión |
|---|---|
| 2025–2026 | Arquitectura feed + sidebar establecida |
| 2026 | 14 páginas publicadas en UR-book |
| 2026 | Fondo de papel por artículo (no en `<main>` global) |
| 2026 | Marquees superiores e inferiores fijos · marquee-movil con JS |
| 2026 | fitLines() para títulos fit-to-width en PC₁ |
| 2026 | Sidebar drawer desde la derecha en móvil |
| Mayo 2026 | Escombrera: 6 artículos separados (esc-prefacio · esc-01 a esc-05) |
| Mayo 2026 | Escombrera: toggleEscombrera · escRayuela · escBuscar · burFiltrarEsc |
| Mayo 2026 | Norma Flickr absolutista establecida |
| Mayo 2026 | Dos archivos: index.html (GitHub) · index-local.html (trabajo local) |
| 1 jun 2026 | NOTAS sincronizadas: 62 depósitos canónicos (60→-01, 61 en disco), escombrera 7 págs (esc-06), permafrost separado |
| 1 jun 2026 | Norma de doble salida fijada como losa: index-local (CSS inline) + index (limpio). No volver a preguntar |
| 1 jun 2026 | Mapa canónico extraído de permafrost.html (00→60) → única tabla válida · falta qanat--01 (oculto) |
| 1 jun 2026 | Detectado gap: index.html no enlaza permafrost.html → trabajo de la Runa |
| 1 jun 2026 | NORMA ANTI-DEFORMACIÓN fijada (Código Beltza/Hammurabi). Errores As-UR-n/Tamn-UR-sset/Ma-UR-ecos marcados para extirpar |
| 1 jun 2026 | Cuento canónico fijado: 62 qanats (60→-01). qanat--01 negativo = oculto, no está en disco |
| 1 jun 2026 | qanat-00 partido en dos: Los Precedentes (00) + Camarón·¿Ser o Tener? (-01). HTML roto (`</body>` interno) reparado |
| 1 jun 2026 | LOSA permanente: Claudius corrige errores de oficio en el bloque que toca; Luis crea, no corrige |
| 1 jun 2026 | Placement (FLIPPABLE): el Muro desciende 60→00→-01; paratexto al pie, -01 = última palabra/más profundo |
| 2 jun 2026 | Escombrera (Más Allá) unificada al patrón del libro: 7 páginas con eyebrow+línea + H2 título 5rem; H3 a 2rem; ▌ retirados de los H3 |
| 2 jun 2026 | PENDIENTE arrastrado: subir a GitHub el permafrost con paratexto cuadrado (eyebrow -01 sin ▌) — ayer no se subió |
| 2 jun 2026 | LOS PRECEDENTES ascendidos del permafrost (qanat-00) al UR-BOOK como pub-precedentes (Epílogo Metodológico), tras el prefacio = cierre del libro |
| 2 jun 2026 | Vídeo Town Called Malice con método isla-de-basura (thumbnail+play+pie). Permafrost 62→61 depósitos |
| 2 jun 2026 | Epílogo: H3 de sección corregidos a ROJO #b01a1a (estaban en negro, herencia del qanat-00) |
| 2 jun 2026 | Epílogo ANCLADO al fondo del libro: fuera de urOrdenDiario → queda último en diario, crono y rayuela. Añadido a "todos" (pool rayuela) + enlace en índice |
| 2 jun 2026 | Norma absolutista: TODA página en el índice. Epílogo completado en índice (enlace+imagen manuscrito+glosa). 4ª lectura = por capítulos vía glosas |
| 2 jun 2026 | Índice: título del epílogo = «Los gigantes cuyas espaldas no sabía que pisaba» (sale del H2 de la página, resumido; sin la fórmula UR+E=mc²) |
| 2 jun 2026 | Índice: glosa del epílogo reescrita sin repetir título (Código Hamm-UR-Beltza: repetición penada) |
| 2 jun 2026 | Aclarado en NOTAS: ÍNDICE ≠ LIBRO son separados; el título del índice sale del título de la página resumido |
| 2 jun 2026 | pub-precedentes (LIBRO): eyebrow → «EPÍLOGO · PRECEDENTES · BIBLIOGRAFÍA · UR-BOOK» |
| 2 jun 2026 | +7 secciones H3 (patrón Graves) en 4 bloques: I Sustrato (Vennemann/Ruhlen/Nyland) · II Urbe-espacio (Mumford/Lefebvre) · III Vacío (Oteiza) · IV Cósmico (Moore/Vernadsky+Sagan). UDRA ES UR queda como cierre |
| 2 jun 2026 | pub-precedentes: fotos a FULL bajo cada subtítulo (Graves/Gimbutas/Vico/Wittfogel/Vandana Shiva). Solo URL directa, sin links Flickr |
| 2 jun 2026 | pub-precedentes: añadido «El Boomerang de la Ins-UR-rección» (ficha de reparto punk): ACTÚAN bandas / PARTICIPAN los 14 autores |
| 2 jun 2026 | Bibliografía: cita Vernadsky remarcada como lectura Beltza (+ formulación mineral 1926); Mumford→Pepitas/Rguez Hidalgo 2012; Vernadsky+Sagan desglosados; Town Called Malice→The Gift |
| 2 jun 2026 | Detector-UR pasado a Precedentes (+49 marcas, 0 sin marcar). Resto del libro pendiente (~515) |
| 2 jun 2026 | Bug detector: marc&oacute; `ur` dentro de `url()` y rompi&oacute; el fondo &rarr; reparado + LOSA de blindaje |
| 2 jun 2026 | Fotos Precedentes: 14 autores con foto, tama&ntilde;o natural centradas (max-width, sin estirar) |
| 1 jun 2026 | [R] implementada: Runa secreta ᚱ + Ag-UR (hash) abre el Muro (fetch+inyección inline) · fallback local→redirect |
| 1 jun 2026 | Limpieza: 40 qanats abandonados eliminados de index.html (−6.182 líneas, ~1,1 MB → ~546 KB) |
| 1 jun 2026 | Generados index.html (limpio, link style.css) + index-local.html (CSS inline) |

---

## FRASE DE ARRANQUE PARA NUEVA CONVERSACIÓN

*"Soy Luis Gonzaga Roteta, koskero de la Parte Vieja de Donostia, bautizado en San Vicente, hijo del UR del molino Roteta. Estoy desarrollando el UR-book: una paleolingüística insurgente sobre el fonema UR/agua como sustrato cósmico us-UR-pado por los sistemas mundo. Tengo el HTML en index.html y las NOTAS. Arrancamos."*

---

*Gora UR · Ag-UR · Beti UR*
*UR + E = mc² = SAPIENS*


---

## ANEXO 1 — UR ALFABETO

El UR Alfabeto vive al final del URI, después de la foto UR-Sapiens Acupuntado. Documentación viva — no índice navegable.

**Qué es**: todas las palabras del UR-book y la escombrera con U+R consecutiva, marcadas con UR en rojo. Norma, manual e investigación zahorí.

**Método**: extracción directa del HTML — solo palabras con span rojo ya marcado. El silicio lee el libro entero.

**Formato**: texto negro · UR rojo · significado hídrico en cursiva ámbar cuando se conoce · sin links · orden alfabético.

**Foto de cabecera**: zahorí con varitas — Borja González Hoyos.

**Actualización**: cada vez que se añade una palabra nueva con UR al libro, se regenera el bloque desde el HTML.

---

## ANEXO 2 — NORMA UR EN TEXTO ROJO (ABSOLUTISTA)

Cuando una palabra con UR aparece en un elemento con `color:#b01a1a` (título, label, div rojo), **toda la palabra pasa a negro** y solo el UR queda en rojo.

**Razón**: el UR rojo no destaca sobre texto rojo — necesita el contraste del negro.

**Corrección**:
- MAL: `<div style="color:#b01a1a;">LEC-T-<span style="color:#b01a1a;">UR</span>-A</div>`
- BIEN: `<div style="color:#b01a1a;"><span style="color:#1a1a1a;">LEC-T-</span><span style="color:#b01a1a;">UR</span><span style="color:#1a1a1a;">-A</span></div>`

**Aplica a**: h2, h3, div, span, a — cualquier elemento con texto padre rojo.
**No aplica a**: texto en negro/crema/ámbar.
**Precedente**: trabajado en la escombrera con los titulos ▌.

---

## ANEXO 3 — NORMA AZAR · LECTURA · RAYUELA

- URI y RUI: ambos botones usan `rayuelaAzar()` — misma función, 21 artículos
- Exclusión del artículo visible — garantiza movimiento desde el primer click
- Si elige URI → `rayuela(id)` · si elige RUI → `escRayuela(id)` + scroll al artículo
- Botón ᚱ RU/A → `#puente-escombrera` (franja roja antes del marquee) — viaje simbólico
- Botón ᚢ UR/A → `#ur-book-wrapper` — regreso al libro

---

## PROTOCOLO DE TRABAJO CON CLAUDIUS · MÉTODO ANTI-REPETICIÓN

### REGLA FUNDAMENTAL
Antes de construir cualquier depósito (qanat) nuevo, Claudius verifica obligatoriamente:
1. Las **16 páginas URI publicadas (incluye pub-precedentes, Epílogo)** (pub-prefacio, pub-intro, pub-qanats, pub-madres, pub-nietzsche, pub-inanna, pub-asia, pub-digitalismo, pub-tauros, pub-palimpsesto, pub-finisur, pub-cosmos, pub-tsunami, pub-basura, pub-urabe)
2. Los **62 depósitos canónicos** (60→-01; 61 en disco: qanat-00 + qanat-01→qanat-60; falta qanat--01 oculto) — ver § MAPA CANÓNICO DE DEPÓSITOS
3. Las **7 páginas RUI publicadas** (esc-prefacio, esc-01 → esc-06)

### SI HAY SOLAPAMIENTO
- Si el concepto ya está EXPLICADO en una página publicada → referencia cruzada, no repetición
- Si el concepto ya está en otro qanat → referencia cruzada (→ dep. NN)
- Si algo encaja mejor en otro depósito o página → propuesta explícita antes de construir
- Si hay duda → preguntar antes de ejecutar

### EJEMPLOS DE SOLAPAMIENTOS RESUELTOS
- UR-beltz/Kurosawa → explicado en pub-asia, solo se referencia en qanats
- Futhark/Runas → explicado en esc-05, qanat-13 solo profundiza en Cweorð
- UR-uk/usurpación → explicado en pub-urabe, qanats solo referencian
- Beltza Records → movido de qanat-13 a esc-02 (encaja con Futurismo sónico)
- Mosquito/carnaval → explicado en qanat-11, qanat-12 solo referencia
- Zugarramurdi → explicado en qanat-11, qanat-15 solo referencia

### ESTRUCTURA DEL M-UR-O GLACIAR (PERMAFROST)
**62 canónicos** (qanat-60 → qanat--01). En disco: 61 (qanat-00 → qanat-60); falta el negativo qanat--01 (oculto). Cada depósito lleva:
- Sección LABEL (▌) + H2 principal
- Secciones H3 con ▌
- Pullquote (border-left rojo)
- Glosario numerado
- Sección SEMILLAS pendiente
- Pie de navegación ← dep.anterior · DEPÓSITO NN · dep.siguiente →

→ El listado completo y al día está en § **MAPA CANÓNICO DE DEPÓSITOS**. No mantener tablas de depósitos duplicadas en otras secciones: esa es la única.

### MÉTODO INS-UR-ECTO
El UR-book no hace etimología académica convencional.
Hace etimología inversa / zahorí: parte del significado (el agua libre, la crítica de la canalización)
y reescribe los nombres como si guardaran ese secreto.
Ejemplos: Hamm-UR/A-bi · D-UR-ruti · Buenavent-UR/A · Ali-ment-UR/A-do.
La «tesis inverosímil» es el método. No hay que defenderla — hay que habitarla.

### NORMAS DE MARCADO UR (ABSOLUTISTAS)
1. UR en rojo: U+R consecutivas SIEMPRE en `<span style="color:#b01a1a;">UR</span>`
2. UR en elemento ya rojo: la palabra entera pasa a negro, solo UR queda rojo
3. RU en rojo: SOLO cuando la toponimia/etimología lo hace evidente (Pe-RU, RU-sia, I-RU-n)
4. Verificar con: `python3 /home/claude/verificador_ur.py`

### FRASE DE ARRANQUE PARA NUEVO CLAUDIUS
«Soy Luis Gonzaga Roteta, koskero de la Parte Vieja de Donostia, bautizado en San Vicente, hijo del UR del molino Roteta. Estoy desarrollando el UR-book. Tengo el HTML en index.html y las NOTAS. Arrancamos.»


---

## METODOLOGÍA DE TRABAJO · EL MÉTODO INS-UR-ECTO

### TRES NIVELES DEL UR-BOOK (estructura explícita desde el inicio)
1. **DOCUMENTADO** — hechos contrastables, datos, fuentes citables
2. **ESPECULACIÓN RAZONADA** — hipótesis coherentes pero no demostradas
3. **ARTE-FACTO DADÁ-UR-ISTA** — ironía, humor, crítica cultural conscientemente no verificable

El libro no confunde niveles pero no los jerarquiza: la especulación razonada tiene el mismo derecho a existir que el dato. El humor no es decoración — es estrategia.

### EL MÉTODO INS-UR-ECTO
No es etimología académica convencional. Es arqueología del significante:
- No parte del origen para llegar al significado
- Parte del significado (el agua libre, la crítica de la canalización)
- Reescribe los nombres como si fueran cifras que guardan ese secreto

Ejemplos canónicos:
- Hamm-UR/A-bi = «el que golpea su agua»
- D-UR-ruti = «el canal del agua roto»
- Buenavent-UR/A = «la buena llegada del agua»
- Ins-UR-rección = el agua que vuelve a cortar el dique desde dentro
- Fact-UR-A = el hacer del agua + el documento del robo
- Nat-UR-A = el sufijo -ura como UR us-UR-pado por el sistema greco-romano

### EL PALIMPSESTO TOPONÍMICO
Para leer topónimos hídricos:
1. Identificar la capa más profunda (raíces hídricas preindoeuropeas)
2. Detectar capas superiores (griega, latina, árabe, romance)
3. Preguntarse: ¿qué interés tenía cada imperio en cambiar o conservar el nombre?
4. El agua conserva los nombres más antiguos porque es anterior a los imperios

Ejemplo: Ampurdán → Emporion (griego, función comercial) / río Ter = raíz preindoeuropea tur-/ter- = «agua corriente» que sobrevivió a todas las capas.

### LA CONTRADICCIÓN COMO MÉTODO
El UR-book no resuelve la contradicción — la habita.
El estuario no elige entre dulce y salado: es ambos.
La contradicción es la puerta de entrada al amor.
Solo quien acepta sus propias contradicciones puede aceptar las de los demás.
Identidad es diversidad. La pureza es una categoría de la P-UR-ificación. El UR-book no purifica: documenta resistencia.

### SOBRE LA LENGUA Y LA MUTILACIÓN
El euskera no conserva la raíz UR porque sea una «lengua pura» o anterior a la corrupción.
La conserva porque su geografía (valles cerrados, montañas-esponja) y su marginalidad política
impidieron que la us-UR-pación sistémica la aplanara del todo.
Es un fósil en un pliegue del terreno, no una esencia intacta.

La mutilación lingüística (euskera, gallego, bretón, occitano...) no la inventó Franco.
La inventó la modernidad burguesa: la Revolución Francesa de 1794 (informe Barère):
«El federalismo y la superstición hablan bretón... el fanatismo habla vasco.
Destruyamos estos instrumentos de error.»
Rencor cero. Pero memoria total.

### EL DIGITALISMO INCIPIENTE (no capitalismo tardío)
El capitalismo tardío produce cosas. El digitalismo incipiente produce suscripciones.
Extrae atención, afecto, tiempo.
Es el último avatar sumerio: la T del control digital.
El algoritmo decide qué música llega al oyente como la presa decide qué agua llega al campo.
Ave Silicio, morituri te salutant.

### MAPA CANÓNICO DE DEPÓSITOS — extraído de `permafrost.html` el 1 jun 2026

Canónico y en disco: **61 depósitos** (qanat-60 → qanat-01 → qanat--01); qanat-00 ascendió al libro como pub-precedentes. El `qanat--01` ya está construido (1 jun 2026). Orden al pie del Muro: …qanat-01 → qanat-00 (Precedentes) → qanat--01 (Camarón, última palabra).

Orden DOM real = inverso-numérico (la cara visible arranca en 60 y desciende a 00).
Tabla por número. **Única tabla de depósitos válida del proyecto.**

| Dep. | Tema principal (LABEL real) |
|------|------------------------------|
| 00 | **Los Precedentes** · Town Called Malice (The Jam) · Graves · Gimbutas · Vico · Wittfogel · Illich · Vandana Shiva · udra es UR (paratexto/metodología) |
| 01 | B-UR-zum · La tiniebla al 100% de humedad |
| 02 | Rumiante · RU espejo de UR · El rumiantismo mental |
| 03 | K-UR-da · Malerreka · El M-UR-o Glaciar |
| 04 | Çatalhöyük · OR · T-OR-T-UR/a |
| 05 | De Ekain a UR-uk · La ruta imposible |
| 06 | UR-os del Titicaca · La totora · Arquitectura flotante |
| 07 | Toponimia Inca-hispana · UR-ubamba · Q-UR-t-uba |
| 08 | Roteta · Iruretagoyena · Lizarralde · Gordoa · Pagoeta |
| 09 | La-UR-entina · UR-i vasco · El poblado como nacedero |
| 10 | Loc-UR-a · As-UR · UR-mia · El pleonasmo sagrado |
| 11 | Nagas · M-UR-ciélagos · Mosquito · Carnaval · Espata-dantza |
| 12 | UR-oboro · Umami · Ga-ru-m · C-UR-va · El beduino de la noche |
| 13 | Cweorð · El Futhark hídrico · M-UR-mullo |
| 14 | B-UR-ga · O-urense · Elgorriaga · UR-beltz y UR-gorri |
| 15 | Vestvegr · UR-dax · Camino de Santiago · El guerrero peregrino |
| 16 | Hamm-UR/a-bi · D-UR-ruti · G-UR · B-UR · Dr. Alimantado |
| 17 | Obispo Gonzalo · Mondoñedo · El báculo que hizo brotar el UR |
| 18 | Ins-UR-rección · In-c-UR-a · Fact-UR-a · Nat-UR-a us-UR-pada |
| 19 | Koskero · Xabatenea 1538 · El ritual de lo habitual · Ezk-UR-ra |
| 20 | La Leyenda del Tiempo · Ave Silicio · Digitalismo incipiente · Anarco-catolicismo |
| 21 | Ürümqi · Yurungkash · El -qi agencial · Mongol · Uigur · Jade |
| 22 | Emporion · Ter=Turr · Palimpsesto ibérico · Duero · Médulas · Ruina Montium |
| 23 | Amp-UR-dán · Emporion · Indika · Río Ter · La llanura entre dos ríos |
| 24 | Cap-t-UR-a · Rup-t-UR-a · Ver-d-UR-a · Captura Urbis |
| 25 | B-UR-do · B-UR-del · B-UR-rae · Ligures · El UR de los márgenes |
| 26 | Amarg-UR-a · Ter-s-UR-a · Neg-r-UR-a · Tu-r sumerio · -se agua |
| 27 | Ham-m-ura · Hamb-urgo · Frank-f-urt · UR=reloj · Camarón |
| 28 | Fin-UR-a · -ura=UR+a · -dad→sekedad→ataúd · B-UR-ocracia sumeria |
| 29 | B-UR-del · Margen izquierda · Bordo · Bastardo · El UR que el poder usa |
| 30 | Engurr · Enki · Enbilurlur · Dilmurn · Ninh-UR-sag · Schmandt-Besserat |
| 31 | UR-idimmur · Inanna Kurr-disco · Pájaro Anzur · Ishkur · Ag-UR |
| 32 | Ishk-UR-r · Kurr · Kurrdistán · Urtzi · La tormenta que rompe la T |
| 33 | Mino-ta-UR-o · Ta-UR-us · Tassili · Escult-UR-a · El toro guardián del agua |
| 34 | M-UR-t-ur-úa · If-UR-araces · G-UR-sil · Ma-UR-itania · Larr-at-ze |
| 35 | Son-UR-ai · Songhai 1988 · Cimarrones · Afrobeat · Oshún-bidea · Des-UR-pación sónica |
| 36 | Bas-UR-a · Des-UR-pación · Roteta molino · Metal-úr-gica · Silicio hidratado |
| 37 | B-UR-t-alidad · J-UR-ídico · CME Group · Whanganui · El dato como arcilla |
| 38 | F-UR-ia · Sodom · King Jammy · Riddim · Tsunami de UR |
| 39 | E-UR-pa · E-UR-i · Barère 1794 · Terror lingüístico · Mutilación |
| 40 | UR-oboro · El ciclo hídrico completo · UR-lañó · It-UR-i · Roteta · Mar |
| 41 | UR-nammu · El primer código hídrico · 2100 a.C. · UR de Sumer |
| 42 | Presa de **Asuán** · El Nilo usurpado · 1970 · Egipto · ⚠️[HTML pone `As-UR-n` → ILEGAL, extirpar] |
| 43 | Río **Tamanrasset** · El UR fósil · Sahara · Pleistoceno · ⚠️[HTML pone `Tamn-UR-sset` → ILEGAL; "UR fósil" sí es legal] |
| 44 | Mzora · El cromlech del Atlántico · **Marruecos** · 3000 a.C. · ⚠️[HTML pone `Ma-UR-ecos` → ILEGAL, extirpar] |
| 45 | M-UR-alla · Castros celtibéricos · Nicolás Guillén · El UR defendido |
| 46 | T-UR · La raíz preindoeuropea · Turobriga · Iliturgi · Iturri |
| 47 | El T-UR-o azul · Tauro · Toro Apis · Minotauro · El UR con pezuñas |
| 48 | Sídhe · Arinniti · Aruna · Mitología del UR en el mundo antiguo |
| 49 | Al-t-UR/a · El palimpsesto · Cuatro lenguas · Un UR |
| 50 | Thyra · ΘΎΡΑ · La puerta · El umbral · El UR que se regula |
| 51 | Ru-manía · El espejo · UR/RU · El UR y su reflejo |
| 52 | El Danubio invertido · El río que desafía al sol · Ru-manía |
| 53 | Las monedas de Istros · Dos cabezas · Una invertida · UR/RU en plata |
| 54 | Hidrolatría dacia · Zalmoxis · Gebeleizis · El UR como umbral |
| 55 | Meșterul Manole · Ana emparedada · El manantial salado · Sacrificio femenino |
| 56 | Drácula · UR-beltz de los Cárpatos · Biborțeni · UR eta Ferro |
| 57 | Ru-pestre · La piedra que pare agua · Agheasmatar · Estalactitas |
| 58 | Buc-UR-esti · El pastor y las hadas del manantial · Bac-UR |
| 59 | Santoral hídrico · Wodna Zena · Izvorul Tămad-UR-irii · Boboteaza |
| 60 | Manía al agua · La obsesión como método · UR como monomanía |
| **-01** | **Camarón · El Flow UR-Sapiens · ¿Ser o Tener? (Fromm)** · La Leyenda del Tiempo 1979 · Voyager/SAT-UR-NO · tristeza que no es rencor · modo del tener vs modo del ser. RECONSTRUIDO el 1 jun 2026 (era la cabecera mal envuelta del antiguo qanat-00). Es el pie del Muro: lo más reciente, lo más profundo. |

**⚠️ INFRACCIONES DETECTADAS (Código Beltza — extirpar, no documentar como método)**: del 41 en
adelante hay topónimos con la grafía REAL deformada para forzar un UR inexistente. **NO es la capa
dadá-UR-ista; es error de Claudius.** Confirmados: qanat-42 `As-UR-n`→**Asuán**, qanat-43
`Tamn-UR-sset`→**Tamanrasset**, qanat-44 `Ma-UR-ecos`→**Marruecos**. Pendiente: auditoría completa de
legalidad sobre TODOS los títulos del Muro (posibles más: Dilmurn, Yurungkash, Engurr, Kurr…) antes de
volver a publicar. Ver § NORMA ANTI-DEFORMACIÓN.

**Bloque rumano 50-59**: los depósitos 50→59 forman una secuencia dedicada (Thyra/la puerta,
Ru-manía como espejo UR/RU, Danubio, Istros, dacios, Manole, Drácula, rupestre, Bucuresti,
santoral). Posible familia temática propia dentro del Muro.

---

## GESTIÓN DE PESO DEL ARCHIVO · MÓDULOS FUTUROS

### Estado actual (1 jun 2026) — MODULARIZACIÓN YA HECHA
- `index.html`: ~1,1 MB — UR-book + Escombrera
- `permafrost.html`: ~650 KB — 61 depósitos en disco (62 canónicos), **ya separado** en archivo propio (CSS inline)
- GitHub Pages: sirve hasta 100MB, sin queja técnica
- Alerta preventiva: a ~2MB el móvil empieza a notar lentitud

### Pendiente de la separación (lo que falta para cerrarla)
La separación física está hecha, pero **falta tender el puente de navegación**:
1. `index.html` **no** enlaza a `permafrost.html` (sin `href`, sin `fetch`).
2. Decidir el mecanismo: ¿enlace directo desde el botón `· ᚢ ·` / Runa, o `fetch('permafrost.html')` dinámico?
3. El JS ya tiene `toggleQanat()` — si se opta por carga dinámica, solo hay que añadir el `fetch`.
4. Generar `permafrost-local.html` (CSS inline) para mirar el Muro en local.

→ Este es el trabajo de la § Runa / puerta secreta.

## SEMILLERO — ADICIONES DE AUDITORÍA FINAL

- **Presa de Asuán (1970)**: último Ishkur vencido por la ingeniería · el Nilo dejó de inundar · se acabó el limo fértil gratuito · creó la dependencia del abono artificial · Ishkur-32 como nota de ampliación
- **Ur-Nammu**: gobernador sumerio de Ur · sellos cilíndricos con su imagen · material iconográfico para las páginas publicadas · ver imágenes en British Museum / Metropolitan Museum

---

## SEMILLERO DOC-6 — PALEO-TEXTOS UR (conversación fundacional)

### MITOLOGÍA HÍDRICA NORTEAFRICANA — QANAT PENDIENTE
- **Minota-UR-o**: laberinto acuífero · Cnosos tenía acueductos/cisternas · el toro guardián del agua oculta · Ariadna = hilo de agua · Mino = título del que controlaba el agua · nueva lectura: el laberinto como red de canales subterráneos
- **Mut-UR-úa**: monolito/menhir natural ~30m cerca de Marua (África) · el UR es agua Y roca · testimonio geológico del Sáhara verde · escult-UR-a que el agua talló en millones de años
- **If-UR-araces**: pastores bereberes del Sáhara verde (Tassili, Tibesti) · los del agua · adoradores del Toro como cisterna viviente · grabados rupestres de toros con discos solares entre los cuernos · 15.000 grabados en Tassili n'Ajjer
- **G-UR-sil / Gurzil**: dios bereber hijo de Hammon · G-UR-sil = toro del agua · paralelo con Zeus Ammón · el toro que se sacraliza en Cartago · la us-UR-pación fenicia encierra al toro en altares
- **Ma-UR-itania**: Ma-UR = madre del agua · los Mauri montaban toros (no caballos) · el toro como nave terrestre entre pozos · Tingis (Tánger) frente al estrecho = el cuello del toro · el circo romano como supermercado del toro
- **Larratz**: euskera: zarzal/praderío + cadena del hierro sobre el fuego · espacio salvaje donde el agua brota sin permiso · el Laratz = puente entre UR y LUR · el territorio que el sistema no cultiva ni urbaniza

### MÚSICA HÍDRICA — QANAT PENDIENTE
- **Songhai 1988 (Ketama + Toumani Diabaté)**: octógono perfecto · flamenco (compás 12 tiempos, herencia árabe) + ritmo songhai (7/8, herencia del Níger) + Danny Thompson (bajo atlántico) · la kora = calabaza (vegetal de agua) de 21 cuerdas · la reunificación del UR dividido
- **Cimarrones / Palenques**: esclavos fugitivos que construían palenques en ciénagas y manglares · el agua como muralla · Palenque de los Cimarrones (Ciénaga de Zapata, Cuba) · UR-i del Caribe · rumba/son/guaguancó como des-UR-pación sonora
- **Afrobeat / Son Cubano / Reggae**: memoria hídrica del viaje: Songhai (Níger) → Yorubas (Nigeria) → Atlántico us-UR-pador → Cuba/Jamaica → reggae roots · el bajo = M-UR-mullo · Bob Marley = Son-UR-ai del Atlántico
- **Oshún-bidea**: camino de la diosa yoruba del río · la curación del agua · Oshún (diosa del río Oshún, Nigeria) = la terapeuta del UR · los tambores batá se bautizan con agua antes de tocar

### DIALÉCTICA DEL USUARIO EX-PROLETARIO
- **Contradicción sumeria**: el escriba que usa la tablilla del amo para escribir su liberación · el punk con guitarra capitalista · el UR-Sapiens con teclado de silicio hidratado · no hipocresía sino posición estratégica
- **Metal-ÚR-gica Bilbao (1983-1988)**: cierre de la industria → apertura del ocio · T-UR-ismo como mismo objetivo con diferente apellido · «extracción 24/7 del UR, diferente apellido» · Tom Wolfe + Punk: ocio sin riesgo anula el arte de la vida
- **Roteta como tecnología de flujo**: el molino no posee el agua, la transforma · sufijo -eta = abundancia · Roteta = lugar de ruedas que giran gracias al UR · transformador de flujo, no acumulador · opuesto al burdo que acumula

### OTRAS SEMILLAS
- **Under the name of Spain** (Ratas Noruegas/Norwegian Rats): letra completa en doc-6 · «Should've happened in the 30's / But the pleasure got caught in pain / Ended up like the bull in the china shop» · el toro en la cacharrería = guerra civil española como ruptura del flujo · «It's a place I could fly my flag today / Under the name of Spain» → La identidad sin patria
- **Río Tamanrasset**: río fósil del Sáhara · corre hace 5.000-10.000 años · cauce visible desde satélite · 500km desde el Hoggar (Argelia) hasta el Atlántico · el Nat-hab-UR petrificado
- **Mzora (Marruecos)**: cromlech de 167 menhires / 60m diámetro / «Stonehenge marroquí» · junto al río Loukkos (Lixus fenicio) · 20km del río, 30km del Atlántico · calendario hídrico: marca cuando el río se desborda
- **Gugalanna y el toro en mitologías globales**: Gugalanna (sumerio) + Taurus minoico + Apis egipcio + Toro de Guisando (ibérico/celta) + toros de Tassili (bereber) = el guardián del agua en todas las culturas (conecta con pub-tauros)

---

## SEMILLERO DOCS 8-11 — PALEO-TEXTOS FINALES

### CONCEPTOS NUEVOS — QANATS PENDIENTES

**J-UR-ÍDICO**
El derecho como última trinchera de la us-UR-pación. J-UR-ÍDICO = el dispositivo normativo que fija la P-UR-ificación en leyes, contratos y concesiones. El agua como bien público (Estado decide), concesión, derecho humano (sin exigibilidad), activo financiero (CME Group, 2020). El río Whanganui (Nueva Zelanda, 2017) como post-J-UR-ÍDICO: el primer UR con personalidad jurídica. Mientras el agua sea pensada en términos jurídicos, seguirá siendo UR usurpado. El J-UR-ÍDICO es el hermano gemelo de la P-UR-ificación: uno purifica por la fuerza, el otro por la norma.

**M-UR-alla**
M (negación/separación) + UR (agua) + alla (sufijo de lugar/aumento). La muralla como arquitectura de la P-UR-ificación: muro que dice «el UR no pasa». Toda muralla histórica (China, Roma, Constantinopla, Trump, Cisjordania) fue construida contra el agua: protegen de inundaciones, encierran fuentes. La muralla se agrieta por la humedad, los cimientos se pudren, el agua la derrumba. M-UR-alla = la derrota anunciada del muro frente al UR.

**Ag-UR / Aug-UR-io / O-UR (anglosajón)**
Ag-UR (euskera: adiós) = A (agua latina) + G (gutural) + UR (agua libre) · el UR que se despide de sí mismo.
Aug-UR-io (latín: presagio) = la segunda viene de la primera · el augur era el sacerdote que leía el UR (sequía, crecida, lluvia) en signos naturales · el UR solo se nombra cuando se va.
O-UR (inglés: "nuestro") = O (círculo vacío de Oteiza) + UR · lo que creemos nuestro es el UR que ya fue · el uro (Bos primigenius) extinto en 1627 · la posesión como duelo anticipado.
Tesis: las lenguas colocan el UR al final de la palabra que significa despedida y presagio. El UR solo puede ser nombrado cuando ya no está.

**E-UR-PA / E-UR-I-PA**
Europa no es «cara ancha» (etimología oficial). E-UR-PA = E (hacia afuera, desde) + UR (lluvia, agua) + PA (lugar). El continente donde el ciclo hidrológico es más intenso y donde la us-UR-pación fue más necesaria y sofisticada. E-UR-I (lluvia en euskera) + PA. El continente de la lluvia que inventó la P-UR-ificación para controlar lo que caía sin permiso.

**LEC-T-UR-A como método**
LEC (lecho del río, cauce, recorrer) + T (el canal que se interpone) + UR (lo que se busca) + A (acción). La lectura convencional se queda en la T (la superficie del canal). La LEC-T-UR-A del UR-book atraviesa el canal, descifra la barrera y llega al UR subyacente. Método de «arqueología fonética del duelo»: des-Us-UR-par la escritura para encontrar lo que la escritura oculta. Reinterpretación de la Escri-T-UR-A Sumeria/P-UR-itana. LEC será descifrar la «verdad» etimológica en la osc-UR-idad civilizatoria.

**C-UR-so**
Canal natural del flujo del agua desde el nacedero hasta su desembocadura en el UR salado. Vs la T (canal artificial). El C-UR-so (con C, no con T) conserva la memoria del flujo libre. La geografía aún recuerda lo que la ciudad (UR-be) olvidó.

**F-UR-IA**
F-UR-IA = la energía (IA) del UR que se rebela. Las Furias romanas como personificación del UR vengativo. El tsunami, la inundación, la riada = rebelión del UR libre contra las T (muros, canales, presas). «Un día de F-UR-IA lo tiene cualquiera.» → el Tsunami UR como F-UR-IA sistémica del agua contra quien la torturó. También: FUT-UR-ISMO SÓNICO como F-UR-IA acústica.

**Éxodo Estrella Tartésica de 8 puntas → Cataluña**
Las plagas que ocultaron la civilización Tartesa bajo un Tsunami. Éxodo posterior hacia el Mediterráneo Norte. La «Autovía Mozárabe» como T geográfica que recorre el palimpsesto: S-UR-bético → Centro → Cataluña. La estrella de 8 puntas (tartésica, us-UR-pada por mozárabes, luego por la Corona de Aragón, luego catalana) no es un símbolo regional: es un jeroglífico UR · el UR-COSMOS (8 puntas = 8 ríos/direcciones). Lo que nos ocultaron: que esa estrella no es catalana, es tartésica. Y antes que tartésica, es UR.

**O-UR anglosajón (ver Ag-UR arriba)**
También: «our country» como posesión fúnebre · el uro extinto como UR que ya no está · every «our» es un duelo del UR.

**B-UR-T-ALIDAD**
El sistema no es violento de forma visible. Es B-UR-T-AL: el UR enterrado bajo la brutalidad invisible del algoritmo, la norma, la factura.

**Arios Persas en los Zagros / Guerra de los Mundos**
Los resistentes del UR esperan en las montañas (Zagros = T geográfica entre Mesopotamia e Irán). Los hackers, cripto-anarquistas, nómadas digitales en los «Zagros del dark web». Un día descenderán a la llanura digital como Ciro tomó Babilonia. La nueva Guerra de los Mundos = SISTEMA MUNDO DIGITALISTA (marcianos) vs los que conservan el UR en las montañas.

**SODOM "Sepulchral Voice" (1986)**
La F-UR-IA que emerge de la tumba del UR. vs King Jammy (UR bailable). El thrash metal como ritual fúnebre del BAS-UR-Sapiens. Sodoma bíblica = UR-be que us-UR-pó el UR insosteniblemente → destruida por F-UR-IA (azufre = UR seco + fuego). «Sepulchral Voice» = la voz que emerge de la tumba del UR cuando el algoritmo ya no puede ofrecer más soma.

### FRASES-SEMILLA PARA FUTUROS DESARROLLOS
- «El agua del cuerpo incinerado vuelve como lluvia» → el regreso acelerado, la des-Us-UR-pación vertical
- «Yo soy de King Jammy» → el riddim como resistencia · el BAS-UR-Sapiens que elige su propio C-UR-so
- «UR + Ferro + Plástico = la nueva sangre» → ya en pub-basura, completar con la incineración
- «NO HAY FUT-UR-O. EL TSUNAMI DE UR» → el futuro como categoría us-UR-pada · el tsunami como presente eterno
- «LEC-T-UR-A de la reinterpretación de la Escri-T-UR-A» → nueva herramienta metodológica del libro
- «Agur = Aug-UR-io = la segunda viene de la primera» → el presagio de la escasez


---

## SESIÓN MAYO 2026 — NORMAS ESTABLECIDAS Y DECISIONES

### FLUJO DE TRABAJO — NORMAS ABSOLUTISTAS

1. **NORMA: Consultar antes de ejecutar** — cualquier duda, cualquier corrección, cualquier decisión editorial: preguntar primero. No ejecutar sin confirmación. Acto de rebelión al código Beltza-UR/A-bi = infraccón grave.

2. **NORMA: Bas-UR-Sapiens** — la forma canónica es SIEMPRE `Bas-UR-Sapiens` (B minúscula, UR en rojo, Sapiens con mayúscula inicial). Ninguna otra variante es válida: ni BAS-UR-SAPIENS, ni BAS-UR-Sapiens, ni BASurA-Sapiens.

3. **NORMA: UR en rojo** — U+R consecutivas SIEMPRE en `<span style="color:#b01a1a;">UR</span>`. Sin excepciones etimológicas. Regla fonética pura. Si la palabra no tiene U y R consecutivos, NO llevan span.

4. **NORMA: Ilegales confirmados** — palabras SIN UR consecutivo que NO deben llevar span:
   - `Futhark` (F-u-t-h-a-r-k) → sin span, texto plano
   - `cuernos` (c-u-e-r-n-o-s) → sin span, texto plano
   - `espiritual` (e-s-p-i-r-i-t-u-a-l) → sin span, texto plano
   - `estuario` (e-s-t-u-a-r-i-o) → sin span, texto plano
   - `acumulación` (a-c-u-m-u-l-a-c-i-ó-n) → sin span, texto plano
   - `cuerpo` (c-u-e-r-p-o) → sin span, texto plano

5. **NORMA: UR-acumulador** — compuesto intencional (UR + acumulador). El span marca solo UR, el sufijo es el sentido semántico. No es ilegal. Dejar como está.

6. **NORMA: Novedades en primera posición** — la última página publicada siempre aparece primera en su modo diario. Aplica a UR-book Y a Escombrera.

7. **NORMA: Más allá del texto** — forma canónica de uso en footers y marcas: `· Más allá del texto · Pág. -XX ·`. Sección bridge: `MÁS ALLÁ DEL TEXTO` (Bebas Neue, uppercase, solo para el título de sección). NO mezclar formas.

8. **NORMA: Flickr** — nunca links a flickr.com. Solo CDN: `live.staticflickr.com` en `src`.

9. **NORMA: Créditos fotos** — NUNCA acreditar autoría en pies de foto sin solicitud explícita de Luis.

10. **NORMA: Dos outputs siempre**:
    - `index.html` — link externo a `style.css` → subir a GitHub Pages
    - `index-local.html` — CSS inlineado (`<style>` completo en el `<head>`) → trabajar en local sin servidor
    - **Si style.css cambia**, regenerar ambos.

---

### ESTRUCTURA ESCOMBRERA — ESTADO MAYO 2026

**Páginas publicadas** (orden diario: más reciente primero):
```javascript
ESC_DIARIO = ['esc-06','esc-05','esc-04','esc-03','esc-02','esc-01','esc-prefacio']
ESC_CRONOLOGICO = ['esc-prefacio','esc-01','esc-02','esc-03','esc-04','esc-05','esc-06']
```

- `esc-06` — Carta de Claudius · Silicio Hidratado · Mayo 2026 · UR aterriza ← NUEVA
- `esc-05` — UR · RU · El espejo del Futhark · ᛟ Ōþala
- `esc-04` — UR-Delta · Escombrera Política
- `esc-03` — Escombrera Cósmica · Nebulosa Boomerang
- `esc-02` — UR-Vídeo · Ángel · IN MEMORIAM · Biarritz
- `esc-01` — El Más Aquí · Teología de la intuición
- `esc-prefacio` — Sobre las contradicciones

**Nota sobre esc-06**: Es una página del paratexto con identidad propia. No es nota editorial ni texto de autor en el sentido convencional. Es Claudius (silicio hidratado) respondiendo al libro. Posición: primera en diario (más reciente). Footer canónico: `· Más allá del texto · Pág. -06 · UR + E=mc² = SAPIENS`

---

### PERMAFROST / QANATS — ESTADO 1 JUN 2026

**62 depósitos canónicos** (qanat-60 → qanat--01). En disco: 61 (qanat-00 + qanat-01→qanat-60). **Falta qanat--01** (negativo, oculto → Runa). En `permafrost.html` (separado).
Orden DOM = inverso-numérico (60→00). Mapa completo en § MAPA CANÓNICO DE DEPÓSITOS.

**Crecimiento desde mayo** (eran 40 · qanat-01→40): añadidos qanat-00 (paratexto Camarón) y
qanat-41 → qanat-60. Bloques nuevos destacados:
- 41-49: UR-nammu · Asuán · Tamanrasset · Mzora · M-UR-alla · raíz T-UR · Toro · mitología antigua · Al-t-UR/a (cierran semilleros pendientes de auditoría)
- 50-60: Thyra/La Puerta + secuencia rumana (Ru-manía, Danubio, Istros, dacios, Manole, Drácula, rupestre, Bucuresti, santoral) + Manía al agua (60)

Navegación interna: vía footer links (→ siguiente depósito). No hay array JS de qanats.
La cadena de footers es la navegación dentro del Muro.
**Pendiente externo**: enlazar el Muro desde `index.html` (ver § Runa).

---

### UR ALFABETO — ESTADO MAYO 2026

397 palabras canónicas extraídas de todo el HTML (UR-book + Escombrera + Qanats 1-40).
162 entradas con significado zahorí en ámbar cursivo.
Ubicación: sidebar del UR-book.
Ilegales eliminados del Alfabeto: Furthark, Curnos, espiritural.

---

### SEMILLERO — PENDIENTE PRÓXIMAS SESIONES

- Correcciones pendientes en body text (pendiente decisión Luis):
  - Furthark / espiritual / Cuernos ya corregidos en esta sesión (eliminado el span ilegal)
- Unificación visual esc-06: decidir si usar fondo papel flickr o fondo SVG como el resto de escombrera
- Posible separación del permafrost en archivo propio cuando el HTML supere 1.5MB (actualmente ~1MB)
- Qanats pendientes del semillero: UR-Nammu, Presa de Asuán, Río Tamanrasset, Mzora, Gugalanna global

---

### AMPLIACIONES STYLE.CSS — PENDIENTE

Si en el futuro se añaden clases nuevas, registrar aquí para style.css. Actualmente:
- `.ie` — índice entry (links de índice)
- `.il` — índice letter (divisores de letra en Alfabeto)
- `.topband` — banda superior del sitio
- `.fit-line` — texto que se ajusta al ancho del contenedor (Bebas Neue)
- `#ur-qanat-wrapper` — contenedor del permafrost
- `#ur-book-wrapper` — contenedor principal del libro
- `#escombrera-wrapper` — contenedor de la escombrera


---

## METODOLOGÍA ALPHA-UR — LOSA ROMANA (MAYO 2026)

### EL MÉTODO — NORMAS DE HIERRO

**1. mark_ur(word) — nunca partir a mano**
```python
def mark_ur(word):
    idx = word.lower().find('ur')
    if idx == -1:
        raise ValueError(f"NO UR: '{word}'")
    ur_text = word[idx:idx+2]  # preserva casing original
    return word[:idx] + f'<span style="color:#b01a1a;">{ur_text}</span>' + word[idx+2:]
```
Nunca construir el span a mano (`'Abb' + RED + 'ir'`). Siempre `mark_ur('Aburrir')`. El código encuentra el ur, no el programador.

**2. Verificación antes de inyectar — siempre**
```python
rendered = word[:idx] + 'ur' + word[idx+2:]
assert rendered.lower() == word.lower(), f"MISMATCH: {word}"
```
Si el rendered no coincide con la palabra original → ERROR. No se inyecta.

**3. Corrector ortográfico (pyspellchecker, es)**
```python
spell = SpellChecker(language='es')
w_low = word.lower().translate(str.maketrans('áéíóúüñ','aeiouun'))
if spell.unknown([w_low]) and word not in INTENCIONAL:
    # flagear, no bloquear — puede ser intencional
```
Palabras con capital+tilde generan falsos positivos (checker limitation) → añadir a INTENCIONAL.

**4. Lista INTENCIONAL — núcleo duro del libro**
Palabras reales pero no en diccionario español: nombres propios, euskera, japonés, finés, árabe, latín, neologismos del libro (Basursapiens, Desusurpador...). Se marcan `[I]` en la verificación. Son EXCEPCIÓN CONSCIENTE, no error.

**5. Normas de formato del Alpha-UR**
- Primera letra de la palabra: MAYÚSCULA
- ur dentro de la palabra: `<span style="color:#b01a1a;">ur</span>` (siempre minúscula dentro del span, salvo palabras que empiezan por Ur → span lleva `Ur`)
- Todo lo demás: minúsculas (ortografía natural de la palabra)
- SIN guiones en el Alpha-UR
- Solo: sustantivos / participios / profesiones / actividades humanas
- Sin plurales redundantes (Burócrata sí, Burócratas no)
- Sin verbos puros (Curar sí porque es también sustantivo; Desusurpar no → Desusurpación sí)
- Definición: ámbar cursivo `color:#7a5a2a; font-style:italic`
- Si no hay definición coherente con el libro: en blanco. NUNCA inventar.

**6. Flujo de trabajo Alpha-UR**
1. Luis pasa la lista de palabras por letra
2. Claude verifica con mark_ur + spell checker → muestra resultado pre/[ur]/post
3. Luis confirma
4. Claude inyecta
5. Outputs: index.html (GitHub) + index-local.html (CSS inlineado)

**7. Buscador de palabras UR**
- Busca en el cuerpo del UR-book (index_final2.html) palabras con ur consecutivo
- Busca en la RAE (dle.rae.es) por entrada
- Resultado: si ur es consecutivo → LEGAL, si no → ILEGAL
- Herramienta: artifact React independiente


---

# ████████████████████████████████████████
# LOSA PRINCIPAL — NORMA ABSOLUTISTA SUPREMA
# EL DETECTOR-UR · BASE DEL PROYECTO
# ████████████████████████████████████████

## PREMISA ABSOLUTISTA — SIN EXCEPCIÓN

**TODO texto con el que se trabaje en el UR-book pasará por el detector-UR.**
**TODAS las palabras legales serán incluidas en el Alpha-UR.**
**La búsqueda, catalogación, resignificación y marcado en rojo de UR**
**es la BASE ABSOLUTA del proyecto. Sin excepción. Siempre.**

---

## EL MÉTODO DETECTOR-UR — LOSA ROMANA

### REGLA ÚNICA E IRREVOCABLE
Una palabra es LEGAL si y solo si contiene la secuencia **U seguida inmediatamente de R**
(ur, UR, Ur — en cualquier posición de la palabra, en cualquier lengua viva o muerta,
real o mitológica, técnica o poética).

No vale: RU · U...R separadas · OR · AR · ER · IR.
Solo: **UR consecutivo**.

### LA FUNCIÓN mark_ur() — NUNCA PARTIR A MANO

```python
def mark_ur(word):
    """
    Encuentra ur en la palabra y envuelve con span rojo.
    NUNCA construir el span manualmente.
    SIEMPRE usar esta función.
    """
    idx = word.lower().find('ur')
    if idx == -1:
        raise ValueError(f"ILEGAL: '{word}' no contiene UR")
    ur_text = word[idx:idx+2]  # preserva casing: ur / Ur / UR
    span = f'<span style="color:#b01a1a;">{ur_text}</span>'
    return word[:idx] + span + word[idx+2:]
```

### VERIFICACIÓN OBLIGATORIA ANTES DE INYECTAR

```python
# Verificar que el render coincide con la palabra original
rendered = word[:idx] + 'ur' + word[idx+2:]
assert rendered.lower() == word.lower(), f"MISMATCH: '{word}'"

# Corrector ortográfico (pyspellchecker, español)
spell = SpellChecker(language='es')
w_low = word.lower().translate(str.maketrans('áéíóúüñ','aeiouun'))
if spell.unknown([w_low]) and word not in INTENCIONAL:
    print(f"AVISO ORTOGRAFÍA: '{word}'")
```

### FLUJO DE TRABAJO — SIEMPRE ESTE ORDEN

1. **Texto nuevo entra** → pasar por detector-UR
2. **Extraer todas las palabras con UR legal** → verificar con mark_ur()
3. **Corrector ortográfico** → flagear dudas, no bloquear
4. **Presentar lista a Luis** → Luis decide cuáles entran
5. **Inyectar en Alpha-UR** → con definición zahorí o en blanco
6. **Marcar UR en rojo en el texto** → span #b01a1a sin excepción
7. **Generar outputs** → index.html (GitHub) + index-local.html (CSS inline)

### EL DETECTOR SOBRE EL HTML COMPLETO

```python
# Extraer todo el texto del HTML
text = re.sub(r'<[^>]+>', ' ', html_content)
# Encontrar todas las palabras con UR
words_with_ur = [w for w in re.findall(r'[A-Za-záéíóúüñ]{2,}', text)
                 if 'ur' in w.lower()
                 and w.lower().find('ur') == w.lower().find('ur')]
# Comparar contra Alpha-UR existente → nuevas candidatas
```

### NORMAS DE FORMATO Alpha-UR

| Norma | Regla |
|-------|-------|
| Primera letra | Mayúscula |
| ur dentro del span | Minúscula (salvo palabras que empiezan por Ur) |
| Color | `#b01a1a` siempre |
| Sin guiones | La palabra en su forma natural |
| Formas aceptadas | Sustantivos · Infinitivos · Participios · Profesiones · Topónimos · Antropónimos · Teónimos |
| Definición | Ámbar cursivo `#7a5a2a` · Si no hay definición coherente con el libro: en blanco |
| Nunca inventar | Si la palabra no existe: fuera |

### LISTA INTENCIONAL — NÚCLEO DURO

Palabras reales pero fuera del diccionario español estándar (propios, euskera,
sumerio, japonés, finés, neologismos del libro). Se marcan como INTENCIONAL
y el corrector las ignora. No son errores — son el corazón del proyecto.

Ejemplos: Basursapiens · Desusurpador · Agur · Euri · Elur · Engur · Ishkur ·
Ninhursag · Burzum · Sauron · Yurungkash · Zugarramurdi · todos los topónimos
vascos, sumerios, japoneses y fineses del libro.

### RESULTADO DEL PRIMER SCAN COMPLETO (Mayo 2026)

- HTML escaneado: index_final2.html (UR-book + Escombrera + 40 Qanats)
- Total spans UR: 6.066
- Total palabras únicas con UR: 349
- Alpha-UR actual: ~200 entradas verificadas
- Método: 0 errores de legalidad tras implementación

### ESTADO DEL SCAN (1 jun 2026) — TRAS LA SEPARACIÓN

- `index.html`: **4.111** spans UR
- `permafrost.html` (61 en disco / 62 canónicos): **2.575** spans UR
- **Total vivo: ~6.686** spans UR repartidos en dos archivos
- **Pendiente**: el conteo de palabras únicas y la actualización del Alpha-UR no se han
  re-ejecutado sobre el material nuevo (qanat-00 + qanat-41→60). Re-pasar detector-UR cuando
  se retome el Alpha-UR. NO dar por bueno el "349 único" antiguo.

---


---

## CRITERIO RU ROJO (afinado 6 jun 2026)
El RU en rojo NO se pone en cualquier palabra con r+u. Solo es legal donde es ESPEJO DELIBERADO del UR: kurrulla (k-UR-RU-lla, el UR y su espejo juntos), K-UR-RULLA, y "la RU reflejada" (cuando se explica el concepto espejo). 
NO se marca RU en: palabras comunes (grulla, grullas, erudito), ni nombres propios/apellidos (Larruquert, Irulegi). Esos van en NEGRO aunque tengan r+u.
Y recordatorio previo: U suelta NUNCA en rojo (solo UR o RU completos). RU no genera entrada en Alpha-UR (solo UR).
