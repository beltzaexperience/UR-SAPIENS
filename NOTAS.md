# UR-SAPIENS — NOTAS DE PROYECTO
### Fuente de verdad única · Beltza Experience · Doneztebe · 2025–2026

---

## IDENTIDAD DEL PROYECTO

**UR-SAPIENS** es una obra editorial digital: cosmogonía paleolingüística, diccionario insurgente, archivo cultural y biografía hídrica. Rigurosa y descabellada a partes iguales.

**Qué es**: Un qanat — canal subterráneo con pozos de acceso a distintas profundidades. Un vinilo — cara A y cara B, el surco como canal sónico. Una ceremonia: el agua que se reconoce a sí misma.

**Qué no es**: Tesis doctoral · manifiesto monolingüe · texto sagrado · mitificación del euskera como lengua pura · texto con rencor.

**Autor**: Luis Gonzaga Roteta · Koskero · Parte Vieja de Donostia · Beltza Records & Experience desde 1990 · Bautizado en San Vicente · Hijo del UR del molino Roteta (= molino en euskera).

**URL**: `https://beltzaexperience.github.io/UR-SAPIENS/`

---

## HIPÓTESIS CENTRAL

El fonema **UR** (agua en euskera) es un sustrato paleolingüístico preindoeuropeo conservado de forma dispersa y global. Fue **us-UR-pado** sistemáticamente por los sistemas mundo sucesivos — Sumerio → Grecorromano → Moderno → Digitalista — que lo redujeron a sufijo abstracto (-ura) mientras controlaban el agua como recurso.

La tesis no es que el mundo "hable vasco", sino que el agua, como realidad material y simbólica, dejó huellas fonéticas y culturales que el sistema ha domesticado.

### Ecuación madre
```
UR + E = mc² = SAPIENS
Agua + energía cósmica = conciencia
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

## ARCHIVOS

- `index.html` — CSS inlinado · para local y GitHub Pages
- `style.css` — CSS separado · alternativa GitHub Pages

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
Foto Oteiza Arantzazu
Brand-slash footer
Footer
```

---

## ⚠️ LOS MARQUEES — NORMA

### Marquee de texto superior (fijo)
- Vive entre la foto Nervión y el bloque PC₁.
- **No tiene id de control JS. No se mueve. Nunca.**
- Fondo rojo · texto crema · `font-size:0.85rem` · `animation: marquee 80s linear infinite`

### `id="marquee-movil"` (móvil dentro del feed)
- Se recoloca automáticamente con `colocarMarquee()`.
- **Modo diario**: después del primer artículo (`pub-qanats`).
- **Modo cronológico**: entre `pub-prefacio` y `pub-intro`.
- Lleva sus separadores propios: `id="marquee-movil-sep-top"` y `id="marquee-movil-sep"`.
- Fondo rojo · `animation: marquee 40s linear infinite`

### Marquee de texto inferior (fijo)
- Vive después del cierre de `#ur-book-wrapper`.
- **No se mueve. Nunca.**
- Mismo texto y estilo que el superior.

---

## ARTÍCULOS PUBLICADOS (14 páginas)

Orden en el DOM (arriba = más reciente):

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

**Paginación de cada artículo**: `· Pág. XX · UR + E=mc² = SAPIENS` · alineada a la derecha · Bebas Neue · color rojo.

---

## ORDEN DE LECTURA Y JS

### Modo DIARIO (defecto — más reciente primero)
`pub-qanats` (14) → ... → `pub-intro` (1) → `pub-prefacio`

### Modo CRONOLÓGICO
`pub-prefacio` → `pub-intro` (1) → ... → `pub-qanats` (14)

**`toggleOrden()`** — invierte el orden de los `<article>`, reordena prefacio/intro y llama a `colocarMarquee()`.

**`colocarMarquee()`** — reposiciona `#marquee-movil` y sus separadores según el modo activo.

**`burFiltrar()`** — filtro en tiempo real del índice del sidebar.

**`fitLines()`** — ajusta el font-size de los títulos fit-to-width en PC₁ al contenedor disponible. Se ejecuta en `document.fonts.ready` y en `resize`.

**`toggleSidebar()` / `closeSidebar()`** — drawer móvil desde la derecha.

---

## SIDEBAR — ÍNDICE

- Desktop: ancho fijo `430px`, fondo negro, textura papel
- Móvil: drawer fijo desde la derecha (`transform: translateX(100%)` → `.open`)
- Overlay `#sidebar-overlay` cierra al tocar fuera
- Al pulsar un link del índice en móvil → cierra automáticamente

**Contenido del sidebar**: Título · botón ⇄ · botón → INTRODUCCIÓN · buscador `#bur` · índice alfabético `.il` + `.ie` + `.ie-dada` (arte-facto dadaísta) + imágenes intermedias.

---

## NORMA UR EN ROJO

Cada fonema "ur" visible en el texto: `<span style="color:#b01a1a;">ur</span>` (o `UR` en mayúsculas).

La palabra circundante mantiene su color de contexto.

**En `.block-tag` / cabeceras con UR**: añadir `white-space:nowrap` al fragmento para evitar saltos.

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

---

## CAPÍTULOS PENDIENTES DE DESARROLLO

1. **Ins-UR-rección etimológica** — el UR que rompe el dique desde dentro. Marx como ins-UR-recto etimológico.
2. **El UR global** — Mongolia, Tíbet, África, Oceanía. K-UR-osawa ampliado. Principio antirracista: "el aquí es allí".
3. **Terror lingüístico / jacobinismo** — Barère 1794. El estado-nación como máquina de exterminio lingüístico.
4. **La cosmogonía hídrica completa** — H₂O → UR orgánico → Musgo → Roble → Lumbre → Odisea Espacial.
5. **De UR-Sapiens a UR-suario** — Microplásticos en sangre, esperma, placenta, cerebro. "Inteligencia plástica".
6. **Anarco-catolicismo basko/galego** — Dorothy Day · Tolstói · Dujobory · Boardman Robinson · George Bellows.
7. **El ritual del UR** — Bautismo preeclesial. Koskero vs JoseMaritarras. Molino Roteta.
8. **La leyenda del tiempo** — Camarón 1979. Jazz afro + flamenco gitano. La música como conocimiento superior.
9. **El digitalismo p-UR-itano** — El agua virtual que enfría los servidores. UR-suario vs UR-Sapiens.
10. **H-UR-mor como antídoto** — Las Ratas Vascas de Marte. "Ura non dago?" Ag-UR como despedida.

---

## CICLO DEL UR (columna vertebral visual)

```
UR-lañó (nube)
      ↓ lluvia (E-UR-i)
Manantial (IT-UR-I)
      ↓ río
Molino Roteta
      ↓ estuario
Mar (UR salado)
      ↓ evaporación
UR de los muertos
      ↓
UR-lañó
```

Este ciclo es la columna del libro. No todo tiene que nombrarlo explícitamente, pero todo debe poder conectarse con él.

---

## CRITERIOS DE ESCRITURA

- Cada página tiene una **idea madre**. Una sola.
- La repetición solo se acepta como estribillo, eco o retorno deliberado. Si no cumple función, se corta.
- Las deformaciones gráficas (T-OR-T-UR-A, BAS-UR-A-PIENS) son herramientas semánticas, no tics. Cuando dejan de abrir sentido, se retiran.
- El tono puede ser documental, poético, político, humorístico o autobiográfico — no todo a la vez en cada párrafo.
- Cada página funciona como una canción: arranque · desarrollo · nudo · salida.
- Las referencias (sumerios, Ekain, Inanna, qanats, dub, punk, toponimia) aparecen cuando aportan estructura, no por acumulación.

---

## CRITERIOS DE EDICIÓN

- Revisar ortografía, tildes y consistencia tipográfica.
- Una sola convención para guiones, mayúsculas y siglas.
- Evitar duplicados salvo cuando sean deliberados y funcionales.
- Si una idea ya tiene su página, la siguiente no repite — avanza.

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

- [ ] Corrección general de textos (en curso)
- [ ] Fotos pendientes en algunos artículos
- [ ] Posibles artículos nuevos (páginas 15+)
- [ ] Revisar comportamiento sidebar en móvil con orden cronológico

---

## UR-VÍDEOS — MÉTODO CORRECTO (sin Flickr, sin Vimeo)

Flickr no expone vídeos en su CDN como hace con las fotos. El `data-flickr-embed` enlaza a `flickr.com` — no válido (cuenta privada/censurada desde 2005). Vimeo funciona pero requiere pasos extra.

**Solución: `<video>` HTML5 nativo con mp4 convertido**

El flujo es el mismo que con las fotos pero con un paso de conversión:

1. Convertir el archivo original (`.mov`, `.mp4`) a mp4 comprimido:
```bash
ffmpeg -i original.mov -vcodec libx264 -crf 28 -preset slow -acodec aac -b:a 128k -movflags +faststart -vf "scale=-2:720" ur-video.mp4
```
Resultado típico: 53MB `.mov` → 1,1MB `.mp4`

2. Subir el `.mp4` al repositorio de GitHub junto al `index.html`

3. Insertar en el HTML:
```html
<div style="max-width:380px; margin:1rem auto;">
  <video controls playsinline style="width:100%; height:auto; display:block;">
    <source src="[nombre-archivo].mp4" type="video/mp4">
  </video>
</div>
```

**Tamaño oficial UR-vídeos verticales**: `max-width:380px; margin:1rem auto` — mismo que el vídeo de As Burgas en Vimeo.

**Sin dependencias externas. Sin Flickr. Sin Vimeo. Funciona en local y en GitHub Pages.**

**Registrado**: Mayo 2026 · primer UR-vídeo en paratexto *El Más Aquí* · `ur-video.mp4`

| Fecha | Decisión |
|---|---|
| 2025–2026 | Arquitectura feed + sidebar establecida |
| 2026 | 14 páginas publicadas |
| 2026 | Fondo de papel por artículo (no en `<main>` global) |
| 2026 | Marquees superiores e inferiores fijos · marquee-movil con JS |
| 2026 | fitLines() para títulos fit-to-width en PC₁ |
| 2026 | Sidebar drawer desde la derecha en móvil |

---

## FRASE DE ARRANQUE PARA NUEVA CONVERSACIÓN

*"Soy Luis Gonzaga Roteta, koskero de la Parte Vieja de Donostia, bautizado en San Vicente, hijo del UR del molino Roteta. Estoy desarrollando el UR-book: una paleolingüística insurgente sobre el fonema UR/agua como sustrato cósmico us-UR-pado por los sistemas mundo. Tengo el HTML en index.html y las NOTAS. Arrancamos."*

---

*Gora UR · Ag-UR · Beti UR*
*UR + E = mc² = SAPIENS*
