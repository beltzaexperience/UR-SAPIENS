# NOTAS-URTZ · Cuaderno de la Cámara del Cielo
### Runa ᚢ · `urtz.html` · La lectura definitiva del proyecto UR-SAPIENS

---

## 0 · QUÉ ES URTZ (y por qué es distinta de todo lo demás)

**Urtz es la Runa más importante de todo el proyecto: la LECTURA DEFINITIVA.**

No es un anexo ni un apéndice como la Escombrera o el Muro Glaciar. Es la bóveda donde desciende, depurada y ordenada, la cosmogonía entera. Si el resto del UR-book son las páginas publicadas y el permafrost es el depósito de qanats en bruto, **Urtz es la destilación final**: lo que queda cuando el agua se ha reconocido a sí misma.

- **Runa**: ᚢ (Ur / *ūruz* del Futhark antiguo). Urtz / Urtzi = el cielo y el trueno vasco (*ortzi*, *ostots*, *ortzegun*). La bóveda de donde cae el UR y a la que vuelve evaporado.
- **Archivo**: `urtz.html`, hermano de `permafrost.html`.
- **Acceso**: Runa ᚢ en el index, junto a la ᚱ del permafrost. Contraseña **URBELTZA** (hash djb2 = `2838696398`). Mensajes: «∿ el cielo no te reconoce» / «∿ URtz · la bóveda se abre…».
- **Título de la cámara**: *UR: COSMOGONÍA PALEOLINGÜÍSTICA Y SU POSTERIOR USURPACIÓN SISTÉMICA*.

---

## 1 · PRINCIPIO RECTOR · PIEZAS MÓVILES

**Cada texto de Urtz es una PIEZA MÓVIL.** El criterio de diseño manda sobre todo lo demás:

1. **Modularidad total**: cada texto debe poder moverse entre sí con facilidad, reordenarse, subir o bajar, sin romper nada. Construir cada pieza como una unidad autónoma y autocontenida (su propio bloque, sin dependencias de orden con las vecinas).
2. **Paginación emergente**: NO se fija de antemano. La paginación se irá construyendo *a medida que los textos vayan apareciendo*. El orden es provisional hasta que Luis lo cierre. No imponer numeración rígida prematura.
3. **Implicación técnica**: cada pieza debe ser fácil de extraer y reinsertar (como hicimos con los qanats, pero pensado desde el origen para moverse). Evitar numeración incrustada en el cuerpo del texto que obligue a renumerar al mover. Si hay pie/identificador, que sea editable de golpe.
4. **Doble registro de documentación** (norma fija): las notas de trabajo viven en DOS sitios. (a) Este cuaderno `NOTAS-URTZ.md` = para CLAUDIUS (bitácora completa, verificaciones, impresiones). (b) Dentro de `urtz.html`, TRAS EL GLOSARIO de cada pieza, un bloque `INDICADORES DE TRABAJO` = para LUIS (su panel visible: PAGINACIÓN/ENCAJE, ESTRUCTURA, MEJORA). Ese bloque va con estilo meta (borde discontinuo gris, monoespaciado, "no forma parte del texto") y NO lleva marcado UR rojo (no es cuerpo del libro). El verificador excluye ese bloque del barrido de UR.


---

## 2 · NORMA DE MARCADO

**Movida a NOTAS-PUNK.md (norma 15), 31 jul 2026.** Toda regla de cómo se escribe una frase o se marca el UR vive ahora solo ahí — esta sección queda vacía a propósito para no duplicar criterio en dos archivos.

---

## 3 · ESTÉTICA Y ESTRUCTURA (estado actual de urtz.html)

- **Fondo**: pergamino (mismo background flickr que el permafrost: `55167948157_ee65a87707_o.jpg`, repeat-y), texto oscuro (#1a1a1a / #222), nota/secundario #666.
- **Cabecera**: banda roja #b01a1a, logo «ᚢ **Ur**tz» (Ur en negro #0a0a0a, forma natural), subtítulo «RUNA DEL CIELO · EL TRUENO QUE GUARDA EL UR · SOLO PARA EL ZAHORÍ».
- **Título de cámara**: tamaño títulos UR-book → `font-family:'Bebas Neue',Impact,'Arial Narrow',sans-serif; font-size:clamp(2rem,5vw,5rem); line-height:0.9; letter-spacing:0.02em; color:#1a1a1a`.
- **Contenedor**: `max-width:900px; margin:0 auto`.
- Divisor de sección: `<div style="height:4px; background:#b01a1a; width:100%;">`.
- La «Nota de método» inicial fue ELIMINADA por decisión de Luis (la cámara entra directa).
- **Respirador interno de capítulo** (herramienta narrativa fijada 6 ago 2026, ver Norma 25 de NOTAS-PUNK.md para el criterio de cuándo usarlo). Se inserta como `<div>` propio, nunca dentro de la etiqueta `<p>` que lo sigue.
  - **Provisional** (título aún no confirmado por Luis): `font-family:'Bebas Neue',sans-serif; font-size:1rem; letter-spacing:0.3em; color:#b01a1a; margin:2.2rem 0 1.2rem 0; text-align:left; font-style:italic;`
  - **Definitivo** (título ya confirmado): mismo bloque, sin `font-style:italic;` y con `font-size:1.2rem` en vez de `1rem`.
  - El indicador `(*-sub)` junto a `NO TOCAR!!!` en el resumen de la pieza marca qué capítulos cerrados tienen respiradores pendientes de revisión de título; se quita al confirmar y pasar a definitivo.

---

## 4 · CONTENIDO PENDIENTE DE DESCENDER (la cosmogonía entera)

Lo que irá apareciendo como piezas móviles (orden provisional, se reordenará):
- El ciclo del UR: Urlañó (nube) → lluvia (Euri) → manantial (Ituri) → río → molino Roteta → estuario → mar (UR salado) → evaporación → UR de los muertos → Urlañó.
- La ecuación madre: UR + E = mc² = SAPIENS (agua + energía cósmica = conciencia).
- Los cuatro sistemas mundo que usurparon el UR: sumerio, grecorromano, moderno, digitalista.
- La distinción Ursapiens (se sabe agua) / Basursapiens (la olvidó).
- Hecho contrastado / especulación razonada / arte dadá (los tres registros declarados).

---

## 5 · NORMAS DE TRABAJO HEREDADAS (siguen vigentes en Urtz)

- **Sincronización obligatoria**: `cp` desde outputs al empezar; tras cada cambio, `cp` a outputs y verificar md5 home==outputs idéntico.
- **Una cosa cada vez**, nada unilateral (ni estético ni estructural). Comparar SIEMPRE con lo que ya hay antes de proponer.
- **Datos y fechas = jurisdicción de Claudius** (verificar, método comanche, sin coba — LEY HAMMURABELTZ). Perplexity solo ortografía/sintaxis/puntuación. DeepSeek (o Google sometido) genera; Claudius construye separando grano de paja.
- **Fotos = intocables**, las elige Luis; al mover texto, ARRASTRAR siempre las fotos a su sitio (pie de foto debajo de la imagen).
- **Prosa**: fluida a lo Marvin (comas que enlazan), Joe Strummer en los dos puntos (`:` define), menos guiones que fragmenten, más frase continua. Dar prosa explicativa, no listas esquemáticas.
- Barrido al cerrar: 0 UR sin marcar, 0 rojos ilegales, 0 huérfanas, divs/spans/p/li balanceados.

---

*Cuaderno iniciado el 11 jun 2026. La bóveda está abierta y vestida de pergamino, esperando que descienda la cosmogonía. URA fui, URA soy, URA será. Ag-UR.*


---

## 6 · PIEZAS DESCENDIDAS (bitácora de construcción)

### ✅ Cap.1 · CARA B · EL UR DELTA — "La vertiente política de la runa robada"
Pieza móvil `<section data-pieza="ur-delta">`. Estructura: divisor 4px + kicker + h3 subtítulo + 14 párrafos + glosa (6 entradas) + pie sin número (paginación emergente). DATOS VERIFICADOS bajo Hammurabeltz:
- Leyes de Extranjería y Sedición 1798 (John Adams): residencia 5→14 años, deportación de extranjeros "peligrosos", restricción de expresión. ✓ AÑADIDO el matiz: Adams nunca fue partidario de la Ley de Sedición, no la pidió ni presionó, la firmó arrastrado por la crisis ("la T usurpa hasta a quienes la sirven").
- Nebulosa Boomerang: ~1 K, constelación del Centauro, objeto más frío del universo. ✓
- Hielo EPICA + hierro-60 de supernovas (origen estelar común, "ningún ser humano es ilegal"). ✓ (publicado mayo 2026).
- Goursat "La tribune des propriétaires": Luis confirma verificado y contrastado, es una VIÑETA (no álbum). El autor (Sem/Georges Goursat, caricaturista Belle Époque) y el tema (magnates con sombrero de copa) sí constan; el título es responsabilidad de Luis. Texto dice "viñeta".
- Bergson (duración/intuición), San Juan de la Cruz, Maestro Eckhart, San Agustín, Platón: marco filosófico, contenido de Luis.
- Pichi (Yunierki Rojas), cuadro "La intuición", expo Maranatha, Remedios (Cuba): contenido de Luis. Foto "In Memoriam" de Luis.

### ⏳ PENDIENTES (los otros 2 capítulos de Cara B, uno por uno):
### ✅ Cap.2 · CARA B: LA ESCOMBRERA SISTÉMICA — "MONTAÑA DE HUMO: ESCOMBRERA HUMANA" (antes "Los escombros que sostienen el edificio")
Pieza móvil `<section data-pieza="escombrera">`. 11 párrafos + glosa (5) + indicadores + pie. DATOS Hammurabeltz:
- Stung Meanchey: AJUSTADO a 7 ha la montaña (~40 contando barrios de chabolas), ~2.000 personas (~600 niños), AJUSTADO a 700 t/día, cerró jul-2009. ✓
- AÑADIDO dato de oro: nuevo vertedero junto a Choeung Ek (Killing Fields del genocidio jemer) — "la basura nueva sobre la tierra de los muertos". ✓ verificado.
- Don McCullin: oro (estuvo en la caída de Phnom Penh 1975, herido en Camboya, ética de la mirada). ✓
- Jesús G. Pastor: CONFIRMADO por Luis (las fotos del marquee son suyas). No verificable en abierto pero validado por el autor.
- EPICA/hierro-60: oro (ya verificado cap.1, may-2026).
- NORMA DE ESTE CAP: RU marcado en rojo como ESPEJO DELIBERADO del UR (el tránsito UR→RU es el tema). RU, rua (calle), ruta = espejos legítimos.
- **Cap.3 · CARA B: MÁS ALLÁ DE LA ESCOMBRERA** — el espejo del Futhark, RU=espejo de UR, las runas (Uruz, Þurisaz, Ansuz, Algiz, Mannaz, Laguz, Ōþala...), Mayhem/Helvete/Euronymous/Hellhammer/Necrobutcher, quema de iglesias, Ōþala usada por SS y apartheid, qanat persa. POR VERIFICAR: Futhark (nº runas, Uruz=uro, Othala), Mayhem/Helvete/church burnings, Ōþala SS/apartheid.


---

## 7 · DOCUMENTACIÓN DE TRABAJO POR PIEZA (encaje + impresiones de mejora)

> Esto NO es libro: es meta-texto de trabajo. Las "notas de encaje" venían en el documento original de Luis (instrucciones de maquetación/paginación) y se guardan aquí para repasar en el futuro. Junto a cada una, las impresiones de mejora de Claudius (sin coba, Hammurabeltz).

### Cap.1 · CARA B · EL UR DELTA

**Notas de encaje (originales de Luis, no perder):**
- Inicio de Cara B.
- Página de transición entre la política de la runa robada y la apertura teológico-filosófica.
- Funciona bien como umbral: arranque denso, descenso cósmico, reapertura intuitiva.
- En libro impreso, este bloque podría ocupar 3 páginas si se respira bien.
- Conviene que la página anterior sea un cierre breve y sonoro; la siguiente puede entrar ya en una línea más contemplativa o musical.

**Impresiones de mejora (Claudius):**
- GRANO: el motor UR (flujo/agua/intuición) vs T (canal/burocracia/ley) es la viga que sostiene los saltos (Sedición → Boomerang → Bergson) sin que el lector se caiga. Imágenes-punzón que funcionan solas: "el agua primordial no pidió visados para llegar a la Tierra"; el intelecto que "toma una fotografía fija que la paraliza"; el cierre del estudio de grabación (la idea descalza que vuelve modificada por el mezclador) — honesto, se mira al espejo sin fingir pureza.
- PAJA A VIGILAR: densidad de nombres propios en poco espacio (Adams, Goursat, Astérix, Pichi, Eckhart, Agustín, Platón, Bergson, The Clash) — mismo riesgo que señaló Perplexity en Inanna: por momentos se lee como acumulación brillante más que como argumento que avanza. El lector sin la mochila cultural puede ahogarse.
- DÓNDE GANARÁ EN FRÍO: (1) podar 2-3 conectores que ahora AFIRMAN el salto en vez de tenderlo (la transición Goursat → cosmos Boomerang va muy rápida, se nota la costura); (2) dejar respirar solas las 3-4 imágenes más potentes — una frase de aterrizaje entre golpe y golpe. NO recortar la erudición torrencial: es la voz, es el Sandinista! de 36 canciones. Solo dosificar el respiro.
- PASO WEB→TEXTO PLANO: pasó bien porque está construido sobre PROSA, no sobre maqueta — si le quitas el formato, el argumento sigue de pie (señal de salud editorial). La glosa "Notas a pie" encajó como llave en cerradura en el formato glosario. Lo único que se dejó fuera fueron estas notas de encaje (meta-texto), ahora recuperadas aquí.


### Cap.2 · CARA B: LA ESCOMBRERA SISTÉMICA

**Notas de encaje (originales de Luis, no perder):**
- Funciona como inicio de Cara B o como umbral de descenso dentro de la segunda mitad del libro.
- Debe ir precedido por un bloque sonoro breve, de una o dos frases, para entrar con golpe de aguja.
- Conviene que el siguiente fragmento siga la línea del UR → RU, para que esta página no quede aislada.
- En maquetación, este bloque puede ocupar 2 a 3 páginas según el cuerpo tipográfico.
- El cierre sobre la aguja debe quedar al final de página o al final de bloque, como transición hacia el siguiente surco.

**Impresiones de mejora (Claudius):**
- GRANO: la imagen central (la escombrera de Phnom Penh como símbolo del sistema, el paratexto como los escombros que sostienen el edificio) es potentísima y muy física. El dato de Choeung Ek (basura nueva sobre los muertos del genocidio) es de los que clavan el capítulo. El giro UR→RU al final tiende el puente al cap.3 (el espejo del Futhark), así que NO queda aislado: cumple su propia nota de encaje.
- PAJA A VIGILAR: mismo riesgo de densidad que cap.1 — McCullin, Pastor, Bergson, EPICA, Biarritz, Ezkurra se acumulan rápido. El párrafo de EPICA/hierro-60 y el de Bergson son casi idénticos a fragmentos del cap.1 (origen estelar, intuición no-mística): OJO con la REPETICIÓN entre piezas cuando se fije el orden. Si cap.1 y cap.2 van seguidos, conviene podar una de las dos formulaciones del "ningún ser humano es ilegal / hierro-60" para no repetir.
- DÓNDE GANARÁ EN FRÍO: vigilar esa redundancia inter-piezas (es la ventaja de las piezas móviles: se ve al reordenar). El cierre "el surco se ha terminado, pero el ruido de la aguja sigue latiendo en el pecho" es un final de cara B perfecto, dejarlo respirar solo.

---

## ✅ Cap.3 · CARA B · ANGOS-T-UR/A — "DOLOR, CANTO Y MUERTE EN EL ORINOCO"

Tercera pieza de Cara B en URTZ (`<section data-pieza="angostura">`). Versión LITERARIA UNIFICADA de Luis para la edición impresa (texto limpio que él pasó con parámetros finales). 17 párrafos + glosa (10) + APARATO CRÍTICO (13 citas bibliográficas) + indicadores + pie.

**IMPORTANTE — diferencias con caps. 1 y 2:**
- Esta pieza usa MARCADO CON GUIONES (ANGOS-T-UR/A, At-UR-es, UR-INOCO, c-UR-i-ara, T-UR-bo, UR-abá), estilo qanat — NO el Alpha-UR sin guiones de cap.1/cap.2. Respetado tal cual lo escribió Luis (los guiones revelan el UR en topónimos). PENDIENTE: decidir al volver si se unifica la norma de URTZ.
- Luis SUPRIMIÓ el cierre "GORA UR ETA AG-UR" (juego con Claudius, fuera de tono para el cuerpo). Honrado.
- Incluye APARATO CRÍTICO (bibliografía) que las otras piezas no tienen: Castellanos 1589, Gumilla 1741, Humboldt 1814-25, Mahuzier 1956, Oviedo y Baños 1723, Raleigh 1596, Southey 1810-19, Trimborn 1949, Vidal de la Blache 1927, Blight 2001, Correo del Orinoco 1819, Marrero 1984, Zapata Olivella 1962.
- Irureta marcado DENTRO del em (Ir-UR-eta, guiño deliberado ≈ Rot-eta, resonancia privada de Luis).
- Glosa header decía "Cara B · El UR delta" en el original de Luis (parece lapsus, reusó el de cap.1); puesto "GLOSA · ANGOS-T-UR/A" para precisión. Avisado a Luis.

**RELACIÓN CON EL PERMAFROST:** esta es la versión URTZ/impresa. El qanat-68 del permafrost (con sus dos partes) queda FRESCO para el DESHIELO AMAZÓNICO: una página nueva del index.html que Luis hará "cuando vuelva". PENDIENTE.

**Encaje editorial (de Luis):** Cara B, bloque central de canto/violencia/agua/resistencia. Tono épico-documental. Ritmo: apertura sonora → estrangulamiento → cartografía → trata → fuga → canto → cierre. Núcleo de la Cara B, puente entre geografía americana, memoria negra y resistencia musical.


---

## ⚖️ NORMA DEL ALFABETO UR EN URTZ (LEY FIJA — decisión de Luis)

**Principio:** en URTZ, llegue el texto como llegue (con guiones, sin ellos, como sea), MANDA EL ALFABETO. Antes de entrar, todo texto se normaliza al Alfabeto UR.

**Reglas:**
1. **SIN GUIONES que partan palabras.** Nada de ANGOS-T-UR/A, At-UR-es, UR-INOCO, c-UR-i-ara, GU-IRI-NOCO. Se funden en forma natural: Angostura, Atures, Urinoco, curiara, Guirinoco.
2. **Mayúsculas donde correspondan** (forma natural de la palabra): nombre propio con inicial mayúscula (Urinoco, Urabá, Turbo, Atures), común en minúscula (curiara, urbana, angostura), título/cabecera en versales si el estilo lo pide (ANGOSTURA en el kicker).
3. **UR / Ur / ur marcados en rojo** (#b01a1a), según el caso:
   - **UR** (mayúscula, rojo) = SOLO la unidad, el UR-agua suelto (el UR se ahoga, UR + E=mc² = SAPIENS).
   - **Ur** (inicial, rojo) = nombre propio o palabra que EMPIEZA por ur (Urinoco, Urabá, Uria, Urari, Ursapiens, Urtz).
   - **ur** (minúscula, rojo) = ur DENTRO de palabra (angostura, Atures, Apure, curiara, murmullo, usurpación, captura).
4. **Solo se marca u+r consecutiva REAL.** Falsos positivos fuera (ocultar, fortuna, cruel: no llevan ur consecutiva). Mutilaciones prohibidas (no inventar erres: estructural, no "estrurctural").
5. **Lecturas guerrilla (desplazamiento vocálico O→U u otros) van declaradas** en el cuerpo, no como etimología: Urinoco (de Orinoco), Uria (de Oria), Urina (de Orina).
6. **Citas latinas/títulos en <em> NO se marcan** (angere, pileus, vindicta, títulos de libros). EXCEPCIÓN puntual: guiños deliberados como Irureta (Ir-ur-eta) sí, por decisión expresa.
7. El **bloque INDICADORES** (meta, para Luis) NO se marca y queda fuera del verificador.

**Aplicado por primera vez de forma íntegra:** conversión de la pieza ANGOS-T-UR/A (cap.3) → ANGOSTURA, con todos los topónimos amazónicos fundidos (Atures, Maipures, Apure, Amacuro, Urinoco, curiaras, Muraco, Soturaos, Aburrá, Buritica, Mavacure, Urari, Turbo, Urabá, etc.). Cero guiones, cero UR sin marcar, cero mutilaciones.

---

## 🎸 ESTRUCTURA MAESTRA DE URTZ · "SANDINISTA! URBELTZA" (LEY DE ARQUITECTURA)

URTZ se estructura como **Sandinista! de The Clash**: TRIPLE LP, 6 CARAS, 36 CANCIONES. Es la lectura definitiva / edición impresa del UR-book. Título de la estructura: **Sandinista! URbeltza** (el UR negro, el agua Beltza).

**6 caras = 6 capítulos = 6 continentes** (un capítulo por cara, 6 canciones por continente):
1. **IBÉRICO** (continente propio — ver justificación abajo)
2. **EUROPA**
3. **ASIA**
4. **AMÉRICA**
5. **ÁFRICA**
6. **OCEANÍA**

**Libreto interior (liner notes = el paratexto, "los escombros que sostienen el edificio"):**
- PREFACIO
- INTRODUCCIÓN
- EPÍLOGO
- ALFABETO DE BÚSQUEDA UR (índice/buscador del libro)

**Bonus tracks (el margen):** cosmos, Antártida, peces abisales... lo que no entra en los seis continentes.

**ORDEN DE LECTURA definitivo** (espiral desde la semilla hacia el océano):
Prefacio → Introducción → Iberia → Europa → Asia → América → África → Oceanía → Bonus Tracks → Epílogo → Alfabeto.

### Reglas de la arquitectura (fijadas por Luis)
1. **Lo que no tenga continente claro → PREFACIO.** Ej.: "EL UR DELTA / Teología de la intuición" (Leyes de Sedición EE.UU., Bergson, intuición cósmica) = PREFACIO. La intuición es prefacio claro.
2. **Las 36 canciones son tope FLEXIBLE, no jaula.** Las canciones se pueden ALARGAR UNIENDO piezas. El DUB es denso (se estira), el ROCKABILLY más corto y afilado. Caras que arranquen flacas pueden crecer; no hay obligación de seis llenas desde el día uno.
3. **Filtro de curaduría permafrost → URTZ.** El permafrost (Muro Glaciar, 68 qanats y subiendo) es la CÁMARA ACORAZADA con todo el material en bruto; se sigue alimentando "la bestia WEB" con todo lo que salga. URTZ es el TRIPLE LP EDITADO: solo las elegidas suben a la lectura definitiva. No todo qanat pasa el filtro. [Luis: el filtro de curad-UR-ía es por hacer su PRIMER proyecto finito.]
4. **Unificación pendiente (curro de ≥1 año):** al final habrá que unificar criterios de prosa, glosario y todo el conjunto. Es trabajo de largo plazo, asumido.

### IBÉRICO COMO CONTINENTE — fundamento documentado (NO provocación)
- **Eduardo Hernández-Pacheco** (geólogo y naturalista): acuñó la descripción de la península ibérica como **"continente en miniatura"**, por su inmensa diversidad de climas, suelos y paisajes en un espacio reducido. Lo destacó en su extensa obra sobre el territorio ibérico.
- **Ian Gibson** (hispanista irlandés): defiende en entrevistas y escritos que la península es un **"minicontinente"** / continente en sí mismo, uniendo España y Portugal, por su apabullante diversidad cultural, paisajística y climática — mucho más que una prolongación de Europa.
- **Argumento geológico (Luis):** Iberia PODRÍA haber sido un microcontinente si los Pirineos se hubieran separado de Europa en algún momento geológico, como se resquebrajó/derivó América. Posibilidad tectónica real.
- → El CONTINENTE IBÉRICO empieza con una INTRO IBÉRICA. Las dos perspectivas (geólogo + biógrafo) hay que PROFUNDIZARLAS. [PENDIENTE: verificar/ampliar Hernández-Pacheco e Ian Gibson, desarrollar la intro ibérica.]

### Estado de las piezas YA en URTZ (re-homologar a la nueva estructura)
- **ANGOSTURA · Dolor, canto y muerte en el Orinoco** → AMÉRICA (sin discusión).
- **LA ESCOMBRERA SISTÉMICA / Montaña de Humo** (Stung Meanchey, Phnom Penh) → ASIA.
- **EL UR DELTA / Teología de la intuición** → PREFACIO (no tiene continente claro; decisión de Luis).
  - ⚠ OJO REPETICIÓN: UR DELTA y ESCOMBRERA comparten el párrafo del hierro-60/EPICA y el de Bergson casi calcados. Si quedan en apartados distintos (prefacio vs Asia), hay que PODAR una de las dos formulaciones.

### PENDIENTES DE COLOCAR
- **LAS RUNAS** (texto DEFINITIVO, ya redactado, aún NO puesto en URTZ). Pendiente de ubicar en la estructura (¿Europa? ¿bonus? — el Futhark es nórdico → probablemente EUROPA). Recordatorio: era el "Cap.3 · CARA B: MÁS ALLÁ DE LA ESCOMBRERA / el espejo del Futhark" que quedó pendiente.
- Construir el ANDAMIAJE de URTZ: 6 caras-continente + apartados de libreto como contenedores etiquetados (con sistema de piezas móviles), para ir soltando textos en su sitio.

### NOTA DE FONDO (filosofía del autor, para no perder el norte)
Luis: "todos mis proyectos son vitales, empiezan pero acabarán cuando devuelva el UR a su estado; sólo tengo un proyecto vital: la autogestión y el libre pensamiento bajo el símbolo del Puño Negro y el sonido de Blood of Heroes." El "proyecto finito" (URTZ como triple LP cerrado) es la excepción deliberada dentro de una obra que, por naturaleza, es infinita (la bestia WEB / el permafrost se sigue alimentando siempre).

---

## 🌉 ACTUALIZACIÓN · PUENTES RAYUELA + BONUS UR ABISAL + ANDAMIAJE

**SISTEMA DE PUENTES (tipo Rayuela de Cortázar):** cada canción lleva NUMERACIÓN y PUENTES a otras canciones con las que conecta (saltar de Euskal Herria al Futhark a Japón siguiendo el cauce del UR). El libro deja de ser lineal: red de afluentes, todo conectado bajo tierra como el permafrost. Cada canción declara sus conexiones (ej. "→ salta a [Futhark], [Japón]"). Mecánica concreta de los puentes: por decidir (numeración + enlaces internos / data-puente).

**BONUS TRACK · UR ABISAL** (verificado Hammurabeltz):
- Fosa de las Marianas / Challenger Deep: punto más profundo del océano, ~11.000 m, presión >1.000 atmósferas, frío cercano a la congelación, oscuridad total.
- Zona HADAL = de Hades, dios del inframundo griego. Agua en el inframundo.
- CLAVE para la tesis: la vida abisal NO depende del sol sino del UR. Fumarolas/respiraderos hidrotermales ("chimeneas negras") liberan agua geotérmica + sulfuros; bacterias prosperan por QUIMIOSÍNTESIS (energía de compuestos químicos, sin luz solar). El reverso de la fotosíntesis: la vida brota del agua caliente y el azufre, no de la luz del amo.
- Guiño negro: hasta el abismo tiene huella humana (microplásticos y contaminantes en los organismos de la fosa). La T llega al fondo.
- Bestiario: pez baboso (Liparidae, hasta 8.000 m), barreleye (cabeza transparente), dragonfish bioluminiscente, xenophyophora (amebas gigantes), "nieve marina" (lluvia de materia orgánica). 
- → BONUS TRACK del libro (junto a cosmos, Antártida). Pendiente de redactar.

**DECISIONES FIJADAS esta vuelta:**
- UR DELTA / intuición → confirmado PREFACIO. Y SÍ PODAR la repetición hierro-60/EPICA + Bergson que comparte con la ESCOMBRERA (cuando se monte). "Podemos ya."
- LAS RUNAS → EUROPA (el Futhark es nórdico). Texto definitivo, pendiente de colocar en el andamiaje.
- Iberia continente: fundamento documentado (Hernández-Pacheco + Ian Gibson + argumento tectónico de los Pirineos). Profundizar.

**ANDAMIAJE:** se construye un esqueleto navegable de URTZ (índice maestro) con las 6 caras-continente + libreto + bonus como contenedores etiquetados, piezas móviles, listos para ir soltando textos. (Ver archivo de andamiaje.)

---

## 🎚️ CAMBIO · FUERA "CARA B" + SONIDOS DE LA CADENA ANALÓGICA

Quitado el rótulo "CARA B" de todas las piezas (obsoleto con la estructura de 6 caras-continente).
Cada CANCIÓN va ahora precedida por los sonidos que escupe la cadena analógica del vinilo, como ritual antes del tema:
**AGUJA krrk·fffsht · AMPLI hmmmmm · TOCATA tk·tk·tk · BAFLES bvvvm**
(monospace, gear en sepia #9a7a4a, sonido en gris #b8b8b8). Las onomatopeyas no llevan ur/ru: no tocan el verificador.

- ESCOMBRERA (Asia 3.1) y ANGOSTURA (América 4.1): llevan el bloque SONIDO + su subtítulo conservado.
- UR DELTA (Prefacio): solo se le quitó "CARA B" (es libreto, no canción; sin bloque de sonido).
- PENDIENTE/ABIERTO: el sonido es de momento el MISMO para las dos canciones. Si Luis quiere, cada canción puede tener su propio sonido distinto (crackle propio por tema). Por decidir.

---

## 🗺️ ARQUITECTURA DEFINITIVA DE LAS 6 CARAS · 36 CANCIONES (Joe Strummer: guía, no dogma)

Cada cara = continente. Cada canción = región aglutinante. La geografía es la cubeta; la cultura hídrica y los puentes Rayuela hacen el resto.

**CARA 1 · IBÉRICO** (el continente en miniatura):
Euskal Herria / Cantábrico / Atlántico / Mediterráneo / Central / Portugal

**CARA 2 · EUROPA** (el espejo del Futhark):
Escandinavia·Norte (LAS RUNAS, pendiente) / Islas Británicas·Atlántico Norte / Europa Central·Rin-Danubio / Mediterráneo Europeo·Grecia-Italia / Europa del Este·Balcanes-Cárpatos / Finlandia·Báltico (Turku, nodo boreal)

**CARA 3 · ASIA** (la escombrera del mundo):
Anatolia·Cáucaso (URARTÚ, qanat-71) / Mesopotamia·Levante (Sal/Zamzam/Sura, qanat-70) / Asia Central·Turán-Irán (Elburz/Luristán) / Asia del Sur·Indo-Ganges (Annapurna) / Asia del Este·Amur-Japón (Kurosawa/Ama-Lur, en index) / **Asia del Sureste·Mekong → MONTAÑA DE HUMO ● (pieza colocada)**

**CARA 4 · AMÉRICA** (del Orinoco al Amazonas):
Ártico americano·Inuit (Katajjaq/S-Iberia/Mantle, qanat-69) / América del Norte·Grandes Lagos-Misisipí / Mesoamérica·México-Caribe / **Orinoco·Amazonia → ANGOSTURA ● (pieza colocada)** / Andes·Pacífico / Cono Sur·Patagonia-Tierra del Fuego

**CARA 5 · ÁFRICA** (la cuna del agua):
Norte de África·Nilo-Sahara / África Occidental·Níger-Senegal (ruta trata, nexo Angostura) / **Cuenca del Congo → ITURI·la iturri congoleña·Leopoldo II·ébola (pendiente)** / África Oriental·Rift Valley-Grandes Lagos / Cuerno de África·Yemen (nexo Levante, qanat-70) / África del Sur·Kalahari-Cabo

**NORMA DE HUECOS (fijada 29 jul 2026):** en cuanto un hueco pasa a "● pieza colocada", se borra cualquier etiqueta de semilla que llevara pegada — nada de dejar el rastro de la idea original conviviendo con la pieza terminada. Blanco o negro, pendiente o colocado, sin estado intermedio ("media respuesta", "parcialmente cubierto") que Claude no debe inventar ni anotar. Claude no propone semillas nuevas por iniciativa propia: Luis genera de sobra por su cuenta: lo que hace falta es estructura para contenerlas (macetas), no más semillas. El permafrost es el contenedor de material en bruto; la arquitectura de las 6 Caras es solo el mapa de huecos, pendiente o colocado, nada más.

**CARA 6 · OCEANÍA** (el UR sin orilla):
Australia·interior árido / Nueva Guinea·Melanesia / Polinesia·el Pacífico como UR absoluto / Micronesia / Nueva Zelanda·Maorí / Antártida·el hielo primordial (flexible, puede migrar a bonus)

**NOTA STRUMMER:** El Sandinista es la guía, no el dogma. Oceanía puede perder canciones y redistribuir. Las regiones son cubetas orientativas; los puentes Rayuela declaran las conexiones reales entre continentes.

**UR CONDUCTOR:** cada cara tiene su hilo — la salinidad, la estrella de 8 puntas, el agua como poder colectivo. Los hilos se cruzan en los puentes.

**PIEZAS COLOCADAS:** ur-delta→Prefacio / escombrera→Asia(Mekong) / angostura→América(Orinoco).
**PENDIENTES DE ESCRIBIR:** todo lo demás. Runas→Europa(Escandinavia). ITURI→África(Congo).

---

## 📝 SESIÓN JULIO 2026 · ACTUALIZACIONES Y NUEVAS NORMAS

### ACTUALIZACIÓN · NORMA DE MARCADO (completa, secc. 2)

**Añadido en julio 2026:** La Ü/ü se suma a U/u para el marcado UR.
- Desde ahora: UR, Ur, ur, **Ür, ür** → todos en rojo.
- Norma permanente del proyecto, confirmada por Luis.
- Aplica a *Altzürükü* y cualquier topónimo con diéresis.
- Los títulos h3 se marcan igual que el cuerpo (ZUR**BELTZ** → el UR en el título).
- La T como categoría política se escribe entre comillas simples: 'T', no en cursiva ni negrita.

---

## 7 · NORMATIVA DE CURSIVAS

**Movida a NOTAS-PUNK.md (norma 16), 31 jul 2026.** Incluye la excepción fijada de UR sin cursiva, la tabla de qué va y qué no va en cursiva, y el orden de aplicación en HTML. Queda solo el registro histórico: 105 instancias corregidas en urtz.html el 18 de julio de 2026 al fijar la excepción de UR; la pieza Meseta/Central sirvió de modelo con 41 instancias `<em>` aplicadas ese mismo mes.

**Pendiente: aplicar la norma de cursivas (ver NOTAS-PUNK.md, norma 16) a las otras piezas ya montadas:**
- Xiberua: *Zamaltzain*, *Maskarada*, *Pastorala*, *Godalet Dantza*, *Gorriak/Urdinak*, *mozorro*, *Euritión* (nombre mitológico), *Sigurd* (nórdico), *Axeri Boda*, y el nombre de la ópera *El anillo del nibelungo*
- Vendée: *Sigurd*, *El anillo del nibelungo*, *Sigournais* (topónimo analizado), *Bourdin*
- Levante de la Sal: *qirbah*, *ghadir*, *Bahr al-Mayyit*, *Nahr al-Urdun*, *Police & Thieves* (canción), *Your House* (canción), *True Democracy* (álbum)
- Indo-Ganges: términos sánscritos cuando los haya
- Escombrera: nombres en khmer si los hay

---

## 8 · BLOQUE A LA MESA

**Regla movida a NOTAS-PUNK.md (norma 17), 31 jul 2026.** Posición (después del cuerpo, antes de la glosa) y criterio de contenido viven ahora solo ahí. Aquí queda el registro de qué piezas ya lo tienen:

**Mesas montadas:**

| Pieza | A la mesa |
|-------|-----------|
| Xiberua · Euskal Herria | Txakoli desde altura + Idiazabal de pastor suletino |
| Meseta Central | Migas + Valdepeñas + manchego |
| Vendée · Europa Latina | Muscadet sur lie + mogettes de Vendée |
| Levante de la Sal · Mesopotamia | Labneh + za'atar + pan de tabún + dátiles |
| El Gran Receptáculo Sónico · Indo-Ganges | Masala chai + dal + arroz del Ganges + ghee |
| Escombrera Sistémica · Mekong | Pho + nuoc mam + arroz glutinoso |
| UR, el Euskera y la Frontera Invisible | Irouléguy tinto + axoa de ternera al pimiento de Espelette |

**Pendientes (cuando se monten las piezas):**
- Atlántico / Portugal: pulpo à lagareiro + vinho verde
- Cantábrico: anchoas de Santoña + sidra asturiana / txakoli
- Europa Central (Alpes): raclette + Grüner Veltliner
- Japón / Asia del Este: sashimi de atún + sake junmai
- Azores / Furnas: caldeirada cocinada en fumarola

---

## 9 · ESTADO ACTUAL DE URTZ (julio 2026)

### Cara 1 · Ibérico — activa
```
[PREFACIO] LEC-T-UR-A · PALIMPSESTO IBÉRICO
● Euskal Herria     → Xiberua / Zurbeltz y el ritual de la máscara
● Central           → El Atlas UR de la Meseta (Del Rioja al Atlántico)
○ Cantábrico
○ Atlántico
○ Mediterráneo
○ Portugal
```

### Cara 2 · Europa
```
● Europa Latina · Francia-Italia-Grecia → El Escarpe de Altura y la Fosa del Fango (Vendée)
○ Escandinavia · Norte      [pendiente: LAS RUNAS]
○ Islas Británicas
○ Europa Central · Rin-Danubio
○ Europa del Este · Balcanes-Cárpatos
○ Finlandia · Báltico
```

### Cara 3 · Asia
```
● Mesopotamia · Levante         → El Levante de la Sal
● Asia del Sur · Indo-Ganges    → El Gran Receptáculo Sónico
● Asia del Sureste · Mekong     → La Escombrera Sistémica
○ Anatolia · Cáucaso
○ Asia Central · Turán-Irán
○ Asia del Este · Amur-Japón
```

### Cara 4 · América
```
● Orinoco · Amazonia            → Dolor, canto y muerte en el Orinoco
○ Ártico americano · Inuit
○ América del Norte
○ Mesoamérica
○ Andes · Pacífico
○ Cono Sur
```

### Cara 5 · África / Cara 6 · Oceanía
Todas vacías (○).

### Prefacio y Bonus
- Prefacio general (UR Delta): montado
- Prefacio Cara 1 Ibérico (Palimpsesto): montado

---

## 10 · ESTADO DEL PERMAFROST (julio 2026)

**73 qanats** en el muro glaciar (numeración inversa: qanat-72 en la cima, qanat--01 en el fondo).

**Qanats desactivados (incorporados a URTZ):**
- **Qanat-72** · Atlas UR de la Meseta (versión de datos) → desactivado, gris 50%, badge ✓ URTZ
- **Qanat-71** · T-UR-LEQUE · La torre mozárabe (versión conceptual) → desactivado, gris 50%

**Qanats activos de esta sesión (no desactivados todavía):**
- Qanat-01 a qanat-70: de sesiones anteriores, estado desconocido en esta sesión

**Norma de desactivación:** cuando el contenido de un qanat se incorpora a URTZ, cambiar el div del qanat en permafrost.html:
```html
<!-- de: -->
<div id="qanat-N" style="padding:clamp(2rem,5vw,4rem)...">
<!-- a: -->
<div id="qanat-N" style="padding:clamp(2rem,5vw,4rem)...; opacity:0.5; filter:grayscale(50%); border-left:4px solid #888;">
<div style="...color:#888;">&#10003; INCORPORADO A URTZ</div>
```

---

## 11B · MÉTODO DE INFORMES DE INVESTIGACIÓN (protocolo fijado 24 jul 2026)

**Origen**: Luis trabaja primero en Chrome (o herramienta de búsqueda IA equivalente), en conversación libre, siguiendo su intuición y su interés real. Pega esa conversación completa aquí. A partir de ahí, el protocolo es fijo:

1. **Chrome investiga y conversa** — Luis pega la conversación entera (sus preguntas + los desarrollos de la IA de búsqueda), sin recortar.
2. **Código Hammurabeltz** — Claudius verifica cada dato específico por separado: qué se confirma, qué se corrige (con el dato correcto al lado, no solo "está mal"), qué queda como intuición declarada sin base filológica real. Nunca se fuerza un UR donde no hay letra, ni se da por bueno un dato porque "suena bien".
3. **Informe con TODO el contenido narrativo** — no basta el veredicto condensado. Cada apartado debe llevar el desarrollo narrativo completo de la investigación: las preguntas exactas de Luis, el desarrollo de Chrome (reescrito por Claudius con sus propias palabras, nunca copiado literal — por derechos de autor y porque así se detectan mejor los fallos), sus propias mejoras si Claudius ve que aportan. **Nada de condensar en una frase bonita que cierre el tema** ("no ser Lorca"): pecar de largo y técnico, sin perder la elegancia de prosa que caracteriza el libro (pilares: The Clash, Marvin Gaye).
4. **Verificación aparte, no mezclada en el cuerpo** — un bloque diferenciado (tipo INDICADORES) con: confirmado / corregido con dato correcto / declarado como intuición. Así Perplexity o quien redacte después sabe qué pisa fuerte y qué es terreno blando.
5. **Rayuelas señaladas, no desarrolladas** — qué conecta con qué otra pieza ya existente del libro, solo apuntado.
6. **Propósito**: esto es una PLANTILLA MAESTRA para que Luis pegue directamente en Perplexity y redacte sin tener que releer la investigación entera cada vez ("mi memoria es de pez"). El objetivo es no perder ningún hilo narrativo por el camino, ni tener que preguntarle constantemente a Claudius qué se dejó fuera.
7. **Semillero** — durante la verificación puede aparecer material genuino pero que no pertenece a la pieza que se está trabajando (otra región, otra época). Se separa en una pestaña aparte llamada SEMILLERO, con nota de a qué otra pieza del mapa UR podría pertenecer en el futuro, sin desarrollar.
8. **Aplica retroactivamente** cuando Luis lo pida explícitamente para un informe ya montado en versión condensada.
9. **UR sin la letra, en cualquier materia** — verificar y coser en la narración, sin marcar aparte ni etiquetar como categoría especial, todo personaje, dios, río, mito, leyenda, música, política, culto, arqueología, arte o dato de prehistoria que sostenga la función del UR (origen, agua, resistencia, agradecimiento frente a usurpación) sin llevar la sílaba en su nombre. No hay materia menor para este libro: hay UR en la piedra y en el cosmos: sin UR no hay vida, sin vida no hay universo. Se gana el sitio por mérito propio, nunca por parecido fonético.
10. **Estándar de calidad de referencia, fijado con precisión el 27 jul 2026** — cuando Luis dice "no te dejes nada" y "todo es todo", es literal, no retórico: cubrir el cien por cien de lo investigado (dioses, guerras, mitos, música, topónimos, pueblos UR, ríos — todo lo que aparezca, sin criterio de selección propio salvo el Hammurabeltz). El **Informe Maestro · AMUR · MANCHURIA** (27 jul 2026) queda fijado como pieza de referencia nombrada — la vara con la que medir si un informe futuro está a la altura o se queda corto. Sus siete rasgos exactos, en las palabras de Luis:
    - **Profundidad de cada punto**: mucho más desarrollo por tema del que parece razonable a primera vista; nunca un párrafo de resumen cuando la investigación da para tres.
    - **Tono**: menos veredicto técnico, más relato — y aun así sin perder rigor. Verificar no es sinónimo de sonar a informe universitario.
    - **Ningún cabo suelto**: ni el más pequeño dato, personaje o hilo de la investigación original queda fuera. Si algo no cabe en el cuerpo, va a la glosa o al semillero — nunca se descarta en silencio.
    - **Convivencia sin robo de aire**: verificación y narración conviven en el mismo informe sin que una le quite espacio o energía a la otra — la prosa no se vuelve acta, y la verificación no se vuelve nota al margen perdida.
    - **Código Hammurabeltz**: aplicado siempre, sin excepción, con el dato correcto al lado del error, nunca solo "esto está mal".
    - **Aportes de investigación propios de Claudius**: buscar por cuenta propia más allá de lo que trajo la conversación original, cuando hay indicio de que puede haber más — insistiendo en esto, sale bien.
    - **Detalles pequeños que marcan la diferencia de cada capítulo**: lo que no es dato ni verificación ni narración pura, sino el hallazgo que solo aparece si de verdad se ha leído todo con calma — el nombre de tapadera de un crimen que lleva la palabra "agua", el cambio de nombre de un río para borrar una rebelión, ese tipo de cosa.
    
    Luis no opinará sobre asuntos que no entiende o que no le conciernen — el criterio de "todo es todo" se aplica a la investigación y a los hechos verificables, no a la interpretación técnica de cuestiones ajenas al libro.
11. **Confirmación breve, no interrogatorio (fijado 27 jul 2026)** — antes de intervenir en el HTML cuando hay ambigüedad real sobre el alcance del cambio, Claude confirma en una frase su entendimiento de la tarea y pregunta si es correcto, en vez de lanzarse a adivinar o de encadenar varias preguntas. Una sola confirmación, no una serie. Si la tarea ya está clara por contexto o por precedente en la propia sesión (p. ej. "esto es una mejora del texto que ya tenemos, ata tú la glosa y los indicadores como siempre"), no se pregunta: se ejecuta directamente, sin pedir permiso por algo que ya es norma establecida.
12. **Ubicación fija de los Informes Maestro (fijado con precisión el 28 jul 2026, tras fallo real de colocación)** — un Informe Maestro va **siempre al final de urtz.html**, sin excepción, independientemente de a qué sección del libro pertenecerá la pieza definitiva que se construya a partir de él. No importa si la pieza futura será de introducción, de Cara 1, 2, 3, 4, 5 o 6: mientras el contenido siga en formato "informe" (verificación Hammurabeltz separada, sin glosa ni notas numeradas todavía), se aparca al fondo del documento. Solo cuando se convierte en pieza definitiva narrativa (con notas, glosa e indicadores) se traslada a su sitio regional o temático correspondiente. Esta regla ya se aplicaba como práctica desde el Informe Maestro de Darién/Urabá, pero nunca había quedado escrita — el fallo de aplicarla mal una vez (Informe Maestro de Río Congo, colocado por error en la introducción) confirmó que hacía falta dejarla fijada aquí, no solo en la memoria de la sesión.

---

## 11 · NORMA GLOSA EN URTZ

**Movida a NOTAS-PUNK.md (norma 18), 31 jul 2026.** El tope de "máximo 2 líneas por entrada" queda derogado ese mismo día — sustituido por un criterio de calidad (cada frase aporta un dato que el cuerpo no tiene), ya que la norma 9 del manifiesto asigna a la glosa el peso completo de la erudición del capítulo.

---

*Actualización: julio 2026. La norma de cursivas queda fijada con la pieza Meseta como modelo. Ag-UR.*
*Enmienda: 18 julio 2026. UR queda excluido de la cursiva por decisión de Luis (ver excepción fijada arriba). El resto de la normativa de la sección 7 sigue vigente sin cambios.*


## MAPA DE RAYUELAS VIVO (iniciado 30 jul 2026)

Tabla de vínculos entre piezas, actualizada cada vez que se coloca o toca una pieza — para no tener que reconstruir el mapa entero cuando el libro esté completo. Sustituye a las cajas RAYUELAS de los indicadores de trabajo (retirados de urtz.html en esta misma sesión; el contenido vive aquí, no se pierde).

**Piezas sin rayuela registrada todavía** (4): XIBERUA - ZUBEROA - ZURBELTZ Y EL RITUAL DE LA MÁSCARA, EL GRAN RECEPTÁCULO SÓNICO: EL INDO-GANGES Y LA CORONA DEL HIMALAYA, MONTAÑA DE HUMO: ESCOMBRERA HUMANA, DOLOR, CANTO Y MUERTE EN EL ORINOCO.

| Pieza | Rayuelas → |
|---|---|
| INTRODUCCIÓN: CÍRCULO SIMBÓLICO — NATURA, UR Y ORIGEN | → EL UR DELTA (bisagra directa: la intuición como método se anuncia aquí y se desarrolla allí) · → CUL-T-UR/A · LEC-T-UR/A (la cultura como contenedor retoma el UR-Sapiens de esta pieza) · → Urdax/Zugarramurdi (pendiente de montar — la lengua aislada y su relación con lo no verificable es el mismo nervio). |
| UR DELTA: TEOLOGÍA DE LA INTUICIÓN, HUÉRFANA DE DOCTRINA | → Escombrera / Asia (comparten el párrafo del hierro-60/EPICA y a Bergson — ver nota en MEJORA) · → Urdax/Zugarramurdi (pendiente de montar — la intuición mística frente al registro inquisitorial es el mismo choque que aquí entre intuición y T) · → ANGOSTURA (Bolívar y la piedra, otra imagen de umbral cósmico-político). |
| EL UR CÓSMICO · DEL HIELO INTERESTELAR A LA GARGANTA | → EL UR DELTA (la Nebulosa Boomerang y esta pieza comparten registro cósmico, una fría e inmóvil, la otra cálida y en viaje) · → KOXKERO (Ekain reaparece allí con su propia glosa; aquí se cita en clave cosmológica, allí en clave etnográfica —dos lecturas del mismo lugar) · → CUL-T-UR/A (el cierre sobre la usurpación enlaza directo con la T como compuerta que abre esa pieza) · → EPÍLOGO / Wittfogel y Mumford (la usurpación del UR libre en UR-be es la misma arquitectura de poder hidráulico). |
| RÍO CONGO: NATURALEZA O SISTEMA | → EL UR DELTA (Sandinista! como modelo estructural del libro entero) · → KOXKERO (Ekain reaparece aquí en clave filosófica de Chesterton, allí en clave etnográfica) · → UR, EL EUSKERA (la lengua aislada como confinamiento conceptual, mismo argumento). |
| CUL-T-UR/A · LEC-T-UR/A | → Mediterráneo Ibérico / Cabo de Gata (el mismo eje sur-bético, Tarteso y el Estrecho como frontera) · → Angostura (Huelva-Odiel y Orinoco comparten la lógica del estur convertido en frontera y en tributo) · → Meseta Central (la columna que asciende desde el sur hasta el norte vasco, mencionada explícitamente en el propio texto). |
| UR, EL EUSKERA Y LA FRONTERA INVISIBLE | → Vendée / Francia Atlántica (mismo aparato revolucionario que Bar&egrave;re: la Francia que se come sus propias lenguas y su propio interior) · → Mediterráneo Ibérico / Cabo de Gata (el paralelismo explícito del balate alpujarreño ya está en la propia glosa) · → Euskal Herria (contigua, continuidad regional directa) · → América · ANIA (eco lejano: otra diáspora vasca, otro siglo, la lengua viajando en vez de resistiendo en el sitio). |
| UR, EL CASTELLANO Y LA FRONTERA INVISIBLE | → Meseta Central (del Rioja al Atlántico · UR viajero: mismo eje de expansión hacia el oeste) · → Euskal Herria (la última frase lo declara sin rodeos: «el UR de los vascos no está solo») · → Cantábrico (pendiente de escribir — costa que recibe el romance en su extremo norte) · → Atlántico (pendiente de escribir — la salida ultramarina que Nebrija ya anuncia). |
| EL KOXKERO ERRANTE DE BAJA ALCURNIA | → UR, EL EUSKERA (contigua, mismo marcador regional) · → ZUBEROA (comparten a Urbeltz, folclorista) · → EL UR DELTA (la cueva de Ekain conecta con la Nebulosa Boomerang vía Nietzsche/Ekain en el epílogo: «Dios murió en Ekain») · → Cantábrico (pendiente de escribir — el molino y la ferrería de Agorregi son la misma T extractivista que las minas de Ollin). |
| AMAIA · AMAIUR · MAIA · AMAYA: EL CONFÍN | → KOXKERO (contigua, comparten las lamiak y el sistema kárstico de Urdax/Ikaburu) · → ANGOSTURA (los cenotes mayas y el Orinoco comparten la lógica del agua subterránea como centro del mundo) · → UR, EL CASTELLANO (la Gran Redada es la misma T institucional que persigue al gallego o al euskera, aplicada a un pueblo entero) · → ZUBEROA (contigua, Akelarre y máscara comparten territorio ritual). |
| XIBERUA - ZUBEROA - ZURBELTZ Y EL RITUAL DE LA MÁSCARA | — (sin rayuelas registradas) |
| REFUGIO PUNK EN EL DESIERTO | → EL EUSKERA (Barère y la Francia jacobina comparten método con cualquier centro que folkloriza el margen, aunque aquí el margen elige irse por gusto, no por represión) · → EL UR DELTA (Sandinista! y The Clash como modelo estructural explícito del libro entero, Strummer aparece en ambas piezas) · → EPÍLOGO / Town Called Malice (mismo Strummer, mismo gesto: elegir el margen como lugar de verdad). |
| EL ATLAS UR DE LA MESETA | → UR, EL CASTELLANO (Alfonso X y Nebrija recorren la misma Meseta que este viaje hidronímico) · → CUL-T-UR/A · LEC-T-UR/A (Tarteso y el Estrecho como la otra gran puerta ibérica, en el extremo sur de esta misma columna) · → MESOPOTAMIA / LEVANTE (el Abzu sumerio y los Ojos del Guadiana son la misma imagen del agua que emerge del subsuelo) · → ANGOSTURA (Urius desemboca en Huelva justo donde Colón zarpó en 1492; el Orinoco recibe otra desembocadura, otro imperio). |
| EL ESCARPE DE ALTURA Y LA FOSA DEL FANGO | → EL EUSKERA (mismo aparato revolucionario/estatal que Barère, aplicado aquí al paisaje en vez de a la lengua) · → MESOPOTAMIA/LEVANTE (el escarpe y la fosa son la misma dualidad altura-refugio/bajo-peligro que estructura esa pieza) · → ANIA (otra figura de umbral entre dos aguas, Ripley y Ania comparten el gesto de descender sin perder la memoria de la altura). |
| FRONTERA AQUITANO-CELTA: GUERRA EN LA GALIA | → UR, EL EUSKERA Y LA FRONTERA INVISIBLE (misma frontera de contacto y resistencia lingüística, otro ángulo) · → Frontera Franco-Belga/Dunkerque (misma investigación de origen, hermana geográfica) · → EL UR DELTA (la T que acaba encontrando otra T distinta). |
| FRONTERA FRANCO-BELGA: RÊV-E-UR · SOÑADOR · ESPEJISMO | → UR, EL EUSKERA (mismo tipo de refugio de frontera, otra geografía) · → VENDÉE / EL ESCARPE Y LA FOSA (mismo eje francés, altura/roca frente a fango/carencia) · → Etimología Insurgente / Absurdo-Susurro (parentesco temático de raíces sonoras inciertas, aunque *swer- y resver son familias distintas —no confundir). |
| FRONTERA FRANCO-BELGA: DUNKERQUE · URBELTZ CELTA | → FRONTERA FRANCO-BELGA: RÊV-E-UR · SOÑADOR · ESPEJISMO (misma franja fronteriza, otro eje narrativo) · → UR ABISAL (la usurpación que llega hasta el fondo más remoto, aquí en Tourcoing) · → Urabá (la Madre de las Aguas, mismo arquetipo sin contacto documentado con el Nikker europeo). |
| EL LEVANTE DE LA SAL | → Iberia (Elgorriaga/Salinas/Keuper · Hermón=Urbasa) · → Ártico (burro/qirbah: el cuerpo como instrumento) · → Urinoco(angostura/Venturi) · → África/Yemen (llamada-respuesta y rogativas). |
| EL GRAN RECEPTÁCULO SÓNICO: EL INDO-GANGES Y LA CORONA DEL HIMALAYA | — (sin rayuelas registradas) |
| MONTAÑA DE HUMO: ESCOMBRERA HUMANA | — (sin rayuelas registradas) |
| ANIA · ANAIA · UR EN EL ATLÁNTICO FRÍO | → Euskal Herria (el origen de los balleneros; sin esa pieza ésta no se sostiene) · → Cantábrico (pendiente de escribir — el puerto de salida, Pasaia/Getaria, antes de cruzar) · → Ártico · Islandia (Spánverjavígin 1615, la matanza y la reconciliación de 2015, mismo frío que Groenlandia/Katajjaq) · → América del Norte · Grandes Lagos-Misisipí (el hacha de Mantle viaja aguas arriba desde aquí hasta allá). |
| URABÁ · TAPÓN DE DARIÉN · RAÍCES INDÍGENAS | → Etimología Insurgente/TURBA (misma raíz turbare, mismo verbo en boca de Panquiaco) · → UR ABISAL (la usurpación que llega hasta el fondo más remoto, aquí el oro que nunca se encuentra) · → Frontera Franco-Belga/Dunkerque (mismo arquetipo de deidad acuática —Madre de Aguas/Nikker— en dos continentes sin contacto) · → Ken Saro-Wiwa/Resistencias Hídricas (mismo canto de resistencia frente a la violencia sistémica, aquí los alabaos). |
| DOLOR, CANTO Y MUERTE EN EL ORINOCO | — (sin rayuelas registradas) |
| SÁJAURA · MAURITANIA · FUR | → UR ABISAL (agua persistiendo donde todo empuja al derrumbe) · → Ken Saro-Wiwa/Resistencias Hídricas (agua como eje de conflicto y resistencia en África) · → Frontera Franco-Belga/Beausonge y Bojayá/alabaos (mismo patrón de música de resistencia surgida del mestizaje). |
| ABSURDO | → Susurro (misma raíz *swer-, dos ramas del mismo zumbido: una se pierde, la otra apenas se oye). |
| SUSURRO | → Absurdo (misma raíz *swer-) · → UR, EL CASTELLANO (Fernando de Rojas y la lengua en los márgenes del poder). |
| TURBA | → URABÁ (Panquiaco, Turbo, el mismo verbo en su contexto histórico completo) · → UR ABISAL (mismo método: raíz real pero de origen incierto, resonancia sin genealogía cerrada). |
| HURÓN | → LAUREL · SAN LORENZO · SHARP (hermana natural: mismo gesto de insulto colonial vuelto bandera, misma década punk) · → ANIA (Wendat, colonización franco-americana, mismo territorio). |
| LAUREL | → HURÓN (hermana natural: mismo gesto de insulto colonial vuelto bandera, misma década punk) · → ANIA (Wendat, colonización franco-americana, mismo territorio) · → EL UR DELTA (Barère y la lengua única: mismo gesto de borrado por nombramiento) · → FRONTERA FRANCO-BELGA (misma familia de resignificación de símbolos usurpados). |
| SULFURO Y OSCURIDAD: EL UR ABISAL | → UDRA ES UR (mismo método: Kurosawa/Urbeltz, resonancia sin genealogía) · → Etimología Insurgente / Turba (mismo patrón: raíz real pero de origen incierto) · → EL UR DELTA (la T que llega hasta el fondo más remoto del planeta). |


---

## 12 · CRITERIO DE CONTINUIDAD EDITORIAL Y PROMPT MAESTRO

*(trasladado y actualizado desde NOTAS-UR-SAPIENS.md §19-20, 31 jul 2026 — allí quedaba descrito para dos capas de salida y un solo cuaderno; aquí se actualiza a los tres archivos reales del proyecto)*

Cuando una conversación avance durante varios días o el hilo empiece a cargar, conviene consolidar el trabajo en una versión de continuidad. Si el dispositivo o hilo principal funciona bien, puede seguirse ahí; si se vuelve pesado, lo más práctico es abrir una conversación nueva con el prompt maestro de abajo, que recupera el marco completo sin perder la línea de trabajo. La conversación nueva no debe sentirse como un reinicio, sino como un traslado de taller.

**Señales de cambio:** el hilo se vuelve lento o pesado · hace falta recuperar contexto una y otra vez · hay demasiados bloques abiertos y el seguimiento se dispersa · se necesita separar redacción, revisión y reordenación conceptual.

**Los tres archivos y qué gobierna cada uno:**
- **`urtz.html`** — el libro mismo. La única fuente de verdad sobre qué está escrito.
- **`NOTAS-PUNK.md`** — manual único de redacción: cómo suena una frase, cómo se marca el UR, cursivas, A LA MESA, la glosa, los tres registros (hecho / especulación / dadá), todo lo que responde a "¿cómo se escribe esto?".
- **`NOTAS-URTZ.md`** (este archivo) — arquitectura y flujo de trabajo: Ley Hammurabeltz, ubicación de informes maestros, mapa de rayuelas, estado de cada Cara, piezas colocadas, todo lo que responde a "¿dónde va esto y en qué estado está?".

### Prompt maestro de arranque

> Quiero seguir trabajando el proyecto UR-SAPIENS / Urtz con la misma dinámica editorial que ya hemos desarrollado. El libro vive en `urtz.html`; el criterio de redacción (marcado UR, cursivas, A LA MESA, glosa, los tres registros hecho/especulación/dadá, y las normas punk de estilo) vive en `NOTAS-PUNK.md`; la arquitectura, el flujo de trabajo y el estado de cada pieza viven en `NOTAS-URTZ.md`. Mantén como marco: UR como núcleo poético-conceptual, el sistema UR/T, la mezcla de rigor y descabello, y la Ley Hammurabeltz (Claudius verifica datos y fechas, sin coba, método comanche). Antes de sustituir cualquier pieza, compara siempre contra lo que ya hay en el archivo y muestra la comparativa antes de tocar nada. Prioriza ritmo, legibilidad, cadencia literaria y precisión conceptual. Evita simplificaciones históricas, repeticiones mecánicas, tono dogmático, moralina y explicaciones redundantes. Si te doy un fragmento para sustituir, compáralo con lo que ya existe, señala qué cambia y por qué, verifica cualquier dato nuevo de forma independiente, y respeta el tono humano, insurgente y musical del libro. Cuando haya decisiones abiertas, propón la opción más sólida sin alargar innecesariamente la discusión, pero nunca sustituyas nada sin confirmación explícita.

### Qué mantener al cambiar de conversación
El núcleo conceptual UR-SAPIENS · el equilibrio entre rigor y descabello · la preferencia por cadencia literaria frente a explicación redundante · la reserva de los bloques que aún no tienen lugar definitivo · la forma de trabajar por capas, no solo por corrección puntual · las piezas marcadas con calavera (NO TOCAR salvo petición explícita con "abre calavera").
