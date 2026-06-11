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
