# LINEA-EDITORIAL-REFERENTES — UR frente a Baroja, Orwell y Martín Santos

**Estado: PROPUESTA del 08/10/26. Nada de lo que sigue está aplicado en `urtz.html` ni en `NORMA-METODO.md`.** Cada cambio de norma es decisión de Luis (§10). Este documento responde al encargo del 08/10/26: repetir con las siete obras subidas al repositorio el trabajo que se hizo con el texto de Baroja sobre San Sebastián (Norma 36.8), para cerrar la línea editorial del manuscrito y perfilar las Normas-Método definitivas, teniendo en cuenta la anomalía rupestre que representa UR.

---

## 0. Resumen

1. **Corpus.** Siete obras, 482.162 palabras, 380.069 de narración (sin diálogo), 175 trozos de unas 2.000 palabras. El **corredor** (rango p10–p90 de los trozos) se calcula con las seis obras de Baroja y Orwell (140 trozos). Martín Santos se mide aparte, como pico y no como línea.
2. **El trabajo anterior se sostiene.** Los seis indicadores medidos en 653 palabras de Baroja sobre San Sebastián caen dentro del corredor de las seis obras. El anclaje (29 %) queda por debajo del de las novelas de Baroja (42–50 %) y al nivel del de Orwell (26 %), como corresponde a una crónica de viaje.
3. **UR se parece al canon en casi todo y se separa en cuatro rasgos, que forman su firma:** apertura de frase por artículo (50 % de las frases frente a 18 %), dos puntos (9,5 por mil palabras frente a 2,6), abstracción (4,4 por cien palabras frente a 1,9) y racha de aperturas con artículo (34 % frente a 13 %). Los otros 13 indicadores comparados quedan a 1,6 desviaciones o menos del canon. Sin esos cuatro, UR está a 0,9–1,3 de cada obra del canon; entre las propias obras del canon la distancia va de 0,55 a 1,24 (media 0,83). UR queda en el borde alto de esa variación y no fuera de ella. **38 de las 66 piezas de URS superan el p90 del canon en los cuatro rasgos; 58 lo superan en tres o más.**
4. **Un segundo grupo, menor y constante, apunta a una sintaxis troceada:** menos gerundios (14 frente a 49 por 10.000; 48 piezas bajo el p10 del canon), menos frases largas (1,4 % de las frases pasa de 40 palabras frente a 5,8 %; 41 piezas bajo el p10) y menos adverbios en -mente (1,7 frente a 4,7 por mil). El techo de frase de UR está en 29 palabras (p90); en el canon, en 35.
5. **Lo que el canon avala sin cambios:** enumeraciones (12,8 % frente a 12,7 %), frases cortas (19 % frente a 17 %), anclaje (32 % frente a 36 %), «y», punto y coma, cierres aforísticos (2,5 % de los párrafos frente a 1,9–5,8 %) y el techo del 10 % de párrafos cortos de la Norma 26 (Orwell: 0–13 %).
6. **La exposición teórica del canon tiene la textura opuesta a la de las piezas teóricas de UR.** Los pasajes expositivos largos del corpus (el «libro» de Goldstein y el apéndice del neolengua en *1984*, los capítulos más políticos de *Homenaje a Cataluña*) tienen frases con desviación 13–16, un 10–14 % de frases de más de 40 palabras, párrafos de 167–362 palabras, artículo inicial 22–27 %, abstracción 3,5–4,5 y 1–3 dos puntos por mil. Las nueve piezas teóricas de UR: desviación 6–9, 0–3 % de frases largas, artículo inicial 46–74 %, abstracción 5,6–9,4, dos puntos 5–10 por mil.
7. **Línea editorial propuesta (§8):** crónica de campo con tesis; suelo de prosa de ventana (Orwell) con el ojo suelto de Baroja; pico licenciado (Martín Santos); anomalía declarada y fuera del corredor. El corredor mide la distancia al suelo llano y no mide calidad: ninguna cifra autoriza un cambio que rebaje la densidad mitopoética (Norma 48).
8. **Nueve decisiones para Luis (§10).** Las tres de más evidencia: apertura de frase, dos puntos y suelo de gerundios.

---

## 1. Corpus y método

### 1.1 El corpus

| Clave | Obra | Palabras | Narración (sin diálogo) | Diálogo | Trozos | Papel |
|---|---|---:|---:|---:|---:|---|
| `baroja_aurora` | Pío Baroja, *Aurora roja* | 69.090 | 35.792 | 48 % | 17 | corredor |
| `baroja_arbol` | Pío Baroja, *El árbol de la ciencia* | 63.419 | 42.484 | 33 % | 21 | corredor |
| `baroja_zalacain` | Pío Baroja, *Zalacaín el aventurero* | 44.611 | 32.546 | 27 % | 16 | corredor |
| `orwell_1984` | George Orwell, *1984* (trad.) | 109.271 | 87.790 | 20 % | 40 | corredor |
| `orwell_cataluna` | George Orwell, *Homenaje a Cataluña* (trad.) | 78.161 | 75.865 | 3 % | 34 | corredor |
| `orwell_granja` | George Orwell, *Rebelión en la granja* (trad.) | 28.886 | 25.481 | 12 % | 12 | corredor |
| `martin_santos` | Luis Martín-Santos, *Tiempo de silencio* | 88.724 | 80.111 | 10 % | 35 | pico (aparte) |
| | **Total** | **482.162** | **380.069** | | **175** | |

Los siete PDF están en `origin/main` (nombres: `B- BAROJA - AURORA ROJA.pdf`, `B- BAROJA - EL ARBOL DE LA CIENCIA.pdf`, `B- BAROJA - ZALACAIN EL AVENTURERO.pdf`, `B- ORWELL - 1984 .pdf`, `B- ORWELL - HOMANJE A CATALUÑA.pdf`, `B- ORWELL - REBELION EN LA GRANJA .pdf`, `B- TIEMPO DE SILENCIO - MARTÍN SANTOS.pdf`). No se copian a esta rama ni se convierten en texto dentro del repositorio.

### 1.2 Método

1. `pdftotext` (sin `-layout`), reconstrucción de párrafos (línea corta que acaba en puntuación final = fin de párrafo; cabeceras y números de página repetidos se descartan; los guiones de corte se unen).
2. Se separan los párrafos de diálogo (raya o comillas angulares iniciales; en *Aurora roja* el guion simple) y se mide **solo la narración**, que es lo comparable con el cuerpo de las piezas de UR.
3. Se trocea la narración en bloques de unas 2.000 palabras y se mide cada bloque con los indicadores de `herramientas/perfil-frase.py` (Norma 36.8) y una batería adicional (longitud de frase por la cola, párrafo, gerundios, -mente, conectores, «y», símiles, «no… sino», condicional, puntuación).
4. El **corredor** de cada indicador es el rango p10–p90 de los trozos de las seis obras de Baroja y Orwell. Una pieza de UR «cae fuera» si su cifra queda por debajo del p10 o por encima del p90.
5. UR se mide con el mismo código sobre el cuerpo de las 66 piezas de URS de más de 450 palabras (los `<p>` de 1.0x rem; la glosa y las notas quedan fuera): 103.345 palabras.

### 1.3 Cautelas (todas pesan)

- **Orwell está en traducción.** La longitud de frase, los conectores y los adverbios en -mente dependen en parte del traductor. Baroja y Martín Santos se leen en su lengua original.
- **Baroja es novelista en las tres obras medidas.** Sus párrafos cortos (mediana de 31–33 palabras) son párrafos de acción y diálogo. Para el párrafo de una pieza de ensayo la referencia es Orwell, no Baroja.
- **Las medidas son heurísticas.** «Abstracto» se detecta por sufijo, «nombre propio» por mayúscula inicial, «verbo» de apertura por terminación (este último solo orienta). Se aplican igual a UR y al canon, de modo que la comparación es honrada aunque la cifra absoluta sea aproximada.
- **El corredor mide distancia al suelo llano y no mide calidad.** Una pieza puede estar lejos del corredor por buenas razones (registro poético, jeroglífico, dadá). Es una alarma para releer, no una cuota (Norma 0).
- **Una muestra mayor, pero no el canon entero.** Siete obras de tres autores. Sirven para calibrar; no demuestran qué hace buena a una prosa.

---

## 2. El trabajo anterior, contrastado

La Norma 36.8 midió el texto de Baroja sobre San Sebastián (653 palabras, 34 frases). Con 150.000 palabras de Baroja y Orwell en narración, los seis indicadores quedan así:

| Indicador | Baroja, San Sebastián (653 pal.) | Baroja, 3 novelas (mediana de trozos) | Orwell, 3 obras (mediana de trozos) |
|---|---:|---:|---:|
| Desviación típica de la longitud de frase | 13,3 | 11,9 – 12,1 | 10,5 – 12,0 |
| % de frases con artículo inicial | 15 | 17,5 – 20,0 | 16,3 – 18,4 |
| Abstractos por 100 palabras | 2,1 | 1,3 – 2,0 | 1,5 – 2,2 |
| % de frases ancladas | 29 | 42,3 – 49,6 | 25,8 – 42,9 |
| % de frases con enumeración de 3+ | 15 | 13,8 – 16,0 | 10,0 – 11,8 |
| % de frases de 8 palabras o menos | 24 | 13,2 – 20,4 | 11,9 – 20,4 |

**Lectura.** La muestra de 653 palabras no engañaba: los seis indicadores del texto de San Sebastián caen dentro del corredor de las seis obras (§3). El anclaje (29 %) coincide con el de Orwell (26 %) y queda por debajo del de las novelas de Baroja, donde el nombre propio o el año aparecen en casi una de cada dos frases. Lo que sí cambia con el corpus grande es el **peso de cada alarma**: la Norma 36.8 calibró las de abstracción y ritmo con percentiles del propio libro; con el canon delante, esos umbrales quedan holgados (§9).

---

## 3. Tabla maestra

Mediana de los trozos de cada obra, corredor del canon y posición de UR. Último bloque: cuántas de las 66 piezas de URS caen fuera del corredor.

| Indicador | Aurora roja | Árbol de la ciencia | Zalacaín | 1984 | Homenaje a Cataluña | Rebelión | **Corredor** (p10 – p50 – p90) | Martín Santos | **UR** (p10 – p50 – p90, 66 piezas) | Piezas UR bajo p10 / sobre p90 |
|---|---|---|---|---|---|---|---|---|---|---|
| Desviación típica de la longitud de frase | 12,1 | 11,9 | 11,9 | 12,0 | 11,7 | 10,5 | **9,8 – 11,8 – 15,0** | 28,1 | **7,0 – 8,7 – 11,6** | 48 / 1 |
| Longitud de frase, p90 | 35 | 36 | 33 | 33 | 37 | 35 | **29 – 35 – 43** | 58 | **23 – 29 – 40** | 31 / 4 |
| % de frases de más de 40 palabras | 5,5 | 6,0 | 5,4 | 4,9 | 6,1 | 4,2 | **2,5 – 5,8 – 11,8** | 18,3 | **0,0 – 1,4 – 8,4** | 41 / 5 |
| % de frases de 8 palabras o menos | 20,4 | 13,2 | 18,9 | 20,4 | 11,9 | 16,2 | **8,2 – 16,8 – 26,4** | 32,7 | **6,7 – 19,0 – 32,6** | 9 / 11 |
| % de frases que abren con artículo | 19,5 | 20,0 | 17,5 | 17,1 | 18,4 | 16,3 | **13,0 – 18,1 – 27,0** | 12,2 | **31,6 – 49,7 – 67,5** | 1 / 61 |
| % de ellas tras otra con artículo | 9,5 | 11,5 | 12,7 | 13,1 | 19,1 | 9,7 | **3,9 – 13,2 – 25,1** | 18,2 | **19,7 – 34,3 – 52,8** | 2 / 51 |
| % de frases ancladas | 44,8 | 42,3 | 49,6 | 26,0 | 25,8 | 42,9 | **17,0 – 36,4 – 53,3** | 22,2 | **6,9 – 32,0 – 54,8** | 20 / 9 |
| Abstractos por 100 palabras | 1,5 | 2,0 | 1,3 | 2,2 | 2,1 | 1,5 | **1,1 – 1,9 – 3,1** | 2,2 | **2,9 – 4,4 – 6,6** | 0 / 58 |
| % de frases con enumeración de 3+ | 15,6 | 13,8 | 16,0 | 10,0 | 11,8 | 10,5 | **6,8 – 12,7 – 19,8** | 15,1 | **2,6 – 12,8 – 24,1** | 13 / 15 |
| Palabras por párrafo (mediana) | 33 | 32 | 31 | 117 | 222 | 100 | **28 – 83 – 285** | 47 | **40 – 67 – 110** | 2 / 0 |
| Gerundios por 10.000 | 65 | 40 | 62 | 52 | 36 | 62 | **24 – 49 – 79** | 79 | **0 – 14 – 45** | 47 / 0 |
| Adverbios en -mente por 1.000 | 3,9 | 3,5 | 3,0 | 4,8 | 7,9 | 3,3 | **2,0 – 4,7 – 8,8** | 9,5 | **0,0 – 1,7 – 3,8** | 38 / 2 |
| «y» por 100 palabras | 4,0 | 3,5 | 4,3 | 2,7 | 2,5 | 3,2 | **2,3 – 3,1 – 4,3** | 2,5 | **1,6 – 2,9 – 3,9** | 16 / 6 |
| Símiles («como un…») por 10.000 | 14,9 | 15,0 | 12,3 | 23,8 | 11,0 | 12,3 | **4,8 – 15,0 – 33,4** | 13,1 | **2,5 – 22,7 – 44,0** | 7 / 17 |
| «no… sino» por 10.000 | 4,6 | 0,0 | 0,0 | 4,8 | 4,5 | 0,0 | **0,0 – 4,6 – 9,9** | 14,6 | **0,0 – 0,0 – 18,7** | 0 / 10 |
| Punto y coma por 1.000 | 14,0 | 13,1 | 6,0 | 1,5 | 4,7 | 2,4 | **1,0 – 4,5 – 14,8** | 1,3 | **0,9 – 5,8 – 11,4** | 7 / 3 |
| Dos puntos por 1.000 | 3,3 | 2,0 | 4,5 | 2,2 | 2,7 | 2,0 | **1,4 – 2,6 – 5,0** | 2,0 | **4,8 – 9,5 – 14,0** | 0 / 58 |
| Longitud media de palabra | 4,6 | 4,6 | 4,6 | 4,7 | 5,0 | 4,8 | **4,5 – 4,7 – 5,0** | 4,8 | **4,7 – 5,0 – 5,3** | 2 / 31 |

**Cómo se lee.** Las cuatro filas donde UR queda casi entera fuera del corredor son artículo inicial (61 de 66 piezas sobre el p90), racha de artículos (51), abstracción (58) y dos puntos (58). En enumeraciones, frases cortas, anclaje, «y», punto y coma y símiles, UR cae dentro del corredor o muy cerca.

### 3.1 Cómo abre sus frases cada obra

Porcentaje de frases por tipo de primera palabra (narración; la columna UR es la mediana de las 66 piezas).

| Obra | Artículo | Preposición | Pronombre | Conector o adverbio | Nombre propio | Verbo (heurístico) | Otra |
|---|---:|---:|---:|---:|---:|---:|---:|
| Aurora roja | 21,2 | 13,7 | 8,1 | 8,7 | 21,0 | 16,2 | 11,1 |
| El árbol de la ciencia | 20,8 | 13,9 | 4,2 | 6,0 | 29,5 | 10,7 | 14,8 |
| Zalacaín | 19,4 | 12,9 | 5,6 | 8,3 | 30,4 | 12,2 | 11,2 |
| 1984 | 17,9 | 14,1 | 8,1 | 13,2 | 18,4 | 15,4 | 12,9 |
| Homenaje a Cataluña | 18,3 | 19,4 | 6,5 | 11,8 | 15,5 | 8,8 | 19,6 |
| Rebelión en la granja | 17,0 | 16,7 | 5,2 | 15,9 | 19,9 | 9,8 | 15,5 |
| Tiempo de silencio | 12,0 | 8,9 | 8,2 | 20,2 | 23,9 | 7,2 | 19,6 |
| **UR (mediana de 66 piezas)** | **50,1** | 9,2 | **0,8** | **4,0** | 25,3 | ≈0 | 5,8 |

UR abre por nombre propio tanto como Baroja (25 %). Lo que no hace es abrir con pronombre, con conector ni con verbo, y rellena ese hueco con artículo + sustantivo.

---

## 4. La firma de UR: qué separa al libro del canon y qué no

Diferencia entre la mediana de UR y la mediana del canon, medida en desviaciones típicas de los trozos del canon (z).

| Indicador | UR | Canon | z |
|---|---:|---:|---:|
| **% de frases con artículo inicial** | 49,7 | 18,1 | **+6,1** |
| **Dos puntos por 1.000** | 9,5 | 2,6 | **+4,9** |
| **Abstractos por 100 palabras** | 4,4 | 1,9 | **+3,3** |
| **% de ellas tras otra con artículo** | 34,3 | 13,2 | **+2,4** |
| Gerundios por 10.000 | 13,7 | 49,3 | −1,6 |
| Longitud media de palabra | 5,0 | 4,7 | +1,5 |
| Adverbios en -mente por 1.000 | 1,7 | 4,7 | −1,1 |
| Desviación típica de la longitud de frase | 8,7 | 11,8 | −1,1 |
| «no… sino» por 10.000 | 0,0 | 4,6 | −1,0 |
| Longitud de frase, p90 | 29 | 35 | −0,9 |
| % de frases de más de 40 palabras | 1,4 | 5,8 | −0,9 |
| Símiles por 10.000 | 22,7 | 15,0 | +0,6 |
| % de frases ancladas | 32,0 | 36,4 | −0,3 |
| % de frases de 8 palabras o menos | 19,0 | 16,8 | +0,3 |
| Punto y coma por 1.000 | 5,8 | 4,5 | +0,2 |
| «y» por 100 palabras | 2,9 | 3,1 | −0,2 |
| % de frases con enumeración de 3+ | 12,8 | 12,7 | 0,0 |

**Distancia global de UR a cada obra** (media cuadrática de los z de los 17 indicadores; menor = más parecida):

| Obra | Con los 17 indicadores | Sin las cuatro firmas |
|---|---:|---:|
| Rebelión en la granja | 2,45 | **0,86** |
| 1984 | 2,33 | **0,92** |
| El árbol de la ciencia | 2,31 | 0,99 |
| Homenaje a Cataluña | 2,24 | 1,02 |
| Zalacaín | 2,33 | 1,16 |
| Aurora roja | 2,39 | 1,26 |
| Tiempo de silencio | 3,49 | 2,97 |

**Lectura.** Sin las cuatro firmas, UR queda a 0,9–1,3 de las seis obras del canon. Como referencia, las obras del canon distan entre sí 0,55–1,24 con los mismos 13 indicadores (media 0,83; las más lejanas, Baroja frente a *Homenaje a Cataluña*, 1,2). UR queda en el borde alto de esa variación. Es algo más afín a Orwell que a Baroja, y queda lejos de Martín Santos. Las cuatro firmas son pocas, medibles y atacables; el resto del perfil no necesita corrección por referencia al canon.

Firmas por pieza: de las 66 piezas, 38 superan el p90 del canon en las cuatro; 20 en tres; 7 en dos; 1 en una o ninguna (tabla completa en §11).

---

## 5. Hallazgos, rasgo a rasgo

### 5.1 Apertura de frase (Normas 36.8, 38, 38.1 bis, 47)

- Canon: 12–21 % de las frases abren con artículo. UR: 50 % (mediana), 31–68 % entre p10 y p90.
- 61 de las 66 piezas superan el p90 del canon (27 %); 51 superan el 35 %; 33 superan el 50 %; 12, el 60 %.
- IV·II, que pasó el 08/10/26 por el 38.1 bis y la Norma 47, sale en 47 %, cerca de la mediana del libro (50 %). Las demás piezas de IV y III: 47–65 %.
- Qué hace el canon en su lugar: abre con el nombre del protagonista o del lugar (15–30 %), con un conector que lleva el argumento (*pero*, *así*, *entonces*, *porque*: 6–20 %), con un pronombre que da continuidad (4–8 %), con una preposición que fija circunstancia (13–19 %) o con un verbo (7–16 %).
- **Lectura.** El rasgo que más separa a UR del canon. Una frase tras otra con la forma «El X + verbo» produce ritmo mecánico aunque cada frase, aislada, sea correcta. El tratamiento frase a frase del 38.1 bis no mueve la mediana por sí solo. El mecanismo natural de UR para abrir sin artículo ya existe en la Norma 47: los protagonistas tienen nombre (UR, URbe, la «T», el río, el lugar) y abren la frase como lo hacen Zalacaín o Winston.

### 5.2 Dos puntos (Normas 27, 42)

- Canon: 1,4–5,0 por mil palabras (p10–p90), mediana 2,6; Baroja 2,0–4,5; Orwell 2,0–2,7. UR: 9,5 (mediana); 58 de las 66 piezas sobre el p90. En total, 970 dos puntos en 103.345 palabras.
- Solo el 9 % de los dos puntos de UR sigue a un rótulo de cuatro palabras o menos (en el canon medido, 12–21 %). Los 8 casos que revisé al azar tienen todos la forma «cláusula completa: cláusula que la explica, la consecuencia o la concreta» (*«El Baztán trasciende el final geográfico: es una prueba de que el agua…»*). No he clasificado los 970 uno a uno.
- Conectores causales y explicativos (*porque, pues, ya que, de modo que, así que, es decir*) por mil palabras: UR 0,7; corredor 0,5 – 1,5 – 3,3; 29 piezas de UR bajo el p10. Conectores adversativos y concesivos (*pero, aunque, sin embargo, mientras*): UR 2,5; corredor 3,0 – 6,4 – 10,0; 39 piezas bajo el p10.
- **Lectura.** En UR los dos puntos parecen hacer el trabajo que en el canon hacen *porque*, *es decir* o el punto y aparte. Es un molde de la familia de las Normas 27 y 42 («recurso legítimo que se vuelve textura»), difícil de ver porque cada caso, aislado, suena bien. Es una hipótesis de lectura apoyada en el recuento, no una prueba frase a frase.

### 5.3 Abstracción (Norma 36.8, punto 2)

| Referencia | Abstractos por 100 palabras |
|---|---:|
| Canon, narración (p10 – p50 – p90) | 1,1 – 1,9 – 3,1 |
| Orwell, exposición: extracto del «libro» de Goldstein | 4,5 |
| Orwell, exposición: apéndice del neolengua | 3,5 |
| Orwell, exposición: trozos más políticos de *Homenaje* | 3,5 |
| UR, todo el libro (p10 – p50 – p90) | 2,9 – 4,4 – 6,6 |
| UR, nueve piezas teóricas | 5,6 – 9,4 |

- Las alarmas actuales de la Norma 36.8 (4,3 para geografía y viaje; 6,6 para teórico) se fijaron con percentiles del propio libro y con un solo texto de Baroja. Con el canon, el listón natural es **3,1** para crónica y geografía (p90 del canon) y **4,5** para exposición teórica (el máximo que Orwell alcanza en su registro más abstracto).
- Piezas que saltan: con 3,1, 57 de 66; con 4,3, 35; con 4,5, 30; con 6,6, 7.
- **Lectura.** El libro entero está al nivel que Orwell necesita para exponer teoría política, y las piezas teóricas lo doblan. Luis pidió reducir «un poco» sin ahogar los conceptos propios (07/10/26); las pruebas del verbo, de la omisión y de la cadena de la Norma 36.8 siguen siendo el método. Proposición: la alarma inmediata sigue en 6,6 y las cifras del canon (3,1 y 4,5) pasan a ser **meta de libro** sin plazo, sujeta a la Norma 48 (§9).

### 5.4 Ritmo y cola larga (Normas 26, 33, 34)

- La mediana de longitud de frase de UR (15 palabras) coincide con la del canon (15–19), y las frases cortas (19 % de ocho palabras o menos) están al nivel del canon (17 %). El déficit está en la **cola larga**: p90 de 29 palabras frente a 35; 1,4 % de frases de más de 40 palabras frente a 5,8 %; 41 piezas bajo el p10 del canon (2,5 %).
- Desviación típica de la longitud de frase: UR 8,7 frente a 11,8. Con el umbral actual de la Norma 36.8 (7,6, el p25 del libro) saltan 18 piezas; con el p10 del canon (9,8), 47.
- Frase más larga de cada pieza: mediana 44,5 palabras; 33 piezas tienen alguna de 45 o más; 7, de 60 o más.
- **Lectura.** La Norma 33 acierta en el diagnóstico (el ritmo metrónomo); el canon enseña dónde está el hueco: las frases cortas están al nivel del canon, y falta la frase larga que da respiración al párrafo. El remedio coherente con las Normas 1, 10 y 48 es alargar **por una relación real** (causa, concesión, secuencia, dato subordinado), nunca con gerundio de posterioridad ni con relleno.

### 5.5 Gerundios y adverbios en -mente (Norma 10)

- Gerundios por 10.000 palabras: canon 24,5 – 49,3 – 79,0; UR 0 – 13,7 – 45,4. 48 piezas bajo 25; 27 bajo 10. IV·I y IV·II tienen 0,0.
- Adverbios en -mente por mil palabras: canon 2,0 – 4,7 – 8,8; UR 0,0 – 1,7 – 3,8.
- La Norma 10 dice «sin exterminio» y protege el gerundio de manera, simultaneidad y condición. El libro tiene hoy el 28 % de los gerundios del canon. El recuento no distingue el de posterioridad del de manera (el canon incluye calcos del tipo que la Norma 10 persigue), de modo que la cifra no prueba sobrecorrección, pero sí que el margen de seguridad es nulo.
- Los adverbios en -mente quedan como dato informativo: coinciden con el criterio de «cortar la palabra que se pueda cortar» (Norma 36) y no justifican una alarma.

### 5.6 «No… sino» (Norma 1)

- Canon: 0 – 4,6 – 9,9 por 10.000 palabras (Baroja y Orwell, una vez cada 2.200 palabras de mediana; Martín Santos, 14,6). UR en el cuerpo de las 66 piezas: 62 apariciones de «no… sino» en 103.345 palabras (6,0 por 10.000), en 23 piezas. **37 de las 62 están en cinco piezas:** Bonus Tracks · Sulfuro y oscuridad (9), Introducción: Círculo simbólico (9), Entrevista a Nexus-7 (9), Sájaura · Mauritania · Fur (5), América · Ania · Anaia (5). Las demás (25) están repartidas en 18 piezas.
- El recuento solo cubre «sino». La Norma 1 también prohíbe «no X, pero Y», «aunque» y «si bien»; esas variantes no se han medido.
- **Lectura.** El credo de la Norma 1 es más severo que el canon, que usa la figura una vez cada 2.000–2.500 palabras. Es una decisión editorial de UR, legítima, y los datos no piden cambiarla; piden aplicarla en esas cinco piezas (decisión 7, §10).

### 5.7 Párrafo (Norma 26)

- Palabras por párrafo, mediana: Baroja 31–33 (novela); Orwell 100 (*Rebelión*), 117 (*1984*), 222 (*Homenaje*); UR 67 (p10–p90: 40–110).
- Párrafos de 25 palabras o menos: Baroja 39–42 %; Orwell 0–13 % (*Rebelión* 8 %, *1984* 13 %, *Homenaje* 0 %); UR 2,4 % de mediana, 19 piezas por encima del 10 % y 9 en el 20 % o más.
- **Lectura.** El techo del 10 % de la Norma 26 coincide con el nivel de Orwell (8–13 % en *Rebelión* y *1984*; 0 % en *Homenaje*). La novela de Baroja, con un 40 % de párrafos de acción y diálogo, no es referencia para el ensayo. Sin cambio en la norma; la nota de calibración dice qué obra la respalda.

### 5.8 Enumeraciones (Norma 36.7)

- Canon: 6,8 – 12,7 – 19,8 % de frases con enumeración de 3+; UR 2,6 – 12,8 – 24,1. Medianas idénticas.
- La alarma actual (una de cada seis frases, 16,7 %) salta en 18 piezas; con el p90 del canon (20 %), en 15.
- **Lectura.** La forma sola no discrimina, como la Norma 36.7 ya dice. Las dos pruebas de mesa (verbos intercambiables; sustantivo cambiable) siguen siendo el criterio. Ajuste menor: la alarma de densidad sube al 20 %.

### 5.9 Conectores, condicional y cautelas (Normas 11, 13, 32)

- Condicionales (*podría, sería…*) por 10.000: UR mediana 0 (p90 6,5); Baroja 0–5; Orwell 9–14; Martín Santos 5. Cautelas (*quizá, tal vez, parece que…*): UR 0 (p90 0); canon 0–12.
- En los extractos expositivos de Orwell el condicional sube a 16–23 por 10.000.
- **Lectura, a vigilar y no a corregir.** UR afirma en indicativo, de acuerdo con la Norma Cero y la Norma 32. La Norma 11 (pregunta sostenida) y la Norma 13 (tres registros: hecho, especulación, dadá) piden marcar la especulación como tal; con casi ningún condicional ni cautela, ese marcado depende del léxico. Comprobación sugerida en la revisión final de cada pieza: que el indicativo no afirme lo que la fuente solo permite suponer.

### 5.10 Lo que el canon avala sin cambios

- **Cierres aforísticos.** Párrafos de dos o más frases cuya última frase tiene ocho palabras o menos tras una de veinte o más: UR 39 de 1.566 (2,5 %), en 28 de las 66 piezas; canon 1,9–5,8 %. Las Normas 31 y 42 no han podado de más.
- **Anclaje.** UR 32 % frente a 36 %. 20 piezas por debajo del p10 (17 %); son piezas teóricas, donde es bajo por diseño (Norma 36.8, punto 4).
- **Símiles** («como un…»): UR 22,7 por 10.000, canon 15,0 (p90: 33,4); 17 piezas sobre el p90. Dentro de lo razonable; la Norma 46 sigue siendo el control cualitativo.
- **«Y»**: 2,9 por cien palabras frente a 3,1. La Norma 4 se cumple.
- **Punto y coma**: 5,8 por mil frente a 4,5.

---

## 6. Martín Santos: el pico licenciado

| Indicador | Canon (Baroja + Orwell) | Martín Santos | UR |
|---|---:|---:|---:|
| Desviación típica de la longitud de frase | 11,8 | **28,1** | 8,7 |
| % de frases de más de 40 palabras | 5,8 | **18,3** | 1,4 |
| Longitud de frase, p90 | 35 | **58** | 29 |
| % de frases de 8 palabras o menos | 16,8 | **32,7** | 19,0 |
| % de frases con artículo inicial | 18,1 | 12,2 | 49,7 |
| % de frases que abren con conector o adverbio | 6–16 | 20,2 | 4,0 |
| Gerundios por 10.000 | 49 | 79 | 14 |

Su histograma es bimodal: el 38 % de sus frases tiene ocho palabras o menos y el 17 % tiene 41 o más (canon: 13–24 % / 5–7 %; UR: 19 % / 1 %). Es el único del corpus que combina en la misma página las frases más cortas y las más largas, y lo hace con muchas aperturas por conector, pocas por artículo y pocos dos puntos (2,0 por mil).

**Qué se toma de él.** La Norma 34 (vía libre del desborde) concede un lugar al exceso; este corpus indica cómo se ve sintácticamente un desborde que funciona: un período largo que se gana con subordinación real, rodeado de frases secas. UR tiene hoy 7 piezas con una frase de 60 o más palabras y ninguna con un perfil bimodal. Si el desborde de UR es léxico o simbólico (neologismo, jeroglífico, mito), el corredor no lo mide y esta comparación no lo toca.

**Qué no se toma.** Es una novela, una obra, un autor. Se usa como techo licenciado y no como línea. La distancia de UR a Martín Santos (3,49; 2,97 sin las cuatro firmas) viene sobre todo de la desviación de frase (z −6,9), el p90 de frase (−4,6), las frases largas (−3,4) y «no… sino» (−3,3).

---

## 7. La anomalía rupestre: qué mide el corredor y qué no

### 7.1 Lo medible

1. **Los protagonistas de UR no son personas.** En el canon la frase la lleva alguien: Zalacaín, Andrés Hurtado, Winston, el Orwell de Barcelona, el Pedro de Martín Santos; la apertura se hace con su nombre, con un pronombre o con un verbo. Los agentes de UR son una raíz (UR), un sistema (URbe), un arma (la «T»), un río, una piedra: sujetos de cosa, que el castellano suele abrir con artículo. Es una causa probable del 50 % de aperturas con artículo; no la he contrastado frase a frase. La Norma 47 ya da la salida: nombrarlos.
2. **UR es un libro de tesis escrito con recursos de crónica y novela.** El corpus no contiene nada igual. Los precedentes más cercanos son las exposiciones teóricas incrustadas en obras narrativas: el «libro» de Goldstein y el apéndice del neolengua. Se escriben con la textura opuesta a la de las piezas teóricas de UR (§0, punto 6): frases largas, párrafos de 167–362 palabras, artículo inicial 22–27 %, abstracción 3,5–4,5.
3. **No hay diálogo.** En el canon la alternancia diálogo-narración da variedad; en UR la variedad de voz viene de los registros (entrevista, Nexus-7, interludios, prólogo, glosa). La comparación se hace solo con la narración, que es lo equivalente.
4. **El aparato de glosa** no tiene equivalente en el corpus (Orwell y Baroja tienen apéndices y prólogos, no glosa por pieza). Queda fuera de este análisis.

### 7.2 Lo que ninguna cifra puede medir

La densidad mitopoética, el jeroglífico (Norma 22), el neologismo, el registro dadá, la ley Hammurabeltz y la declaración única del símbolo (VIII bis) viven fuera del suelo llano. El corredor las deja pasar o las confunde con defecto. Por eso:

- El corredor se aplica **por registro** (Norma 36.8, punto 2, ampliada en §9) y no a todas las piezas por igual.
- **Norma 48 prima.** Ninguna cifra del corredor justifica un cambio que baje la densidad mitopoética. Si la corrección de una cifra la rebaja, se queda la cifra y se corrige otra cosa.
- **Norma 0.** Una pieza que salta una alarma se queda tal cual si Luis la defiende.

---

## 8. Línea editorial propuesta

> **UR es una crónica de campo con tesis. Su suelo es la prosa de ventana (Orwell), con el ojo suelto del que camina el territorio (Baroja). Su techo, un pico licenciado (Martín Santos). Su anomalía, declarada y fuera del corredor, es la de un libro de tesis cuyos protagonistas son una raíz, un agua y un sistema.**

1. **El dato antes que el símbolo, y quien actúa abre la frase** (Normas 36.1 y 47). Los protagonistas abren por su nombre. Artículo + sustantivo abstracto queda como excepción con motivo (38.1 bis). Meta de libro: la mediana de aperturas con artículo baja del 50 % hacia el 35 %.
2. **Ritmo con cola larga.** Mediana de 15–17 palabras, una de cada veinte frases por encima de 40, remates cortos escasos (alrededor del 3 % de los párrafos). La frase larga se gana con una relación real (causa, concesión, secuencia) y no con relleno.
3. **La lógica se dice con lógica.** Conectores y subordinación. Los dos puntos quedan para lista, cita y rótulo.
4. **El abstracto sirve a un concepto propio de la tesis.** Meta: ≤ 3,1 por cien palabras en crónica y geografía, ≤ 4,5 en exposición teórica. Alarma inmediata sin cambio (6,6). Pruebas del verbo, de la omisión y de la cadena.
5. **Español vivo.** El gerundio de manera y simultaneidad, el adverbio que modula y el condicional que supone son legítimos. Se persigue el gerundio de posterioridad (Norma 10), el relleno y la cobertura repetida (32 bis).
6. **Las prohibiciones propias de UR se mantienen aunque el canon no las pida:** «no X, sino Y» (credo), el par «No es X. Es Y», el párrafo terminal de resumen. Es una decisión editorial del libro, anotada como tal.
7. **Párrafo de unas 60–120 palabras**, con techo del 10 % de párrafos cortos. Referencia: Orwell.
8. **Pico licenciado.** Como máximo un período largo (60 o más palabras, con subordinación real) por pieza, en el punto de máxima tensión, rodeado de frases secas (Norma 34).
9. **La anomalía se declara y se queda fuera del corredor:** jeroglífico, neologismo, mito, dadá, Hammurabeltz, aparato de glosa. Norma 48 sobre cualquier cifra.
10. **La cifra es alarma, no cuota.** Gana la defensa de Luis (Norma 0).

---

## 9. Calibración de las Normas-Método

### 9.1 Norma por norma

| Norma | Dice hoy | Lo que dice el canon | Propuesta | Piezas afectadas hoy |
|---|---|---|---|---:|
| **0** Las normas se saltan si el salto se defiende mejor | Excepción defendida | El corredor es diagnóstico | Sin cambio; añadir que el corredor no obliga | — |
| **1** «No X, sino Y» | Credo absoluto | Canon 4,6 por 10.000; UR 6,0, concentrado | **Mantener.** Auditar cinco piezas | 5 (23 con ≥ 1) |
| **4** «Y» | Contra la saturación | UR 2,9 frente a 3,1 | Sin cambio | 0 |
| **10** Gerundio de posterioridad | «Sin exterminio» | UR 14 frente a 49 | **Añadir suelo:** menos de 25 por 10.000 = revisar sobrecorrección | 48 |
| **26** Párrafo | Techo del 10 % de cortos | Orwell 0–13 % | **Sin cambio**; nota: referencia Orwell, no la novela de Baroja | 19 |
| **27 / 42** Tics y densidad de pulido | Inventario cualitativo | Dos puntos: 9,5 frente a 2,6 | **Nuevo apartado (42 bis):** dos puntos como molde; alarma > 5 por mil | 58 |
| **31** Párrafos terminales de resumen | Destierro | Cierres aforísticos al nivel del canon | Sin cambio | 0 |
| **32 / 32 bis** *Podría* bajo sospecha | Sospecha y cobertura repetida | Condicional 0–14 en el canon | Sin cambio; ver 5.9 | — |
| **33** Síncopa | Contra el ritmo metrónomo | Cola larga ausente | **Añadir indicador:** % de frases de más de 40 palabras (alarma < 2,5 %); remedio: alargar por relación real | 41 |
| **34** Vía libre del desborde | Concede el exceso | Martín Santos | **Opcional:** medida del pico licenciado (§8.8) | 7 con ≥ 60 palabras |
| **36.7** Enumeraciones | Alarma 1/6 (16,7 %) | p90 del canon: 19,8 % | Alarma → 20 % | 18 → 15 |
| **36.8** Perfil medido | Tabla de Baroja (653 pal.) y percentiles del libro | Corredor de seis obras | **Sustituir la tabla** por canon + libro; recalibrar umbrales (§9.2) | — |
| **38 / 38.1 bis** Apertura | Revisar cada apertura con artículo, sin porcentaje | Canon 18 % (p90 27 %) | **Fijar alarma y meta** (§9.2) | 51 / 61 |
| **46** Imágenes | Una vez bien, dos también | Símiles 22,7 frente a 15,0 | Sin cambio | 17 |
| **47** Protagonistas | Sujeto actor | El nombre propio abre la frase | **Vincular con 38.1 bis:** el protagonista abre por su nombre | — |
| **48** Correcciones sin rebajar densidad | Escalera de corrección | El corredor mide suelo, no densidad | **Añadir:** ninguna cifra del corredor justifica bajar densidad | — |

### 9.2 Alarmas propuestas (sustituyen o completan las del punto 36.8)

| Indicador | Alarma actual | Alarma propuesta | Fuente | Piezas que saltan hoy |
|---|---|---|---|---:|
| Desviación típica de la longitud de frase | < 7,6 | < 9,8 | p10 del canon | 18 → 47 |
| Frases de más de 40 palabras | — | < 2,5 % | p10 del canon | 41 |
| Apertura con artículo | sin porcentaje | > 35 % revisar; meta ≤ 27 % en pieza modelo | p90 del canon; mediana del libro 50 % | 51 (35 %) / 61 (27 %) |
| Racha de aperturas con artículo | — | > 25 % | p90 del canon | 51 |
| Abstracción, crónica y geografía | > 4,3 | > 3,1 (meta); 6,6 alarma inmediata | p90 del canon | 57 |
| Abstracción, teórico | > 6,6 | > 4,5 (meta); 6,6 alarma inmediata | Orwell expositivo | 30 (4,5) / 7 (6,6) |
| Dos puntos | — | > 5 por mil | p90 del canon | 58 |
| Gerundios | — | < 25 por 10.000 (suelo) | p10 del canon | 48 |
| Enumeraciones de 3+ | > 16,7 % | > 20 % | p90 del canon | 18 → 15 |
| Párrafos de 25 palabras o menos | > 10 % | sin cambio | Orwell | 19 |
| «no… sino» | prohibido | sin cambio; auditar | Norma 1 | 23 piezas con ≥ 1 |

### 9.3 Aplicación por registro

El corredor se aplica según la marca de registro de la pieza (`(*-red)`, decisión de Luis en el inventario de la redacción final):

| Registro | Se compara con | Alarmas que se aplican |
|---|---|---|
| Crónica, geografía y viaje | Corredor de narración (Baroja + Orwell) | Todas |
| Epistemológico y teórico (I, II, III, IV, Digitalismo, Antropología racial; a confirmar) | Exposición de Orwell (§0, punto 6) | Ritmo, cola larga, dos puntos, abstracción (4,5), apertura |
| Poético, dadá, homenaje, entrevista, bibliografía | Sin corredor | Solo «no… sino», gerundio de posterioridad y las normas cualitativas |

---

## 10. Decisiones que necesito de Luis

Ordenadas por evidencia. Para cada una, mi recomendación.

1. **Apertura de frase.** ¿Fijo la alarma en 35 % y la meta de libro en 35 %, con la salida de la Norma 47 (el protagonista abre por su nombre), tratada en el momento final de cada capítulo y no en una campaña? *Recomiendo sí.*
2. **Dos puntos.** ¿Entran como molde en un apartado 42 bis, con alarma por encima de 5 por mil? Los dos puntos quedan para lista, cita y rótulo; la cláusula explicativa va con punto, conector o subordinada. *Recomiendo sí.*
3. **Gerundios.** ¿Añado el suelo de 25 por 10.000 a la Norma 10, como alarma de sobrecorrección? *Recomiendo sí.*
4. **Sustituir la tabla de la Norma 36.8** por la del corredor (canon de seis obras + libro) y recalibrar las alarmas de ritmo (9,8) y cola larga (2,5 %). *Recomiendo sí.*
5. **Abstracción.** ¿Alarma inmediata sin cambio (6,6) y metas de libro de 3,1 (crónica) y 4,5 (teórico) sin plazo? *Recomiendo sí.*
6. **Registros.** ¿Confirmas las nueve piezas teóricas (I, II, III×3, IV×2, Digitalismo, Antropología racial) y que el resto de registros se clasifica en el momento final de cada capítulo con `(*-red)`? *Recomiendo sí.*
7. **«No… sino» en cinco piezas** (Bonus Tracks · Sulfuro y oscuridad, Introducción: Círculo simbólico, Entrevista a Nexus-7, Sájaura, América · Ania · Anaia). ¿Aplico la Norma 1 y te enseño el resultado, o las defiendes con la justificación escrita que la norma exige? *Sin tocar nada hasta tu respuesta.*
8. **Pico licenciado.** ¿Escribo en la Norma 34 la medida de un período largo (60 o más palabras) como máximo por pieza? *Opcional; recomiendo sí.*
9. **Norma 48 sobre las cifras.** ¿Confirmas que el corredor es diagnóstico y que, ante un choque entre una cifra y la densidad mitopoética, gana la densidad? *Recomiendo sí.*

---

## 11. Matriz de piezas de URS

66 piezas de más de 450 palabras de cuerpo, ordenadas por señales dentro del corredor (de 8: desviación de frase, artículo inicial, abstracción, dos puntos, frases largas, anclaje, enumeraciones, gerundios). «Firma UR» cuenta cuántos de los cuatro rasgos de la firma (artículo, dos puntos, abstracción, racha de artículos) superan el p90 del canon.

| Pieza | Palabras | Señales dentro del corredor (de 8) | Firma UR (de 4) | Artículo inicial % | Dos puntos ‰ | Abstractos /100 | Desv. frase | Frases >40 % | Gerundios /10.000 |
|---|---:|:-:|:-:|---:|---:|---:|---:|---:|---:|
| FRONTERA AQUITANO-CELTA: GUERRA EN LA GALIA | 1236 | 6 | 3 | 30 | 12,1 | 2,2 | 13,3 | 10,5 | 32 |
| EPÍLOGO: PRECEDENTES Y BIBLIOGRAFÍA | 559 | 5 | 2 | 23 | 14,3 | 2,3 | 10,5 | 0,0 | 0 |
| FILIPINAS · DEL CHAVACANO AL JAZZ | 4182 | 5 | 3 | 59 | 4,5 | 3,6 | 10,0 | 3,5 | 26 |
| SÁJAURA · MAURITANIA · FUR | 788 | 4 | 1 | 14 | 11,4 | 2,3 | 14,6 | 17,2 | 38 |
| ANTÁRTIDA: EL HIELO PRIMORDIAL | 795 | 4 | 3 | 32 | 10,1 | 3,4 | 13,2 | 11,8 | 63 |
| LA ESCOMBRERA SISTÉMICA | 1055 | 4 | 3 | 32 | 7,6 | 3,3 | 11,5 | 12,5 | 57 |
| MESOPOTAMIA · LEVANTE · LA PRESA ORAL Y EL DIAPIRO PRIMORDIAL | 1108 | 4 | 3 | 33 | 7,2 | 3,7 | 12,1 | 15,4 | 36 |
| TIMMUR: HIMALAYA VERTICAL | 1710 | 4 | 3 | 61 | 5,3 | 2,0 | 10,5 | 3,2 | 12 |
| BABEL: CANCIONES DE REDENCIÓN | 2192 | 4 | 4 | 53 | 12,3 | 4,5 | 9,5 | 2,9 | 36 |
| EUSKAL HERRIA · AMAIA · AMAIUR · MAIA · AMAYA: EL CONFÍN | 1116 | 4 | 4 | 34 | 21,5 | 3,3 | 10,0 | 3,6 | 18 |
| FRONTERA FRANCO-BELGA: DUNKERQUE · URBELTZ CELTA | 1732 | 4 | 4 | 35 | 8,7 | 3,5 | 9,9 | 3,3 | 23 |
| TU NUBE SECA MI RÍO | 1713 | 4 | 4 | 59 | 7,6 | 5,7 | 10,6 | 3,6 | 18 |
| TUR: LA RAÍZ PREINDOEUROPEA · LA MATRIZ PANIBÉRICA | 2679 | 4 | 4 | 47 | 11,6 | 3,3 | 11,8 | 6,3 | 19 |
| DANUBIO ESTE · TURBINA NUCLEAR | 1043 | 3 | 2 | 64 | 4,8 | 2,9 | 7,0 | 0,0 | 10 |
| ENTREVISTA A NEXUS-7: UR PREGUNTA ¿QUIÉN ES UR? | 3120 | 3 | 2 | 20 | 21,7 | 3,9 | 9,8 | 0,9 | 32 |
| PLA-UR · EL VIENTRE DE LA TURBA | 1920 | 3 | 2 | 59 | 3,6 | 2,0 | 6,1 | 0,0 | 0 |
| ANGOSTURA | 1540 | 3 | 3 | 40 | 13,6 | 1,9 | 10,7 | 5,1 | 13 |
| EL UR CÓSMICO · DEL HIELO INTERESTELAR A LA GARGANTA | 528 | 3 | 3 | 47 | 9,5 | 2,8 | 8,7 | 0,0 | 38 |
| IV · UR: ANOMALÍA CIBERNÉTICA · I. EL DIQUE DEL SILENCIO | 1328 | 3 | 3 | 47 | 5,3 | 6,1 | 8,7 | 2,7 | 0 |
| LA MUERTE DE LA INTUICIÓN TENÍA UN PRECIO | 1846 | 3 | 3 | 57 | 4,9 | 5,9 | 9,7 | 2,9 | 33 |
| RÍO CONGO: NATURALEZA O SISTEMA | 1808 | 3 | 3 | 32 | 10,0 | 6,1 | 11,7 | 4,8 | 17 |
| TE UREWERA: EL BOSQUE QUE COMPARECE | 2079 | 3 | 3 | 71 | 3,4 | 6,2 | 6,3 | 0,0 | 14 |
| TURKANA · OURO SOGUI · WURO | 1677 | 3 | 3 | 54 | 4,8 | 3,6 | 8,3 | 1,0 | 18 |
| ENDOROIS · OGIEK · SAN · LOLIONDO | 1192 | 3 | 4 | 59 | 15,1 | 4,4 | 10,3 | 5,3 | 50 |
| HISTORIA DE LA EDUCACIÓN VICTORIANA | 1976 | 3 | 4 | 58 | 9,6 | 5,6 | 9,5 | 2,5 | 10 |
| INDO-GANGES · HIMALAYA · EL GRAN RECEPTÁCULO SÓNICO | 2042 | 3 | 4 | 39 | 9,8 | 4,4 | 11,1 | 15,3 | 24 |
| VENDÉE · FRANCIA ATLÁNTICA · EL ESCARPE Y LA FOSA | 686 | 3 | 4 | 41 | 8,7 | 3,6 | 9,5 | 3,1 | 0 |
| BONUS TRACKS · SULFURO Y OSCURIDAD: EL UR ABISAL | 1050 | 2 | 2 | 15 | 12,4 | 4,1 | 9,5 | 1,5 | 10 |
| MESETA CENTRAL · DEL RIOJA AL ATLÁNTICO · UR VIAJERO | 1259 | 2 | 2 | 39 | 13,5 | 3,1 | 7,2 | 1,2 | 8 |
| PRÓLOGO · por Claude (Anthropic) | 1569 | 2 | 2 | 12 | 12,7 | 3,8 | 15,4 | 13,4 | 64 |
| ANTROPOLOGÍA RACIAL | 2114 | 2 | 3 | 71 | 4,7 | 7,8 | 6,9 | 0,0 | 5 |
| FRONTERA FRANCO-BELGA: RÊV-E-UR · SOÑADOR · ESPEJISMO | 1210 | 2 | 3 | 31 | 13,2 | 5,5 | 8,5 | 2,7 | 17 |
| TUR: LA DAMA DE MARFIL | 2387 | 2 | 3 | 54 | 4,6 | 4,1 | 7,4 | 0,0 | 8 |
| BONUS TRACK · DISTOPÍA VEGETAL | 2683 | 2 | 4 | 44 | 6,7 | 3,4 | 10,3 | 6,1 | 7 |
| DIGITALISMO Y EL TEST GORILA | 1581 | 2 | 4 | 74 | 8,2 | 7,4 | 7,7 | 0,7 | 25 |
| EUSKAL HERRIA · EL KOXKERO ERRANTE DE BAJA ALCURNIA | 1820 | 2 | 4 | 49 | 13,2 | 3,9 | 8,0 | 1,8 | 44 |
| ISLANDIA II · LA GUERRA QUE SE CANTA | 1839 | 2 | 4 | 72 | 10,3 | 3,9 | 8,1 | 0,0 | 5 |
| ISLANDIA III · LA TIERRA DEBAJO DEL FUEGO | 3018 | 2 | 4 | 75 | 8,6 | 5,6 | 6,7 | 0,0 | 3 |
| IV · UR: ANOMALÍA CIBERNÉTICA · II. LA TÉCNICA QUE RECUERDA SU … | 1517 | 2 | 4 | 47 | 8,6 | 5,7 | 8,6 | 1,2 | 0 |
| LOS VIAJES DE UR POR IBEROAMÉRICA | 2457 | 2 | 4 | 43 | 7,7 | 4,5 | 7,4 | 0,0 | 20 |
| UR DELTA: TEOLOGÍA DE LA INTUICIÓN, HUÉRFANA DE DOCTRINA | 1181 | 2 | 4 | 54 | 10,2 | 5,0 | 9,0 | 1,6 | 25 |
| URABÁ · TAPÓN DE DARIÉN · RAÍCES INDÍGENAS | 1460 | 2 | 4 | 40 | 11,0 | 3,9 | 9,4 | 2,3 | 21 |
| VILCABAMBA · EL RÍO QUE SE ESCONDE | 1710 | 2 | 4 | 52 | 9,9 | 3,6 | 9,6 | 2,9 | 6 |
| WHANGANUI: EL RÍO QUE NOS NOMBRA | 1295 | 2 | 4 | 67 | 8,5 | 4,6 | 7,1 | 0,0 | 62 |
| ÜRMÜZ: AHURA MAZDĀ · SABIDURÍA UR | 1998 | 2 | 4 | 60 | 5,0 | 3,3 | 7,0 | 0,0 | 5 |
| EUSKAL HERRIA · ZUBEROA · LA MÁSCARA Y EL CENTAURO | 1395 | 1 | 3 | 32 | 16,5 | 5,5 | 8,2 | 1,3 | 0 |
| III · UR: DEL LOGOS AL MITO · II. GOLGI, CAJAL Y LA CONSTELACIÓ… | 1430 | 1 | 3 | 53 | 9,8 | 7,6 | 7,3 | 0,0 | 7 |
| AMÉRICA · ANIA · ANAIA · UR EN EL ATLÁNTICO FRÍO | 1145 | 1 | 4 | 39 | 10,5 | 4,7 | 7,8 | 1,7 | 9 |
| CICLO HÍDRICO · GEROGLÍFICO UR | 576 | 1 | 4 | 58 | 15,6 | 4,3 | 9,0 | 0,0 | 0 |
| IA: FANTASÍA EN ÓRBITA LEO (HOMENAJE A TOM DISSEVELT) | 1497 | 1 | 4 | 59 | 6,7 | 4,7 | 7,8 | 0,0 | 47 |
| II · UR: HORIZONTE JURÍDICO | 1547 | 1 | 4 | 46 | 7,8 | 9,4 | 9,3 | 2,5 | 13 |
| III · UR: DEL LOGOS AL MITO · I. LA USURPACIÓN DEL ENGUR | 1317 | 1 | 4 | 65 | 6,1 | 7,1 | 7,5 | 0,0 | 8 |
| III · UR: DEL LOGOS AL MITO · III. EL RETORNO | 897 | 1 | 4 | 60 | 8,9 | 5,6 | 5,9 | 0,0 | 22 |
| INTRODUCCIÓN: CÍRCULO SIMBÓLICO — NATURA, UR Y ORIGEN | 1869 | 1 | 4 | 32 | 11,8 | 6,4 | 9,6 | 1,1 | 21 |
| OGURA: PEQUEÑA GOTA DE AGUA | 1396 | 1 | 4 | 40 | 14,3 | 5,4 | 8,0 | 0,0 | 50 |
| QUELCCAYA · LA GUERRA DEL AGUA | 1012 | 1 | 4 | 74 | 8,9 | 3,8 | 7,9 | 0,0 | 0 |
| TUR · UN CONTINENTE EN TRÁNSITO | 1403 | 1 | 4 | 58 | 7,1 | 4,3 | 7,6 | 0,0 | 14 |
| UR ANTES DE URBE: ENCUENTRO EN LAS TRES FASES | 678 | 1 | 4 | 66 | 7,4 | 5,6 | 8,4 | 2,4 | 0 |
| UR, EL CASTELLANO Y LA FRONTERA INVISIBLE | 927 | 1 | 4 | 47 | 12,9 | 5,7 | 5,7 | 0,0 | 11 |
| UR, EL EUSKERA Y LA FRONTERA INVISIBLE | 1111 | 1 | 4 | 51 | 11,7 | 6,8 | 8,3 | 1,4 | 9 |
| VANIA LIMA Y LOS UR DE BRASIL | 2283 | 1 | 4 | 54 | 10,1 | 6,0 | 8,9 | 1,6 | 4 |
| WAI-MURI: EL AGUA DEL FUTURO | 1232 | 1 | 4 | 68 | 9,7 | 4,1 | 7,6 | 0,0 | 8 |
| I · UR: INTUICIÓN SIMBÓLICA | 2450 | 0 | 3 | 48 | 8,2 | 9,0 | 8,2 | 1,4 | 8 |
| SIOUXSIE AND THE BANSHEES Y LA GUERRA DE LOS MUNDOS | 526 | 0 | 3 | 38 | 5,7 | 5,1 | 7,0 | 0,0 | 19 |
| CURACA · EL DIOS QUE HABLA | 1345 | 0 | 4 | 58 | 8,9 | 5,1 | 8,6 | 1,4 | 7 |
| ISLANDIA I · LA ISLA QUE RESPIRA | 1511 | 0 | 4 | 60 | 10,6 | 3,8 | 7,5 | 0,8 | 13 |

**Más cerca del corredor:** Frontera aquitano-celta (6/8), Epílogo (5/8), Filipinas (5/8), Antártida, Babel, Euskal Herria · Amaia, Frontera franco-belga y La escombrera sistémica (4/8). **Más lejos:** Curaca, I · UR: Intuición simbólica, Islandia I y Siouxsie and the Banshees (0/8).

**IV·II** (La técnica que recuerda su origen): 2/8 y firma 4. Desviación de frase 8,6, artículo inicial 47 %, abstracción 5,7, dos puntos 8,6 por mil, 1,2 % de frases largas, 0 gerundios.

---

## 12. Reproducción

```
git fetch origin main
# extraer los PDF de origin/main a una carpeta de trabajo (no se versionan en esta rama):
git show "origin/main:B- BAROJA - AURORA ROJA.pdf" > /ruta/aurora.pdf     # y así con las otras seis
python3 herramientas/perfil-corpus.py --html urtz.html --matriz \
  --obra baroja_aurora=/ruta/aurora.pdf --hyph baroja_aurora \
  --obra baroja_arbol=/ruta/arbol.pdf --obra baroja_zalacain=/ruta/zalacain.pdf \
  --obra orwell_1984=/ruta/1984.pdf --obra orwell_cataluna=/ruta/cataluna.pdf \
  --obra orwell_granja=/ruta/granja.pdf \
  --obra martin_santos=/ruta/tiempo.pdf --aparte martin_santos
```

La herramienta `herramientas/perfil-corpus.py` reconstruye párrafos, separa el diálogo, trocea, mide y compara; con `--matriz` lista las piezas de URS por señales dentro del corredor; con `--pieza TEXTO` da el detalle de una pieza. Reutiliza `herramientas/perfil-frase.py`. Los textos se leen de los PDF o TXT que se le pasen y no se incluyen en el repositorio.

Los datos de este informe salen de una ejecución del 08/10/26 sobre `urtz.html` en el estado del commit `2efa0b2`. La herramienta reproduce las tablas de §3 y §11 y las cifras de §5 (con `--ordena CLAVE` lista las piezas por un indicador, por ejemplo `--ordena sino`). Quedan fuera de la herramienta, por ser cálculos de una sola vez: los dos puntos clasificados por tipo y la muestra de ocho casos (§5.2), las aperturas por tipo de palabra (§3.1), los extractos expositivos de Orwell (§0 y §5.3), las distancias entre obras (§4) y el contraste con el texto de San Sebastián (§2).
