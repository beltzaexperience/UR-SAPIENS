# UR-SAPIENS — NOTAS DE PROYECTO
### Fuente de verdad única · Beltza Experience · Doneztebe · 2025–2026

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

## ARCHIVOS

- `index.html` — para GitHub Pages (producción)
- `index-local.html` — para trabajo local y correcciones
- `style.css` — CSS separado · `/* PREVIEW LOCAL */` al principio: borrar al subir a GitHub

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

## ARTÍCULOS PUBLICADOS — ESCOMBRERA (6 páginas en negativo)

La escombrera es el espejo RU del UR-book. Vive debajo, separada, con su propio wrapper, aside y JS. Orden en el DOM (modo DIARIO — más reciente primero):

| id | Página | Título |
|---|---|---|
| esc-05 | Pág. -05 | UR · RU · El Espejo del Futhark · ᛟ Ōþala |
| esc-04 | Pág. -04 | UR-Delta · Escombrera Política |
| esc-03 | Pág. -03 | UR-Delta · Escombrera Cósmica |
| esc-02 | Pág. -02 | UR-Vídeo · Futurismo Sónico · Partitura Concreta |
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
1. Las **15 páginas URI publicadas** (pub-prefacio, pub-intro, pub-qanats, pub-madres, pub-nietzsche, pub-inanna, pub-asia, pub-digitalismo, pub-tauros, pub-palimpsesto, pub-finisur, pub-cosmos, pub-tsunami, pub-basura, pub-urabe)
2. Los **depósitos del permafrost** ya construidos (qanat-01 a qanat-17)
3. Las **6 páginas RUI publicadas** (esc-prefacio, esc-01 a esc-05)

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
17 depósitos · cada uno con:
- Sección LABEL + H2 principal
- Secciones H3 con ▌
- Pullquote (border-left rojo)
- Glosario numerado
- Sección SEMILLAS pendiente
- Pie de navegación ← dep.anterior · DEPÓSITO NN · dep.siguiente →

| Dep. | Tema principal |
|------|----------------|
| 01 | B-UR-zum · tiniebla · cadena zahorí · Tolkien |
| 02 | Rumiante · RU espejo de UR · rumiantismo digital |
| 03 | K-UR-DA · Malerreka · M-UR-O Glaciar |
| 04 | Çatalhöyük · OR · T-OR-T-UR/A |
| 05 | De Ekain a UR-uk · la ruta imaginativa |
| 06 | UR-os del Titicaca · totora · arquitectura flotante |
| 07 | UR-ubamba · Inca-hispana · Q-UR-T-UBA |
| 08 | Roteta · Iruretagoyena · Lizarralde · Gordoa · Pagoeta |
| 09 | La-UR-entina · URI vasco · el poblado como nacedero |
| 10 | LOC-UR-A · AS-UR · UR-MIA · pleonasmo sagrado |
| 11 | Nagas · mosquito · carnaval · espata-dantza · Zugarramurdi |
| 12 | UR-OBORO · umami · garum · curva · beduino · ag-ur |
| 13 | Cweorð · Futhark hídrico · M-UR-mullo |
| 14 | B-UR-ga · Ourense · Elgorriaga · UR-beltz · UR-gorri |
| 15 | Vestvegr · UR-dax · diáspora vikinga · Catoira |
| 16 | Durruti · Hammurabi · G-UR · B-UR · Dr. Alimantado |
| 17 | Obispo Gonzalo · Mondoñedo · báculo · Gebō |

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

