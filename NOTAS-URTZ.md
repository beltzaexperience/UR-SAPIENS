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
### ✅ Cap.2 · CARA B: LA ESCOMBRERA SISTÉMICA — "LOS ESCOMBROS QUE SOSTIENEN EL EDIFICIO"
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
