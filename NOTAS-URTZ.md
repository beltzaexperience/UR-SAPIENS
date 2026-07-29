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

## 2 · NORMA DE MARCADO (mismo método que el ALFABETO UR / Alpha-UR)

Urtz NO usa la maquinaria de guiones de los qanats. Usa la **forma natural del Alfabeto UR**:

- **SIN GUIONES** que partan palabras. Nada de US-UR-PACIÓN, UR-Sapiens, BAS-UR-Sapiens. Se escribe en forma natural: *usurpación, Ursapiens, Basursapiens, Urlañó, sistemas mundo*.
- **UR en MAYÚSCULA solo cuando va como UNIDAD** (el UR-agua suelto, el fonema-concepto): «el ciclo del **UR**», «**UR** + E=mc² = SAPIENS».
- **Dentro de las palabras, ur en MINÚSCULA roja**, forma natural con primera mayúscula de la palabra: **Ur**tz, **Ur**tzi, **Ur**lañó, **Ur**sapiens, Bas**ur**sapiens, us**ur**pación, capt**ur**a, m**ur**o.
- Span rojo estándar: `<span style="color:#b01a1a;">ur</span>` (minúscula) o `...">UR</span>` (unidad).
- Reglas heredadas que siguen vigentes: solo u+r consecutivas REALES en rojo; RU rojo solo si es espejo deliberado; nombres propios con UR real sí se marcan; método comanche (nada por descartado, todo por contrastar); cazar UR falsos inventados (incl. los propios de Claudius).

---

## 3 · ESTÉTICA Y ESTRUCTURA (estado actual de urtz.html)

- **Fondo**: pergamino (mismo background flickr que el permafrost: `55167948157_ee65a87707_o.jpg`, repeat-y), texto oscuro (#1a1a1a / #222), nota/secundario #666.
- **Cabecera**: banda roja #b01a1a, logo «ᚢ **Ur**tz» (Ur en negro #0a0a0a, forma natural), subtítulo «RUNA DEL CIELO · EL TRUENO QUE GUARDA EL UR · SOLO PARA EL ZAHORÍ».
- **Título de cámara**: tamaño títulos UR-book → `font-family:'Bebas Neue',Impact,'Arial Narrow',sans-serif; font-size:clamp(2rem,5vw,5rem); line-height:0.9; letter-spacing:0.02em; color:#1a1a1a`.
- **Contenedor**: `max-width:900px; margin:0 auto`.
- Divisor de sección: `<div style="height:4px; background:#b01a1a; width:100%;">`.
- La «Nota de método» inicial fue ELIMINADA por decisión de Luis (la cámara entra directa).

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

## 7 · NORMATIVA DE CURSIVAS (norma definitiva, julio 2026)

Establecida a partir del criterio de Perplexity + revisión de Claudius. Rige para todo el libro.

### Qué va en cursiva

**EXCEPCIÓN FIJADA (agosto 2026, decisión de Luis, prevalece sobre el criterio de Perplexity):** UR como concepto/protagonista **NO va en cursiva**. Se queda derecho, solo con el marcado rojo (`<span style="color:#b01a1a;">UR</span>`, sin `<em>`). El consejo original de Perplexity era cursiva; Luis lo revoca por decisión propia — el rojo ya cumple la función de distinguir la palabra, y es la palabra más repetida de todo el libro: doblar cursiva sobre el color más veces que cualquier otro término del texto rompe la propia convención tipográfica de la cursiva (marca de excepción, no de estribillo). Cualquier Claudius futuro debe respetar esto a rajatabla salvo que Luis mismo lo revierta con nuevo razonamiento ortográfico. 105 instancias corregidas en urtz.html el 18 de julio de 2026.

| Categoría | Ejemplos | Criterio |
|-----------|----------|----------|
| Extranjerismos antiguos y mitológicos | *Abzu*, *Ain*, *Zamzam* | Términos de lenguas antiguas con valor histórico, ritual o simbólico no integrados en el español actual |
| Latinismos y nombres científicos | *Durius*, *urus* | Formas latinas o denominaciones zoológicas que conservan su forma original |
| Términos en euskera u otras lenguas peninsulares | *Iturza*, *Laminiturri*, *jauregi*, *Zamaltzain*, *Maskarada*, *Pastorala*, *Godalet Dantza* | Cuando designan realidades específicas analizadas en el libro |
| Títulos de documentos históricos, leyes, mapas | *Génesis de Eridu*, *Código de Ur-Nammu*, *mapa de Nippur* | Nombres singulares de textos, leyes o cartografías con identidad propia |
| Títulos de obras artísticas | *El anillo del nibelungo*, *Alien*, *True Democracy* | Películas, óperas, álbumes |
| Formas musicales o folclóricas como categoría | *La Manchega* | Géneros o palos cuando se usan como categoría analítica |

### Qué NO va en cursiva

- **Topónimos actuales de uso normal:** Ojacastro, Toledo, Las Hurdes, Mesopotamia, Roma
- **Nombres propios de personas:** Schulten, Segoviano, Sansinenea, Zurbarán
- **La T como categoría política:** usar comillas simples 'T' — `su antagonista es la 'T': la 'T' que mide, tasa...`
- **Términos de la glosa en posición de cabecera:** la glosa usa negrita para los headwords; no añadir cursiva encima

### Orden de procesamiento en HTML

1. Aplicar `<em>` a los términos (en texto plano, antes de codificar)
2. Codificar entidades HTML (á → `&aacute;`, etc.)
3. Aplicar marcado UR en rojo (`<span style="color:#b01a1a;">`)
4. El resultado: `<em><span style="color:#b01a1a;">UR</span></em>` (cursiva + rojo simultáneos)

### Modelo de aplicación (Meseta, julio 2026)
La pieza Central/Meseta ha sido normalizada como modelo. 41 instancias `<em>` aplicadas:
- *UR* standalone como concepto (~15 instancias)
- *Abzu* ×5, *Durius* ×1, *URIUS* ×1, *urus* ×2
- *Ain*, *Zamzam*, *Iturza*, *Laminiturri*, *jauregi*, *La Manchega*
- *Génesis de Eridu*, *Código de Ur-Nammu*, *mapa de Nippur*
- 'T' con comillas simples en el párrafo del antagonista

### Pendiente: aplicar la misma norma a las otras piezas ya montadas
- Xiberua: *Zamaltzain*, *Maskarada*, *Pastorala*, *Godalet Dantza*, *Gorriak/Urdinak*, *mozorro*, *Euritión* (nombre mitológico), *Sigurd* (nórdico), *Axeri Boda*, y el nombre de la ópera *El anillo del nibelungo*
- Vendée: *Sigurd*, *El anillo del nibelungo*, *Sigournais* (topónimo analizado), *Bourdin*
- Levante de la Sal: *qirbah*, *ghadir*, *Bahr al-Mayyit*, *Nahr al-Urdun*, *Police & Thieves* (canción), *Your House* (canción), *True Democracy* (álbum)
- Indo-Ganges: términos sánscritos cuando los haya
- Escombrera: nombres en khmer si los hay

---

## 8 · BLOQUE A LA MESA (norma definitiva, julio 2026)

Cada pieza de URTZ lleva un bloque gastronómico entre el cuerpo y la glosa.

**Posición:** después del último párrafo del cuerpo, antes del `<div>` de la GLOSA.

**Formato visual:**
```html
<div style="border-top:1px solid rgba(176,26,26,0.15); margin-top:2rem; padding:1.2rem 0 0.8rem 0;">
  <div style="font-family:'Bebas Neue'...; color:#b01a1a;">A LA MESA</div>
  <p style="font-family:'Courier Prime'...; color:#444; font-size:0.95rem;">...</p>
</div>
```

**Criterio de contenido:**
- 3-5 frases de prosa, no lista de ingredientes ni receta
- El alimento como otra expresión del UR en el territorio (no decoración)
- El vino, la leche, el grano, el aceite como formas del agua transformada
- Tono sofá y copa de vino, no enciclopédico
- Sin juegos de palabras forzados (es parte del cuerpo narrativo, no del UR-book WEB)

**Mesas montadas:**

| Pieza | A la mesa |
|-------|-----------|
| Xiberua · Euskal Herria | Txakoli desde altura + Idiazabal de pastor suletino |
| Meseta Central | Migas + Valdepeñas + manchego |
| Vendée · Europa Latina | Muscadet sur lie + mogettes de Vendée |
| Levante de la Sal · Mesopotamia | Labneh + za'atar + pan de tabún + dátiles |
| El Gran Receptáculo Sónico · Indo-Ganges | Masala chai + dal + arroz del Ganges + ghee |
| Escombrera Sistémica · Mekong | Pho + nuoc mam + arroz glutinoso |

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

## 11 · NORMA GLOSA EN URTZ (distinción del UR-book WEB)

La glosa de URTZ usa formato limpio de diccionario operativo. **Sin** juegos de palabras tipo "GLOSA-UR-IO" (eso es estilo UR-book WEB). En URTZ:

```html
GLOSA · [NOMBRE DE LA PIEZA]
```

Las entradas son breves, precisas, sin redundar con el cuerpo. Máximo 2 líneas por entrada. Los headwords van en `<strong>`, sin cursiva añadida (la jerarquía tipográfica ya es suficiente). El marcado UR rojo sí aplica dentro de las definiciones.

---

*Actualización: julio 2026. La norma de cursivas queda fijada con la pieza Meseta como modelo. Ag-UR.*
*Enmienda: 18 julio 2026. UR queda excluido de la cursiva por decisión de Luis (ver excepción fijada arriba). El resto de la normativa de la sección 7 sigue vigente sin cambios.*
