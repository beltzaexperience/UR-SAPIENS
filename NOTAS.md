# UR-SAPIENS · NOTAS DE PROYECTO

## Archivos
- `index.html` — todo en uno con CSS inlinado (para local sin servidor)
- `style.css` — CSS separado (para GitHub Pages)
- El `index.html` de GitHub usa `<link rel="stylesheet" href="style.css">` — sin inlinar

---

## ESTRUCTURA GENERAL

### Topband
- Izquierda: `BELTZA RECORDS · DONOSTIA _ DONEZTEBE`
- Derecha: `beltzarecords.com · MANIFIESTO · MAGIC BUS · DUB²BEAT · UR-SAPIENS`
- Móvil: flex-wrap, fuente reducida a 0.72rem, links visibles

### Brand-slash
- Fondo rojo, `UR` negro + `SAPIENS` sobre negro
- Logo SVG símbolo UR + imágenes derecha
- Móvil: padding reducido

### PC₁ — Símbolo + Título
- Desktop: símbolo izq + título fit-to-width derecha
- Móvil: símbolo a **full width**, título oculto (`display:none`)
- El subtítulo en la intro-3col lo sustituye

### Marquee de fotos
- Animación `marquee-fotos 70s`
- Clic pausa/reanuda
- Fotos actuales: incluye Nervión Abril 2026 (×2) + resto colección

### Intro 3 columnas
- Fondo textura papel `db52b26076_h.jpg`
- Grid 1fr 1.4fr 1fr → en móvil 1 columna

### UR-BOOK wrapper
- `id="ur-book-wrapper"` — flex en desktop, block en móvil
- Feed (main) izquierda + Sidebar derecha

---

## SIDEBAR / ÍNDICE

### Desktop
- Ancho fijo 430px, fondo negro, textura papel
- `toggleSidebar()` muestra/oculta con `display:flex/none`

### Móvil
- **Drawer** desde la derecha: `transform: translateX(100%)` → `.open: translateX(0)`
- Overlay oscuro `#sidebar-overlay` cierra al tocar fuera
- Botón `☰ ÍNDICE` en topband (solo visible en móvil, `#btn-hamburger`)
- Botón `✕ CERRAR` dentro del drawer (`#sidebar-close`)
- Al pulsar link del índice → cierra automáticamente

### Contenido del sidebar
1. Título `ÍNDICE UR-BOOK`
2. Botón `⇄ CRONOLÓGICO / ⇄ DIARIO` (mismo estilo que → LEER INTRODUCCIÓN)
3. `→ LEER INTRODUCCIÓN`
4. Lista de entradas `.ie` y `.il`
5. Buscador `#bur`

---

## ORDEN DE ARTÍCULOS

### Modo DIARIO (defecto — más reciente primero)
`pub-14 (qanats) → ... → pub-02 → pub-intro → pub-prefacio`

### Modo CRONOLÓGICO (invertido)
`pub-prefacio → pub-intro → pub-02 → ... → pub-14`

### Marquee móvil `#marquee-movil`
- **Diario**: después del primer artículo (pub-14)
- **Cronológico**: entre pub-prefacio y pub-intro
- Se reposiciona automáticamente con `colocarMarquee()`
- Respira con línea negra `clamp(0.5rem,2vw,1.75rem)` arriba y abajo

---

## FONDO DE PAPEL CONTINUO
- Textura: `55167948157_ee65a87707_o.jpg`
- Cada `<article>` tiene su propio `background-image` (no el `<main>`)
- El sidebar interior también tiene la textura
- `.ur-main` en el CSS también la tiene
- **NO tocar con replace masivo** — se pierden instancias

---

## FOTOS AÑADIDAS POR ARTÍCULO

| Artículo | Foto | Posición |
|---|---|---|
| pub-prefacio | Supernova ESO (astroaventura.net) | Bajo h3 "SOMOS UR + POLVO DE SUPERNOVA" |
| pub-nietzsche | Nietzsche con su madre (Guardian) | Tras párrafo Camello-León-Niño |
| pub-inanna | Astarté bronce fenicio (camas.es) | Tras cita "La estrella viajó por mar" |
| pub-inanna | Gilgamesh/Toro Celeste (Wikipedia) | Tras párrafo "primera epopeya / elegía" |
| pub-madres | Relieve Kom Ombo (Reddit) | Tras "Son las madres del UR-SAPIENS" |
| pub-madres | Comadrona romana (worldhistory.org) | Tras párrafo "útero como canal" |
| pub-basura | Portada LP BAS-UR-A (Flickr) | Full width + pie + texto debajo |

---

## PAGINACIONES AÑADIDAS
- pub-prefacio: `· Prefacio · UR + E=mc² = SAPIENS`

---

## TYPOS CORREGIDOS
- `'Bebas Nye'` → `'Bebas Neue'` en pub-madres h2
- `font-weight:700` eliminado del título ÍNDICE UR-BOOK (causaba engorde en fallback)

---

## LINKS
- DUB²BEAT: `http://dubbeat.beltzarecords.com/` — topband y footer

---

## MÓVIL — BREAKPOINTS
```css
@media (max-width: 900px) → intro-3col a 1 columna
@media (max-width: 768px) → móvil completo (drawer, topband, ur-main, artículos)
```

### Reglas clave móvil
- `#ur-simbolo-box { width:100% }` — logo full width
- `#ur-titulo { display:none }` — título oculto (subtítulo lo sustituye)
- `#btn-hamburger { display:flex }` — visible solo en móvil
- `#sidebar { position:fixed; transform:translateX(100%) }` — drawer
- `#sidebar > div { padding: 0.8rem 1rem 2rem 1rem }` — padding interior restaurado

---

## PENDIENTE
- Fotos pendientes en algunos artículos
- Rattus Norvegicus: imagen duplicada eliminada, queda solo la primera
