# MARCO-ANALISIS-TEXTUAL — Los 18 análisis aplicados a UR y medidos frente al canon

**Estado: PROPUESTA del 09/10/26. Nada de lo que sigue está aplicado a `urtz.html` ni a `NORMA-METODO.md`.** Complementa a `LINEA-EDITORIAL-REFERENTES.md`. Responde a la petición de Luis del 08/10/26: llevar la comparación con Baroja, Orwell y Martín Santos a los análisis de texto y sintáctico, y tener el marco completo en las Normas-Método para usarlo en las correcciones finales. Los informes se van aplicando a medida que se trabaja cada capítulo (Luis, 08/10/26); este documento no propone una campaña.

---

## 0. Resumen

1. **Cobertura.** De los 18 análisis, 7 se miden por completo con herramienta (2 morfológico, 3 sintáctico, 4 léxico, 9 legibilidad, 14 estilometría, 16 entidades, 18 plantillas), 5 se miden en parte (1 fonético, 5 textualidad, 8 estilístico, 13 narratológico, 17 sinteticidad), 5 son lectura guiada de Claude con preguntas fijas (6 semántico, 7 temático, 10 pragmático, 11 discurso, 12 intención) y 1 no se aplica (15 sentimiento).
2. **Instrumento.** `herramientas/analisis-texto.py`, con el analizador sintáctico del español de spaCy: 80 indicadores sobre ventanas de 1.000 palabras, comparados con el mismo corredor del canon (270 ventanas de Baroja y Orwell) y con 104 ventanas de UR. Reutiliza `perfil-corpus.py`.
3. **Hallazgo central: UR escribe en estilo nominal.** El sujeto de la oración principal es «artículo + sustantivo» en el 46 % de los casos (canon 23 %), casi nunca se omite (9 % frente a 28 %) ni se retoma con pronombre (0 % frente a 5 %). Hay más sustantivos (26,4 por cien palabras frente a 20,8) y menos verbos (14,0 frente a 16,3), pronombres (3,6 frente a 7,0), subordinadas (1,1 por frase frente a 1,5) y conectores. Es la misma firma que aparecía en el informe anterior (artículo inicial, racha de artículos, abstracción, dos puntos), vista ahora por dentro.
4. **No lo han causado las normas.** Medidas 42 piezas el 09/09, el 23/09, el 03/10 y el 08/10, el perfil no se mueve (sujeto artículo + sustantivo 43,8 → 43,7 %; subordinadas por frase 1,2 → 1,2). Es el perfil de origen del borrador. Y las revisiones hechas hasta hoy tampoco lo han movido: pide una pasada sistemática, que este documento ordena (§2).
5. **Las soluciones son aditivas.** Elipsis del sujeto, pronombre, conectores, subordinadas con dato, gerundio de manera, punto y coma. Alargan la frase (hueco de la cola larga) sin tocar las frases cortas de The Clash (§6).
6. **Dos puntos:** 68 % unen dos cláusulas con verbo. Borrador de norma y soluciones clásicas por clase en §5.
7. **Gerundios:** la Norma 10 funciona; no hay que cambiarla (§7).
8. **Plantillas (análisis 18):** el 18 % de las frases de UR tiene un esqueleto gramatical que se repite cuatro o más veces en su ventana (canon 0 %; Orwell expositivo 1 %). La forma más repetida, «artículo + sustantivo + verbo + artículo» (*«El agua evita la línea recta.»*), abre el 7,8 % de todas las frases del libro. El texto no repite frases literales (4-gramas al nivel del canon). Repite moldes.
9. **Voz (análisis 14):** cinco piezas pasan de 0,7 de distancia al perfil medio de UR (Sulfuro 0,91, Prólogo 0,85, Sájaura 0,74, Siouxsie 0,74, Rêv-E-UR 0,73) y dos están en el límite (América y Ciclo hídrico, 0,70). La lista de las doce más alejadas del §3 es un ranking y no doce fallos. Sulfuro y Sájaura coinciden con las que concentran «no… sino». Aviso para la revisión final, no un defecto.
10. **Legibilidad (análisis 9):** las piezas de crónica están en la banda normal de INFLESZ (58); las teóricas, en «algo difícil» (48), igual que la exposición de Orwell (49), pero con palabras más largas.
11. **Decisiones nuevas para Luis (§9),** que se suman a las nueve del informe anterior.

---

## 1. Los 18 análisis: cobertura, estado y uso en la corrección final

| # | Análisis | Cómo se hace en UR | Estado | Normas con las que enlaza | Qué alimenta en la corrección final |
|---|---|---|---|---|---|
| 1 | Fonético y fonológico | Sílabas por frase y su variación, cadencia final (aguda, llana, esdrújula), rima asonante entre frases consecutivas, aliteración | Parcial (no se mide verso accidental) | 33 (síncopa), 36.8 (ritmo) | Alarma de ritmo silábico; cadencia final repetida |
| 2 | Morfológico | Categorías, tiempo, modo, persona y número con el analizador | Medido | 28 (tiempos), 2 (presente), 36.8 | Perfil nominal/verbal; tiempo y persona por pieza |
| 3 | Sintáctico | Árbol de dependencias: profundidad, distancia, verbos finitos y subordinadas por frase, tipo de sujeto, pasivas, gerundios por clase | Medido | 10, 33, 38.1 bis, 47 | Continuidad del sujeto; subordinación; gerundio |
| 4 | Léxico (lexicometría) | Densidad léxica, MATTR, hápax, repetición local, abstractos | Medido | 36.8 (abstracción), 21, 36 | Alarma de densidad y abstracción |
| 5 | Textualidad (cohesión y coherencia) | Solape léxico con la frase anterior, conectores por clase, continuidad de sujeto. La coherencia lógica es lectura | Parcial | 38 (muleta de apertura), 25 y 43 (subtítulos) | Tejido conectivo; saltos sin enlace |
| 6 | Semántico | Lectura guiada: términos propios con más de un sentido sin declarar | Lectura | VIII bis, 12, 13, glosario | Aviso de ambigüedad; glosa que falta |
| 7 | Temático | Lectura guiada: tema principal y hasta tres subtemas; deriva | Lectura | 25, 43, 39, 29 | Comprobación contra título y subtítulos |
| 8 | Estructural y estilístico | Párrafo, cierres, enumeraciones, símiles, preguntas, anáfora; la arquitectura macro es lectura | Parcial | 7, 26, 31, 36.7, 39, 42, 46 | Alarmas de recursos; ratio de secciones |
| 9 | Legibilidad y complejidad | Fernández Huerta, Szigriszt-Pazos (INFLESZ), sílabas por palabra, palabras de 4+ sílabas | Medido | 21, 36.8 | Contraste con la banda del registro |
| 10 | Pragmático | Lectura guiada + marcadores (imperativos, segunda persona, condicional, cautelas) | Lectura | 0 (Norma Cero), 30, XXV, 32 | Autojustificación y petición de permiso |
| 11 | Discurso y discurso crítico | Lectura guiada: voz de las fuentes, sesgos, relaciones de poder | Lectura | 14, 19, 11, 13 | Sesgo y atribución |
| 12 | Intención | Lectura guiada: intención dominante de la pieza y su coherencia con el registro | Lectura | 13, `(*-red)` | Registro de la pieza |
| 13 | Narratológico | Persona, tiempo, sujeto-actor, diálogo; el narrador es lectura | Parcial | VIII quater, 47, 28 | Protagonistas y tiempo |
| 14 | Estilometría | Delta de Burrows con las 150 palabras más frecuentes | Medido | 36, 36.8 | Voz atípica de una pieza |
| 15 | Sentimiento | No se aplica (§3, dimensión 4) | No aplica | 45 (urgencia) | La urgencia se mide con indicadores formales |
| 16 | Entidades (NER) | Entidades por clase, frases con entidad o cifra | Medido | 36.1 (anclaje) | Sustituye a la heurística de anclaje |
| 17 | Sinteticidad | Ráfaga (variación de la longitud de frase); la perplejidad exige un modelo de lenguaje y no se calcula | Parcial | 36, 33 | Alarma de ráfaga |
| 18 | Plantillas | Esqueleto gramatical repetido, aperturas repetidas, 4-gramas repetidos | Medido | 38.1 bis (plantilla), 36.7, 38.2 | Alarma de molde |

Lectura guiada significa que Claude responde por pieza a un guion fijo de preguntas (§2, paso 4) y solo enseña a Luis lo que levanta una bandera.

---

## 2. El Pase de análisis final (propuesta)

Se hace pieza a pieza en el momento final de cada capítulo (el mismo momento de la auditoría de glosa, `(*-glo)`), después del Pase automático único (N1, N3, 38.1 bis, 36.7, 46, 47, cuerpo limpio, 28).

1. **Medir.** `perfil-corpus.py --pieza X` y `analisis-texto.py --pieza X`. Salen las alarmas de la Norma 36.8 y las 17 alarmas de este marco, con la dirección en que saltan.
2. **Diagnosticar por tipo y no frase a frase.** Claude agrupa lo que salta en cinco familias: continuidad del sujeto y aperturas (3, 18), dos puntos (norma propia, §5), longitud y cola (1, 3), conectores y subordinación (5), gerundio (3). De cada familia enseña entre cinco y diez casos con su arreglo propuesto.
3. **Aplicar sin consulta lo aprobado.** Aprobados los casos de muestra, se aplica a toda la pieza, como se hizo con las Normas 36.7, 38.1 bis, 47 y 28 (Luis, 08/10/26). Norma 0 y Norma 48 mandan: si un arreglo baja la densidad mitopoética, se queda la cifra y se corrige otra cosa.
4. **Lectura guiada (análisis 6, 7, 10, 11, 12, 13).** Seis líneas por pieza, con estas preguntas:
   - *Semántico:* ¿hay un término propio (UR, URbe, la «T», frontera, archivo, memoria…) usado con dos sentidos sin declararlo? ¿Dónde se declara?
   - *Temático:* ¿cuál es el tema principal y cuáles los tres subtemas? ¿Coinciden con el título y los subtítulos?
   - *Pragmático:* ¿hay frases que piden permiso, se justifican o explican su propia decisión (Normas 0, 30 y XXV)? ¿Qué presupone la pieza que el lector ya sabe?
   - *Discurso:* ¿quién habla en cada pasaje (autor, fuente, comunidad)? ¿Hay vocabulario cargado o atribución de poder sin fuente (Normas 14 y 19)?
   - *Intención:* ¿informa, argumenta, propone, homenajea, impugna o juega? ¿Coincide con el registro de `(*-red)`?
   - *Narratológico:* ¿quién narra, en qué tiempo, y quién es el sujeto de las frases importantes? Los datos de persona y tiempo salen de la herramienta.
5. **Voz.** Si la distancia de Burrows de la pieza al perfil medio de UR pasa de 0,7, se avisa: ¿voz atípica intencional (otro registro, otra mano) o pendiente de unificar?
6. **Decisión de Luis y re-medición.** Tras corregir, se vuelve a medir y se anota en el ledger la cifra antes y después.

---

## 3. Resultados por dimensión

Las tablas completas (80 indicadores) están en el Anexo A. Cifras: mediana de UR frente a mediana del canon (Baroja y Orwell), salvo indicación.

### Dimensión 1 · Lingüística estructural (el esqueleto)

**1 · Fonético y fonológico.**
- Las frases de UR tienen 36 sílabas de media (canon 40) y varían menos: desviación de 18,4 sílabas frente a 22,9; el 40 % de las ventanas de UR queda bajo el p10 del canon. Es el mismo hallazgo de ritmo que en palabras (desviación de frase 8,5 frente a 11,8).
- Cadencia final. El 7,9 % de las frases de UR acaba en palabra esdrújula (canon 4,2 %; 11,6 % en las piezas teóricas) y el 18,6 % en aguda (canon 16,7 %). Las esdrújulas finales son sobre todo adjetivos y sustantivos cultos: *política* (14), *histórica* (8), *tránsito* (8), *jurídica* (7), *máquina* (7). Es la cadencia del vocabulario técnico y se oye como un cierre uniforme.
- La rima asonante entre frases consecutivas (6,2 % frente a 6,7 %) y la aliteración (5,5 pares por cien palabras frente a 5,1) quedan al nivel del canon. No hay rima involuntaria.
- No medido: los versos accidentales (endecasílabos o alejandrinos escondidos en la prosa).

**2 · Morfológico.**
- UR es nominal: sustantivos 26,4 por cien palabras (canon 20,8; el 88 % de las ventanas sobre el p90), determinantes 19,0 (15,5), verbos 14,0 (16,3; el 42 % de las ventanas bajo el p10), pronombres 3,6 (7,0; el 83 % bajo el p10), preposiciones 13,5 (16,2), adverbios 2,4 (4,8), conjunciones subordinantes 1,5 (2,6).
- Tiempo y persona. El 89 % de los verbos finitos va en presente (canon 8 %; Orwell expositivo 40 %; el extracto de Goldstein, 71 %), el 100 % en tercera persona (canon 98 %; *Homenaje* 88 %) y casi ninguno en subjuntivo o condicional (2,5 % y 0 %; canon 5,2 % y 2,4 %). El presente es de registro (crónica y tesis frente a novela de acción); es coherente con las Normas 2 y 28 y no pide corrección.
- Participios 0,3 por cien palabras (canon 1,0): casi no hay tiempos compuestos ni pasivas (2,6 por mil frente a 5,0).

**3 · Sintáctico.**
- Estructura: 1,8 verbos finitos por frase (canon 2,2; Orwell expositivo 2,5), 1,1 subordinadas (1,5; 1,8), distancia media de dependencia 2,2 (2,6). La profundidad del árbol es normal (4,3 frente a 4,4). UR no es sintácticamente más compleja que el canon; es más plana.
- Sujeto de la oración principal. Artículo + sustantivo: 46 % (canon 23 %; Orwell expositivo 28 %); artículo + abstracto: 8,4 % (1,8 %; 6,0 %); pronombre: 0 % (5,2 %); omitido: 8,8 % (28,3 %; 23,0 %). El 76 % de las ventanas de UR supera el p90 del canon en artículo + sustantivo y el 90 % queda bajo el p10 en sujeto omitido.
- Lectura: el castellano continúa hablando del mismo sujeto con elipsis o pronombre; UR repite el sustantivo con su artículo en cada frase. Es la causa más directa del 50 % de aperturas con artículo.
- Gerundios: ver §7.

**4 · Léxico.**
- Densidad léxica (palabras con significado) 55,5 % frente a 49,7 %: el 93 % de las ventanas sobre el p90. La riqueza es normal: MATTR 0,5 como el canon; hápax y repetición local dentro del corredor. El vocabulario no es pobre; la densidad alta es la otra cara del estilo nominal (pocos pronombres, preposiciones y conjunciones).
- Abstractos en -ción, -dad, -miento, -ncia: 4,2 por cien palabras (canon 1,7); 7,2 en las teóricas (Orwell expositivo 3,4).

**5 · Textualidad.**
- Solape léxico con la frase anterior: 1,4 % (canon 1,9 %); 18 % de las ventanas con más de lo normal de frases sin ninguna palabra en común con la anterior (82 % frente a 76 %). En la exposición de Orwell, ese dato es del 60 %: sus frases se enlazan más entre sí. En las teóricas de UR, 78 %.
- Conectores por mil palabras (mediana de UR, canon, Orwell expositivo): consecutivos 0,0 – 1,0 – 2,4; aditivos 1,0 – 1,8 – 3,7; causales 0,7 – 1,5; adversativos 2,5 – 6,4.
- Continuidad del sujeto con la frase anterior: 0 % (canon 3,6 %).
- Lectura: UR enlaza por repetición del artículo y por dos puntos y deja sin decir la relación lógica entre frases. Coherente con §5.

### Dimensión 2 · Lingüística cognitiva y de contenido (el cerebro)

**6 · Semántico (lectura guiada).** Los términos con más de un sentido son los propios de la tesis: *UR* (raíz, agua, símbolo, protagonista), *URbe*, *la «T»*, *frontera*, *archivo*, *memoria*, *río* (literal y simbólico). La Norma VIII bis ya manda declararlos una vez para todo el libro, y las Normas 12 y 13 separan homonimia, hecho y especulación. El pase comprueba que cada término se usa en el sentido declarado y que la glosa lo respalda donde hace falta rigor (Norma 18).

**7 · Temático (lectura guiada).** Una línea por pieza con el tema principal y hasta tres subtemas, contrastada con el título, los subtítulos (Normas 25 y 43) y el glosario. Señala la deriva (un subtema que se ha comido la pieza) y el dato huérfano (Norma 29).

**8 · Estructural y estilístico.**
- Recursos: símiles 22,9 por 10.000 (canon 15,0), cierres aforísticos 2,5 % de los párrafos (canon 1,9–5,8 %), enumeraciones 12,8 % (12,7 %), preguntas 0 (0), exclamaciones 0 (0) y paréntesis dentro del corredor (una vez excluidas las llamadas de glosa); las rayas superan el p90 del canon en el 15 % de las ventanas. Todo en rango, como en el informe anterior.
- Anáfora: el 10,7 % de las frases abre con la misma palabra que la anterior (canon 2,6 %; el 69 % de las ventanas sobre el p90; 15,8 % en las teóricas). Es la racha de artículos de la Norma 38.1 bis medida de otra manera: *El… El… La… La…*
- La arquitectura macro (Norma 7, Norma 39 de ratio de secciones) se lee en el pase.

**9 · Legibilidad.**

| Banda INFLESZ | Lectura |
|---|---|
| menos de 40 | muy difícil |
| 40 – 55 | algo difícil |
| 55 – 65 | normal |
| 65 – 80 | bastante fácil |
| más de 80 | muy fácil |

- UR: INFLESZ 57,2 (banda normal), Fernández Huerta 74,3. Canon: 61,4 y 80,7 (Baroja 63–68; Orwell 55–61; *Homenaje* 55). Las piezas de crónica de UR se leen tan fácilmente como *Homenaje a Cataluña*.
- Piezas teóricas: INFLESZ 47,8 (algo difícil), Huerta 60,9. La exposición de Orwell: 48,6 y 75,3. Con el mismo INFLESZ, las teóricas de UR tienen palabras más largas (2,3 sílabas por palabra frente a 2,1; el 20 % de las palabras con cuatro sílabas o más frente a 16,6 %) y frases más cortas: el INFLESZ premia las frases cortas y oculta que las palabras son más largas.

### Dimensión 3 · Lingüística social y contextual (el entorno)

**10 · Pragmático (lectura guiada + marcadores).** Marcadores de la herramienta: imperativos 10,2 por 10.000 en las teóricas (Orwell expositivo 3,2; el 18 % de las ventanas de UR sobre el p90), segunda persona 0,5 %, condicional 0 %, cautelas (*quizá, tal vez, parece que*) 0 (canon 0–12). UR afirma, de acuerdo con la Norma Cero y la 30. El pase busca lo contrario: frases que se justifican o piden permiso (Norma XXV) y presuposiciones que el lector no comparte.

**11 · Discurso y discurso crítico (lectura guiada).** Quién habla en cada pasaje, con qué fuente, y qué vocabulario carga sentido o poder sin fuente. Enlaza con la Norma 14 (contra la moralina) y la 19 (contra el buen salvaje), y pesa sobre todo en las piezas de antropología, colonialismo y tecnopolítica.

**12 · Intención (lectura guiada).** Una intención dominante por pieza: informar, argumentar, proponer, homenajear, impugnar o jugar (dadá). Se contrasta con el registro de `(*-red)` y con la Norma 13. Marca la pieza que deriva de una a otra (por ejemplo, informar que acaba exhortando).

**13 · Narratológico.**
- Narrador impersonal: 100 % de los verbos finitos en tercera persona; primera persona del 0 % (canon 1,5 %; *Homenaje* 12,5 %), salvo en entrevistas e interludios.
- Sujeto-actor (Norma 47): el sujeto principal es un nombre propio en el 20 % de las frases (canon 14 %). Los protagonistas ya aparecen como sujeto; falta que lo hagan sin repetir artículo (§6).
- Diálogo: 0 %, frente al 3–48 % de las obras del canon. La variedad de voz de UR viene de los registros.

### Dimensión 4 · Forense y de inteligencia artificial (la huella)

**14 · Estilometría (Delta de Burrows).**
- El perfil medio de UR dista 0,62–0,73 de cada obra del canon. Entre las obras del canon la distancia va de 0,23 (dos novelas de Baroja) a 0,57 (*Rebelión* y Martín Santos): UR queda algo más lejos de cada obra que Baroja de Orwell (0,48–0,55).
- «Obra más cercana» no informa: la frecuencia de las palabras más comunes depende del tiempo verbal y del registro, y esa elección sale casi siempre en una novela de Baroja o en Martín Santos.
- Lo que sí sirve es la voz interna: las piezas más alejadas del perfil medio de UR (Delta) son Bonus Tracks · Sulfuro (0,91), Prólogo por Claude (0,85), Sájaura (0,74), Siouxsie (0,74), Rêv-E-UR (0,73), América · Ania (0,70), Ciclo hídrico (0,70), Epílogo (0,66), Whanganui (0,64), Euskal Herria · Amaia (0,62), TUR · Un continente en tránsito (0,62) y Frontera aquitano-celta (0,61). Las más cercanas: Ürmüz, Historia de la educación victoriana, Antropología racial, TUR · La raíz preindoeuropea, Babel y Filipinas.
- Sulfuro, Sájaura y América son tres de las cinco piezas que concentran «no… sino»: la coincidencia sugiere piezas de otra mano o de otro momento de redacción.

**15 · Sentimiento: no se aplica.** Exige un léxico de polaridad que no está disponible para este registro, y la ironía, el humor, el mito y el vocabulario técnico de UR lo falsean. La emoción que interesa a Luis, la urgencia de The Clash (Norma 45), se mide con indicadores formales: frases de ocho palabras o menos (19,1 % frente a 16,8 %), exclamaciones (0), imperativos. Si Luis quiere una lectura de la temperatura emocional por sección, entra en el pase como lectura (análisis 12).

**16 · Entidades.**
- Entidades por cien palabras 6,6 (canon 5,6). Por clase: lugares 1,8 (0,9; el 48 % de las ventanas sobre el p90), otras (obras, pueblos, conceptos) 3,0 (2,1), personas 0,9 (2,0; el 25 % bajo el p10), organizaciones 0,2. Cifras: 0,2 por cien palabras (0,0).
- Lectura: el anclaje de UR es de lugares y conceptos y no de personas. Es lo esperable en un libro cuyos protagonistas no son personas, y no pide corrección.
- Cautela: el reconocimiento de entidades del analizador es ruidoso en prosa literaria.

**17 · Sinteticidad.**
- La perplejidad (qué predecible es la siguiente palabra) exige un modelo de lenguaje y no se calcula.
- Ráfaga: coeficiente de variación de la longitud de frase 0,5 (canon 0,6); el 31 % de las ventanas bajo el p10. El salto medio entre frases consecutivas es normal.
- Repetición literal: 0,4 % de las secuencias de cuatro palabras (canon 0,7 %), dentro del corredor.
- El *Prólogo por Claude* no salta ninguna de las 17 alarmas del marco (Anexo B). Las alarmas no detectan «texto de IA»; miden moldes sintácticos concretos que Luis ha pedido evitar.

**18 · Plantillas (ingeniería inversa).**
- Esqueleto gramatical de las cuatro primeras palabras repetido cuatro o más veces en la ventana: 18,4 % de las frases de UR (canon 0 %, p90 7,7 %; el 72 % de las ventanas de UR sobre el p90; 28 % en las teóricas; Orwell expositivo 1,4 %).
- Los cuatro moldes más repetidos, sobre las 6.120 frases del cuerpo:

| Molde (cuatro primeras palabras) | Frases | % del libro | Ejemplo |
|---|---:|---:|---|
| artículo + sustantivo + verbo + artículo | 477 | 7,8 | *El agua evita la línea recta.* |
| artículo + sustantivo + verbo + preposición | 337 | 5,5 | *Este libro argumenta con fuerza y, en la frase siguiente, se pone un límite.* |
| artículo + sustantivo + adjetivo + verbo | 278 | 4,5 | *La energía solar sostiene el movimiento.* |
| artículo + sustantivo + pronombre + verbo | 224 | 3,7 | *Un libro que declara sus límites en voz alta es más fiable que uno que pretende no tenerlos.* |

- Dos primeras palabras repetidas tres o más veces: 4,5 % (canon 0 %).
- Lectura: el texto no se copia a sí mismo; repite el molde de frase. Es la Norma 38.1 bis («plantilla») medida con un instrumento que no depende de reconocer el sustantivo.

---

## 4. El hallazgo central: estilo nominal, de origen

| Rasgo | UR | Canon | Orwell, exposición |
|---|---:|---:|---:|
| Sujeto principal: artículo + sustantivo | 46 % | 23 % | 28 % |
| Sujeto principal: omitido | 9 % | 28 % | 23 % |
| Sujeto principal: pronombre | 0 % | 5 % | 7 % |
| Sustantivos por 100 palabras | 26,4 | 20,8 | 20,6 |
| Verbos por 100 palabras | 14,0 | 16,3 | 14,5 |
| Verbos finitos por frase | 1,8 | 2,2 | 2,5 |
| Subordinadas por frase | 1,1 | 1,5 | 1,8 |
| Pronombres por 100 palabras | 3,6 | 7,0 | 5,8 |
| Esqueleto repetido (% de frases) | 18 % | 0 % | 1 % |
| Conectores consecutivos por 1.000 | 0,0 | 1,0 | 2,4 |

**Prueba de la hipótesis de sobrecorrección: descartada.** La hipótesis era que las normas, al retirar dispositivos (conectores correctivos con la Norma 1, gerundios con la 10, condicionales con la 32, cierres con la 31), habrían empujado el texto al estilo nominal. Se midieron las 42 piezas que existen igual en los cuatro cortes del historial de `urtz.html`:

| Corte | Sujeto art.+sust. | Sujeto omitido | Subordinadas/frase | Verbos finitos/frase | Esqueleto repetido | Gerundios/10.000 |
|---|---:|---:|---:|---:|---:|---:|
| 09/09/26 | 43,8 | 11,5 | 1,2 | 1,9 | 22,4 | 29,7 |
| 23/09/26 | 43,8 | 11,5 | 1,2 | 1,9 | 22,4 | 29,7 |
| 03/10/26 | 43,7 | 11,4 | 1,2 | 1,9 | 22,4 | 29,4 |
| 08/10/26 | 43,7 | 11,4 | 1,2 | 1,9 | 22,4 | 29,4 |

El perfil estaba desde el 09/09 y no se ha movido. Es el perfil del borrador de origen. Sirve de línea base: toda corrección sistemática debe verse en esta tabla.

**Lectura.** Dos conclusiones. Primera, las normas no son la causa y no hay que tocarlas por esto. Segunda, el pase pieza a pieza hecho hasta ahora no ha movido el perfil de conjunto: lo que se corrige son casos, no el patrón. El patrón se corrige con la familia de arreglos aditivos de §6.

**Piezas con más y menos alarmas** (17 alarmas, Anexo B). Menos: Prólogo (0); Sulfuro, Entrevista a Nexus-7, Euskal Herria · Amaia y Sájaura (4); Frontera aquitano-celta (6). Más: IV · I. El dique del silencio (16); Quelccaya, Te Urewera y Whanganui (15); Islandia III, Pla-UR, Siouxsie, TUR · Un continente en tránsito y TUR · La dama de marfil (14). IV · II tiene 9. La distribución completa va de 0 a 16, con mediana 10.

---

## 5. Los dos puntos: datos, borrador de norma y soluciones clásicas

*(Para la decisión 2 del informe anterior y la petición de Luis del 08/10/26: una norma específica y soluciones de puntuación más clásicas y sencillas.)*

### 5.1 Qué dicen los datos

Por 1.000 palabras de narración, con el analizador (`analisis-texto.py --dospuntos`):

| Clase | Canon | UR, resto | UR, teóricas |
|---|---:|---:|---:|
| **Cláusula + cláusula** («A: B», las dos con verbo) | 0,7 – 1,6 | **6,7** | **4,8** |
| Complemento (aposición o lista corta) | 0,3 – 2,8 | 1,3 | 1,6 |
| Enumeración | 0,03 – 0,24 | 1,0 | 0,7 |
| Cita | 0,07 – 0,82 | 0,09 | 0 |
| Rótulo (tres palabras o menos) | 0,0 – 0,21 | 0,42 | 0,21 |
| Rótulo largo + cláusula | 0,0 – 0,06 | 0,28 | 0,14 |
| **Total** | **2,4 – 4,2** | **9,7** | **7,4** |

El 68 % de los 966 dos puntos unen dos cláusulas con verbo. La exposición de Orwell usa entre 0,9 y 3,0 por mil en total. Luis lo describió como un tic artificial que puede ayudar en el campo teórico y ser muy evitable en la narración: los datos lo confirman en las dos mitades (en crónica 6,7 de cláusula + cláusula; en teóricas 4,8, menos pero también alto).

### 5.2 Borrador de norma (Norma 42 bis)

> **Norma 42 bis — Los dos puntos anuncian; no explican.**
>
> **Se quedan:** (1) anunciar una enumeración o lista; (2) anunciar una cita; (3) rótulo o definición en glosa, tabla o pieza teórica («X se define así: …»), como máximo una vez por sección; (4) la pregunta o el enunciado que el párrafo siguiente desarrolla, en las piezas teóricas.
>
> **Cláusula + cláusula:** no se sustituye por sistema. Cada caso se decide por sus motivos (se queda si B es la demostración breve de A, si A es una tesis y B su prueba, o si sustituir empeora la frase; se sustituye si hay racha, si la relación lógica no se dice en otro sitio, si es un molde repetido o si B pide punto). *Aprobada el 09/10/26 con esta modificación; texto definitivo en `NORMA-METODO.md`, Norma 42 bis.*
>
> **Soluciones clásicas, según lo que B hace con A:**
>
> | B es… | Se escribe con… | Ejemplo de forma |
> |---|---|---|
> | la causa de A | *porque*, *pues*, *ya que* | «A, porque B» |
> | la consecuencia de A | *de modo que*, *así*, *por eso*, o punto y coma | «A; de modo que B» |
> | una aclaración o concreción | *es decir*, *esto es*, *en concreto*, o paréntesis o rayas con el dato | «A, es decir, B» |
> | un contraste o precisión | punto y coma, *pero*, *aunque* | «A; B» |
> | una frase que se sostiene sola y es corta | punto y seguido | «A. B.» (la síncopa de The Clash) |
> | una aposición del nombre | comas o rayas | «A, B, …» |
> | el binomio «El pretexto: X. La realidad: Y.» | punto y coma con elipsis del verbo | «El pretexto fue X; la realidad, Y.» |
>
> **Medida (instrumento de Claude):** en crónica y geografía, más de 5 dos puntos por mil o más de 1,6 de cláusula + cláusula; en teóricas, más de 6 y más de 3. Meta de libro: 4 por mil.
>
> **Aplicación:** muestra de diez a veinte casos con su motivo y su arreglo; aprobados, se aplica sin consulta al resto de la pieza.

La mayoría de las soluciones alarga la frase y añade conectores, justo lo que faltaba (§3, análisis 5 y §6): resuelven dos desvíos con un cambio.

### 5.3 Ejemplos de forma

Tomados de los ejemplos que muestra el analizador; ilustran el arreglo, no modifican el libro (las piezas siguen intactas).

- *«El pretexto: una reserva de caza. La realidad: un tajo sobre el mapa que cortó el paso al lago.»* → *«El pretexto fue una reserva de caza; la realidad, un tajo sobre el mapa que cortó el paso al lago.»* (punto y coma con elipsis).
- *«La cercanía de las dos palabras permite una imagen precisa: el larre deja el UR libre sobre la hierba; el laratz lo levanta sobre el fuego.»* → *«La cercanía de las dos palabras permite una imagen precisa, pues el larre deja el UR libre sobre la hierba y el laratz lo levanta sobre el fuego.»* (causa).
- *«Es otra cosa, y me parece más interesante: es la prueba de que esa intuición no nacía del vacío.»* → *«Es otra cosa, y me parece más interesante, porque es la prueba de que esa intuición no nacía del vacío.»* (causa).

---

## 6. Alargar frases sin perder The Clash

*(Petición de Luis del 08/10/26: ampliar las frases, teniendo en cuenta la urgencia de The Clash, Norma 45.)*

**Lo que dicen los datos.** Las frases cortas de UR están al nivel del canon (19,1 % de ocho palabras o menos frente a 16,8 %). La urgencia de The Clash está intacta y no se toca. Falta la cola larga: 1,3 % de las frases pasa de 40 palabras (canon 5,8 %; p10 2,5 %) y el techo de frase está en 29 palabras (canon 35). Martín Santos muestra cómo conviven las dos cosas: el 38 % de sus frases tiene ocho palabras o menos y el 17 % tiene 41 o más.

**Meta orientativa:** de 1,3 % a 4–5 % de frases de más de 40 palabras (una de cada veinticinco), sin quitar una sola frase corta que se la gane (Norma 26: cambio de escala, imagen decisiva, cierre con presión).

**Caja de herramientas aditivas, por orden de preferencia:**
1. **Elipsis del sujeto.** Si la frase siguiente habla del mismo sujeto, el verbo va solo: *«El Baztán recoge la lluvia y la reparte entre tres cuencas»* (ejemplo de forma). Resuelve a la vez la apertura con artículo, el sujeto repetido y el esqueleto.
2. **Pronombre o aposición** para retomar al protagonista sin repetir artículo + sustantivo.
3. **Subordinada con dato:** causal (*porque*), concesiva (*aunque*), temporal (*cuando*, *mientras*) o consecutiva (*de modo que*). Cada una trae una relación que hoy se calla.
4. **Relativa con dato** (*que* + verbo) en lugar de dos frases con el mismo molde.
5. **Gerundio de manera o simultaneidad:** permitido por la Norma 10 y casi ausente hoy (§7).
6. **Punto y coma** entre dos afirmaciones emparentadas (UR lo usa a nivel del canon: 5,8 por mil frente a 4,5; admite algo más).

**Cuándo alargar:** donde hoy hay dos o tres frases cortas seguidas con el mismo molde (esqueleto repetido), y en el punto de más carga de datos del párrafo. No se alarga una frase suelta por alargar.

**Límites:** no se alarga con relleno, adjetivos ni *es decir* vacío; no se alarga con gerundio de posterioridad (Norma 10), con cadenas de tres cláusulas del mismo molde (Norma 36.7) ni con «no X, sino Y» (Norma 1). La elipsis encadena como máximo dos verbos; el tercero va en frase nueva con otra apertura.

**Borrador de norma (38.1 ter — Continuidad del sujeto):**

> Cuando la frase sigue hablando del mismo sujeto que la anterior, el sujeto se elide o se retoma con pronombre o aposición. Repetir «artículo + sustantivo» es el último recurso y necesita motivo (Norma 38.1 bis). El protagonista se nombra al abrir el párrafo o la sección (Norma 47) y la continuidad la lleva el verbo. Alarma: más del 35 % de sujetos principales con «artículo + sustantivo» (p90 del canon 35,5), o menos del 18 % de sujetos omitidos (p10 del canon).

---

## 7. Gerundios: respuesta a la duda sobre la Norma 10

**La norma es buena y hace su trabajo.** Tres datos:

1. El patrón que persigue (gerundio posterior tras coma: *«…desplazó el vertedero, provocando la miseria»*) baja a 5,5 por 10.000 (canon 12,6) en el libro y a 0 en las piezas teóricas.
2. La norma protege expresamente el gerundio de manera, simultaneidad y condición, y deja decidir con la prueba «¿cabe sustituirlo por *y luego*?».
3. La perífrasis (*estar, ir, seguir* + gerundio) se conserva casi entera: 4,7 frente a 6,3.

**Lo que sugieren los datos** es una práctica algo más estricta que la norma: los gerundios de manera y los antepuestos son los más reducidos (0,18 y 0,09 del canon), y en la exposición teórica Orwell sigue usándolos (20,2 por 10.000 de «otros») y UR no (0,0). Parte de esa diferencia es de género, pero ese es el hueco del que sale la herramienta número 5 de §6.

**Propuesta mínima:** ninguna alarma ni cambio de norma. Una línea de recordatorio en la Norma 10 (el gerundio de manera y simultaneidad es herramienta para alargar frases) y, en la revisión final, un chequeo: menos de 25 por 10.000 en una pieza, se pregunta si la norma se ha aplicado de más.

El análisis es estadístico y la clasificación por clase aproximada; la cifra orienta y no sustituye la prueba del «y luego».

---

## 8. Integración propuesta en `NORMA-METODO.md`

Texto propuesto para una sección nueva, que se redactaría tras las decisiones de Luis:

> **XXVII. MARCO DE ANÁLISIS TEXTUAL — LOS 18 ANÁLISIS EN CUATRO DIMENSIONES**
>
> 1. **Qué es.** El conjunto de análisis con que se revisa una pieza en el momento final de su capítulo. Se agrupan en cuatro dimensiones (estructural, cognitiva y de contenido, social y contextual, forense) y se reparten en tres tipos: medido por herramienta, medido en parte, lectura guiada. La tabla de los 18 y su estado está en `MARCO-ANALISIS-TEXTUAL.md`, §1.
> 2. **El corredor del canon.** Baroja y Orwell son el suelo llano del español narrativo; Martín Santos, el pico licenciado. El corredor es un diagnóstico, no una cuota (Norma 0). Se aplica según el registro de la pieza (`(*-red)`), y ninguna cifra autoriza una corrección que rebaje la densidad mitopoética (Norma 48).
> 3. **El Pase de análisis final.** Seis pasos: medir, diagnosticar por tipo, aplicar lo aprobado, lectura guiada, voz, decisión y re-medición (`MARCO-ANALISIS-TEXTUAL.md`, §2).
> 4. **Alarmas.** Las de la Norma 36.8 más las 17 del marco (sujeto, sintaxis, léxico, ráfaga, plantillas). Cada alarma lleva su dirección y se compara con el canon.
> 5. **Línea base.** Medición del 08/10/26 sobre 66 piezas. Una corrección sistemática se evalúa contra esa línea.
> 6. **Cautelas.** El analizador es estadístico; Orwell está en traducción; las cifras orientan.

---

## 9. Decisiones nuevas para Luis

Se suman a las nueve del informe anterior. Para cada una, mi recomendación.

10. **Norma 42 bis (dos puntos).** *Cerrada el 09/10/26:* aprobada con la modificación de Luis (la cláusula + cláusula se decide por motivos, no por sistema). Escrita en `NORMA-METODO.md`.
11. **Norma 38.1 ter (continuidad del sujeto).** *Cerrada el 09/10/26:* aprobada; texto definitivo en `NORMA-METODO.md`, Norma 38.1 ter.
12. **Alargar frases.** *Cerrada el 09/10/26:* aprobada por Luis; escrita como adenda de la Norma 33.
13. **Pase de análisis final.** *Cerrada el 09/10/26:* aprobada por Luis; escrita como sección XXVII de `NORMA-METODO.md`.
14. **Línea base.** *Cerrada el 09/10/26:* aprobada por Luis; medición en `LINEA-BASE-2026-10-08.md` y formato de «antes y después» en `analisis-editorial.md`.

---

## Anexo A · Tabla completa de indicadores

Canon: ventanas de 1.000 palabras de las seis obras de Baroja y Orwell (270 ventanas). UR: 104 ventanas de las 66 piezas. «Orwell, exposición»: media de tres pasajes expositivos (el «libro» de Goldstein y el apéndice del neolengua en *1984*; cuatro trozos de contenido político de *Homenaje*). «UR, 9 piezas teóricas»: I, II, III×3, IV×2, Digitalismo y Antropología racial. (La lista de teóricas se amplió el 09/10/26 con Río Congo y, provisionalmente, la Introducción; las cifras de esta tabla corresponden a las nueve originales. La herramienta ya usa la lista nueva.)

#### 1 · Fonético y fonológico

| Indicador | Canon: p10 – p50 – p90 | UR: p10 – p50 – p90 | % ventanas de UR bajo p10 / sobre p90 | Orwell, exposición (media) | UR, 9 piezas teóricas (media) |
|---|---|---|---|---:|---:|
| sílabas por frase (media) | 30,5 – 40,2 – 53,2 | 28,3 – 36,1 – 48,4 | 21 / 3 | 54,9 | 34,8 |
| sílabas por frase (desviación) | 17,4 – 22,9 – 32,3 | 14,2 – 18,4 – 24,8 | 40 / 1 | 28,9 | 18,3 |
| % de frases que acaban en palabra aguda | 11,0 – 16,7 – 23,9 | 11,1 – 18,6 – 28,5 | 10 / 32 | 19,7 | 22,9 |
| % de frases que acaban en esdrújula | 0,0 – 4,2 – 9,1 | 2,7 – 7,9 – 15,6 | 0 / 37 | 5,5 | 11,6 |
| % de frases que riman en asonante con la anterior | 2,3 – 6,7 – 12,1 | 1,8 – 6,2 – 10,9 | 14 / 7 | 7,2 | 5,6 |
| aliteración (pares por 100 palabras) | 4,1 – 5,1 – 6,2 | 4,4 – 5,5 – 6,9 | 5 / 26 | 5,6 | 6,5 |

#### 2 · Morfológico

| Indicador | Canon: p10 – p50 – p90 | UR: p10 – p50 – p90 | % ventanas de UR bajo p10 / sobre p90 | Orwell, exposición (media) | UR, 9 piezas teóricas (media) |
|---|---|---|---|---:|---:|
| sustantivos por 100 palabras | 18,9 – 20,8 – 22,9 | 22,7 – 26,4 – 29,4 | 1 / 88 | 20,6 | 27,4 |
| verbos por 100 palabras | 13,4 – 16,3 – 19,0 | 10,7 – 14,0 – 18,0 | 42 / 6 | 14,5 | 16,5 |
| adjetivos por 100 | 5,4 – 7,2 – 9,4 | 5,6 – 8,2 – 11,5 | 10 / 32 | 9,6 | 9,4 |
| adverbios por 100 | 3,3 – 4,8 – 6,3 | 1,3 – 2,4 – 4,8 | 67 / 4 | 5,0 | 3,2 |
| preposiciones por 100 | 14,4 – 16,2 – 17,9 | 11,5 – 13,5 – 16,8 | 66 / 1 | 16,2 | 11,9 |
| determinantes por 100 | 13,7 – 15,5 – 17,0 | 15,9 – 19,0 – 21,5 | 2 / 83 | 15,2 | 18,8 |
| pronombres por 100 | 5,3 – 7,0 – 8,7 | 2,3 – 3,6 – 5,8 | 83 / 2 | 5,8 | 3,5 |
| conjunciones coordinantes por 100 | 3,4 – 4,2 – 5,3 | 2,5 – 3,7 – 4,8 | 32 / 3 | 4,0 | 3,7 |
| conjunciones subordinantes por 100 | 1,6 – 2,6 – 3,5 | 0,8 – 1,5 – 2,7 | 59 / 1 | 3,1 | 1,9 |
| nombres propios por 100 | 1,8 – 4,2 – 7,3 | 1,5 – 5,1 – 9,4 | 12 / 19 | 5,1 | 3,2 |
| adjetivos por sustantivo | 0,3 – 0,4 – 0,4 | 0,2 – 0,3 – 0,5 | 26 / 12 | 0,5 | 0,3 |
| % de verbos finitos en presente | 1,8 – 7,6 – 39,8 | 57,4 – 88,8 – 97,5 | 0 / 96 | 40,1 | 85,5 |
| % en pasado (pretérito + imperfecto) | 55,7 – 88,9 – 96,1 | 1,4 – 8,9 – 42,3 | 96 / 0 | 54,1 | 11,0 |
| % en futuro | 0,0 – 0,0 – 1,6 | 0,0 – 0,0 – 1,3 | 0 / 8 | 1,4 | 0,6 |
| % en condicional | 0,0 – 2,4 – 5,7 | 0,0 – 0,0 – 1,7 | 0 / 3 | 4,1 | 2,1 |
| % en subjuntivo | 1,7 – 5,2 – 11,1 | 0,2 – 2,5 – 6,8 | 31 / 2 | 9,4 | 4,1 |
| % en primera persona | 0,0 – 1,5 – 13,4 | 0,0 – 0,0 – 2,2 | 0 / 1 | 4,6 | 0,5 |
| % en tercera persona | 86,5 – 98,4 – 100,0 | 96,1 – 100,0 – 100,0 | 2 / 0 | 95,2 | 99,0 |
| infinitivos por 100 | 1,9 – 3,0 – 4,1 | 1,0 – 2,4 – 4,2 | 35 / 15 | 3,2 | 4,4 |
| participios por 100 | 0,3 – 1,0 – 1,9 | 0,0 – 0,3 – 0,9 | 57 / 3 | 1,0 | 0,4 |

#### 3 · Sintáctico

| Indicador | Canon: p10 – p50 – p90 | UR: p10 – p50 – p90 | % ventanas de UR bajo p10 / sobre p90 | Orwell, exposición (media) | UR, 9 piezas teóricas (media) |
|---|---|---|---|---:|---:|
| profundidad máxima del árbol (media por frase) | 3,8 – 4,4 – 5,1 | 3,7 – 4,3 – 5,0 | 19 / 7 | 5,0 | 4,0 |
| distancia media de dependencia | 2,4 – 2,6 – 2,9 | 2,0 – 2,2 – 2,5 | 74 / 0 | 2,8 | 2,1 |
| verbos finitos por frase | 1,9 – 2,2 – 2,7 | 1,5 – 1,8 – 2,2 | 63 / 2 | 2,5 | 1,7 |
| subordinadas por frase | 1,1 – 1,5 – 1,9 | 0,6 – 1,1 – 1,6 | 46 / 4 | 1,8 | 1,0 |
| % de frases sin verbo finito | 0,0 – 0,0 – 3,8 | 0,0 – 0,0 – 4,8 | 0 / 16 | 0,9 | 1,3 |
| pasivas por 1.000 palabras | 2,0 – 5,0 – 9,6 | 0,0 – 2,6 – 5,9 | 46 / 4 | 7,1 | 3,0 |
| sujeto principal: % nombre propio | 2,8 – 14,1 – 32,1 | 7,2 – 20,0 – 31,6 | 3 / 10 | 10,2 | 14,9 |
| sujeto principal: % pronombre | 1,6 – 5,2 – 10,0 | 0,0 – 0,0 – 3,3 | 76 / 2 | 6,6 | 1,1 |
| sujeto principal: % artículo + sustantivo | 13,7 – 23,1 – 35,5 | 31,0 – 45,9 – 59,3 | 1 / 76 | 27,7 | 42,4 |
| sujeto principal: % artículo + abstracto | 0,0 – 1,8 – 5,8 | 2,6 – 8,4 – 17,0 | 0 / 68 | 6,0 | 15,4 |
| sujeto principal: % sustantivo sin artículo | 3,3 – 8,3 – 13,9 | 3,3 – 8,1 – 15,6 | 11 / 14 | 10,6 | 7,5 |
| sujeto principal: % omitido | 18,0 – 28,3 – 40,6 | 3,6 – 8,8 – 16,7 | 90 / 0 | 23,0 | 11,5 |
| gerundios por 10.000 | 22,7 – 59,2 – 110,2 | 0,0 – 19,3 – 54,5 | 64 / 0 | 40,9 | 11,1 |
| gerundio tras coma y tras su verbo (candidato Norma 10) por 10.000 | 0,0 – 9,2 – 30,3 | 0,0 – 0,0 – 19,1 | 0 / 5 | 5,2 | 0,0 |
| gerundio posterior sin coma por 10.000 | 0,0 – 17,1 – 39,1 | 0,0 – 0,0 – 25,8 | 0 / 1 | 9,4 | 5,5 |
| gerundio antepuesto por 10.000 | 0,0 – 0,0 – 16,1 | 0,0 – 0,0 – 0,0 | 0 / 0 | 1,1 | 0,7 |
| gerundio en perífrasis (estar, ir, seguir…) por 10.000 | 0,0 – 0,0 – 18,5 | 0,0 – 0,0 – 15,6 | 0 / 8 | 5,0 | 4,9 |
| otros gerundios por 10.000 | 0,0 – 19,6 – 47,2 | 0,0 – 0,0 – 18,3 | 0 / 0 | 20,2 | 0,0 |

#### 4 · Léxico

| Indicador | Canon: p10 – p50 – p90 | UR: p10 – p50 – p90 | % ventanas de UR bajo p10 / sobre p90 | Orwell, exposición (media) | UR, 9 piezas teóricas (media) |
|---|---|---|---|---:|---:|
| densidad léxica (% de palabras de contenido) | 47,7 – 49,7 – 51,5 | 52,3 – 55,5 – 58,4 | 1 / 93 | 50,2 | 56,9 |
| diversidad léxica (MATTR 500) | 0,5 – 0,5 – 0,6 | 0,5 – 0,5 – 0,6 | 9 / 22 | 0,5 | 0,5 |
| % de palabras distintas que aparecen una vez | 72,2 – 76,1 – 78,6 | 70,9 – 74,7 – 81,0 | 25 / 24 | 74,1 | 74,1 |
| % de palabras de contenido que repiten otra de las 50 anteriores | 10,7 – 14,5 – 19,2 | 7,0 – 13,0 – 18,3 | 26 / 7 | 15,6 | 16,3 |
| % de las palabras de contenido que son las 10 más usadas | 10,7 – 13,5 – 16,8 | 9,3 – 12,3 – 16,0 | 25 / 8 | 14,2 | 14,4 |
| abstractos (-ción, -dad…) por 100 | 1,0 – 1,7 – 2,9 | 2,4 – 4,2 – 7,0 | 0 / 81 | 3,4 | 7,2 |

#### 5 · Textualidad

| Indicador | Canon: p10 – p50 – p90 | UR: p10 – p50 – p90 | % ventanas de UR bajo p10 / sobre p90 | Orwell, exposición (media) | UR, 9 piezas teóricas (media) |
|---|---|---|---|---:|---:|
| solape léxico con la frase anterior (%) | 0,9 – 1,9 – 3,4 | 0,5 – 1,4 – 2,7 | 23 / 5 | 3,0 | 2,2 |
| % de frases sin ninguna palabra en común con la anterior | 59,5 – 76,0 – 88,7 | 69,9 – 81,8 – 92,4 | 2 / 18 | 60,1 | 77,8 |
| % de frases con el mismo sujeto que la anterior | 0,0 – 3,6 – 12,5 | 0,0 – 0,0 – 4,5 | 0 / 0 | 3,0 | 1,5 |
| demostrativos por 1.000 | 3,4 – 6,2 – 10,6 | 2,0 – 5,8 – 14,3 | 13 / 15 | 5,5 | 6,7 |
| conectores aditivos por 1.000 | 0,0 – 1,8 – 4,9 | 0,0 – 1,0 – 4,2 | 0 / 8 | 3,7 | 1,6 |
| conectores consecutivos por 1.000 | 0,0 – 1,0 – 2,9 | 0,0 – 0,0 – 2,6 | 0 / 8 | 2,4 | 0,8 |
| marcadores temporales por 1.000 | 4,8 – 9,1 – 14,6 | 2,9 – 8,6 – 14,4 | 18 / 8 | 7,3 | 8,5 |

#### 8 · Estilístico (recursos)

| Indicador | Canon: p10 – p50 – p90 | UR: p10 – p50 – p90 | % ventanas de UR bajo p10 / sobre p90 | Orwell, exposición (media) | UR, 9 piezas teóricas (media) |
|---|---|---|---|---:|---:|
| preguntas retóricas (¿) por 10.000 | 0,0 – 0,0 – 24,2 | 0,0 – 0,0 – 10,9 | 0 / 5 | 5,5 | 8,3 |
| exclamaciones (¡) por 10.000 | 0,0 – 0,0 – 29,9 | 0,0 – 0,0 – 0,0 | 0 / 0 | 1,7 | 0,0 |
| paréntesis por 10.000 | 0,0 – 0,0 – 21,9 | 0,0 – 0,0 – 16,9 | 0 / 9 | 17,2 | 2,7 |
| rayas por 10.000 | 0,0 – 0,0 – 44,3 | 0,0 – 0,0 – 59,3 | 0 / 15 | 42,5 | 9,3 |
| % de frases que abren con la misma palabra que la anterior | 0,0 – 2,6 – 7,3 | 3,2 – 10,7 – 20,1 | 0 / 69 | 3,3 | 15,8 |

#### 9 · Legibilidad

| Indicador | Canon: p10 – p50 – p90 | UR: p10 – p50 – p90 | % ventanas de UR bajo p10 / sobre p90 | Orwell, exposición (media) | UR, 9 piezas teóricas (media) |
|---|---|---|---|---:|---:|
| Fernández Huerta | 75,7 – 80,7 – 86,4 | 63,2 – 74,3 – 82,5 | 59 / 1 | 75,3 | 60,9 |
| Szigriszt-Pazos (INFLESZ) | 51,6 – 61,4 – 70,1 | 49,0 – 57,2 – 67,2 | 24 / 2 | 48,6 | 47,8 |
| sílabas por palabra | 1,9 – 2,0 – 2,1 | 2,0 – 2,1 – 2,3 | 2 / 53 | 2,1 | 2,3 |
| % de palabras de 4+ sílabas | 9,1 – 11,9 – 15,5 | 9,9 – 14,4 – 18,6 | 7 / 37 | 16,6 | 20,1 |

#### 10 · Pragmática y 13 · Narratología (marcadores)

| Indicador | Canon: p10 – p50 – p90 | UR: p10 – p50 – p90 | % ventanas de UR bajo p10 / sobre p90 | Orwell, exposición (media) | UR, 9 piezas teóricas (media) |
|---|---|---|---|---:|---:|
| imperativos por 10.000 | 0,0 – 0,0 – 9,4 | 0,0 – 0,0 – 16,0 | 0 / 18 | 3,2 | 10,2 |
| % de verbos en segunda persona | 0,0 – 0,0 – 0,9 | 0,0 – 0,0 – 1,2 | 0 / 12 | 0,2 | 0,5 |

#### 16 · Entidades

| Indicador | Canon: p10 – p50 – p90 | UR: p10 – p50 – p90 | % ventanas de UR bajo p10 / sobre p90 | Orwell, exposición (media) | UR, 9 piezas teóricas (media) |
|---|---|---|---|---:|---:|
| entidades por 100 palabras | 4,0 – 5,6 – 7,4 | 3,8 – 6,6 – 8,7 | 12 / 29 | 5,5 | 5,0 |
| personas por 100 | 0,4 – 2,0 – 4,0 | 0,2 – 0,9 – 1,8 | 25 / 0 | 1,0 | 1,0 |
| lugares por 100 | 0,4 – 0,9 – 1,9 | 0,3 – 1,8 – 3,9 | 12 / 48 | 1,1 | 0,6 |
| organizaciones por 100 | 0,0 – 0,2 – 1,0 | 0,0 – 0,2 – 0,6 | 0 / 3 | 1,3 | 0,2 |
| otras entidades por 100 | 1,3 – 2,1 – 3,0 | 1,9 – 3,0 – 4,5 | 0 / 50 | 2,1 | 3,3 |
| % de frases con entidad o cifra | 64,4 – 73,3 – 82,9 | 57,6 – 78,9 – 87,5 | 14 / 31 | 77,4 | 61,7 |
| cifras por 100 palabras | 0,0 – 0,0 – 0,5 | 0,0 – 0,2 – 1,3 | 0 / 32 | 0,4 | 0,3 |

#### 17 · Ráfaga y 18 · Plantillas

| Indicador | Canon: p10 – p50 – p90 | UR: p10 – p50 – p90 | % ventanas de UR bajo p10 / sobre p90 | Orwell, exposición (media) | UR, 9 piezas teóricas (media) |
|---|---|---|---|---:|---:|
| ráfaga: coeficiente de variación de la longitud de frase | 0,5 – 0,6 – 0,7 | 0,4 – 0,5 – 0,6 | 31 / 0 | 0,5 | 0,5 |
| ráfaga: salto medio entre frases consecutivas / longitud media | 0,5 – 0,6 – 0,7 | 0,5 – 0,6 – 0,7 | 19 / 4 | 0,5 | 0,6 |
| % de secuencias de 4 palabras que se repiten | 0,0 – 0,7 – 1,9 | 0,0 – 0,4 – 1,5 | 0 / 9 | 1,2 | 0,6 |
| % de frases con esqueleto gramatical repetido (≥4 veces) | 0,0 – 0,0 – 7,7 | 0,0 – 18,4 – 40,4 | 0 / 72 | 1,4 | 28,1 |
| % de frases cuyas dos primeras palabras se repiten (≥3 veces) | 0,0 – 0,0 – 8,2 | 0,0 – 4,5 – 15,8 | 0 / 29 | 1,7 | 9,8 |

---

## Anexo B · Matriz de las 66 piezas: alarmas del marco

Las 17 alarmas y su dirección: sujeto principal «artículo + sustantivo» ↑, «artículo + abstracto» ↑, sujeto pronombre ↓, sujeto omitido ↓, sustantivos ↑, verbos ↓, pronombres ↓, subordinadas por frase ↓, verbos finitos por frase ↓, esqueleto repetido ↑, aperturas de dos palabras repetidas ↑, anáfora de apertura ↑, paréntesis ↑, ráfaga ↓, variación silábica ↓, densidad léxica ↑, gerundios ↓. Una alarma salta cuando la media de las ventanas de la pieza queda fuera del corredor del canon en esa dirección.

| Pieza | Alarmas (de 17) | Cuáles |
|---|:-:|---|
| PRÓLOGO · por Claude (Anthropic) | 0 |  |
| BONUS TRACKS · SULFURO Y OSCURIDAD: EL UR ABISAL | 4 | suj_abstracto_art↑ s_fin_frase↓ l_densidad↑ g_total↓ |
| ENTREVISTA A NEXUS-7: UR PREGUNTA ¿QUIÉN ES UR? | 4 | suj_omitido↓ s_fin_frase↓ e_anafora↑ e_parent↑ |
| EUSKAL HERRIA · AMAIA · AMAIUR · MAIA · AMAYA: EL CONFÍN | 4 | suj_pronombre↓ suj_omitido↓ m_sust↑ l_densidad↑ |
| SÁJAURA · MAURITANIA · FUR | 4 | suj_art_sust↑ suj_omitido↓ m_verbo↓ l_densidad↑ |
| FRONTERA AQUITANO-CELTA: GUERRA EN LA GALIA | 6 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ m_verbo↓ m_pron↓ l_densidad↑ |
| INTRODUCCIÓN: CÍRCULO SIMBÓLICO — NATURA, UR Y ORIGEN | 6 | suj_art_sust↑ suj_abstracto_art↑ suj_omitido↓ m_sust↑ r_cv↓ l_densidad↑ |
| RÍO CONGO: NATURALEZA O SISTEMA | 6 | suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ l_densidad↑ g_total↓ |
| ANTÁRTIDA: EL HIELO PRIMORDIAL | 7 | suj_art_sust↑ suj_pronombre↓ suj_omitido↓ m_verbo↓ m_pron↓ s_fin_frase↓ l_densidad↑ |
| LA ESCOMBRERA SISTÉMICA | 8 | suj_art_sust↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ r_cv↓ l_densidad↑ |
| AMÉRICA · ANIA · ANAIA · UR EN EL ATLÁNTICO FRÍO | 9 | suj_art_sust↑ suj_abstracto_art↑ suj_omitido↓ m_sust↑ m_pron↓ s_fin_frase↓ r_cv↓ f_sil_sd↓ g_total↓ |
| ENDOROIS · OGIEK · SAN · LOLIONDO | 9 | suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ l_densidad↑ |
| EUSKAL HERRIA · ZUBEROA · LA MÁSCARA Y EL CENTAURO | 9 | suj_abstracto_art↑ suj_omitido↓ m_sust↑ m_pron↓ e_anafora↑ r_cv↓ f_sil_sd↓ l_densidad↑ g_total↓ |
| FILIPINAS · DEL CHAVACANO AL JAZZ | 9 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ q_esqueleto↑ e_anafora↑ l_densidad↑ |
| FRONTERA FRANCO-BELGA: RÊV-E-UR · SOÑADOR · ESPEJISMO | 9 | suj_abstracto_art↑ suj_pronombre↓ m_sust↑ m_pron↓ s_fin_frase↓ e_anafora↑ f_sil_sd↓ l_densidad↑ g_total↓ |
| II · UR: HORIZONTE JURÍDICO | 9 | suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_fin_frase↓ r_cv↓ l_densidad↑ g_total↓ |
| IV · UR: ANOMALÍA CIBERNÉTICA · II. LA TÉCNICA QUE RECUERDA SU O | 9 | suj_art_sust↑ suj_abstracto_art↑ suj_omitido↓ m_sust↑ m_pron↓ q_esqueleto↑ e_anafora↑ l_densidad↑ g_total↓ |
| OGURA: PEQUEÑA GOTA DE AGUA | 9 | suj_abstracto_art↑ suj_omitido↓ m_sust↑ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ f_sil_sd↓ l_densidad↑ |
| TU NUBE SECA MI RÍO | 9 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ q_esqueleto↑ e_anafora↑ l_densidad↑ |
| VANIA LIMA Y LOS UR DE BRASIL | 9 | suj_art_sust↑ suj_abstracto_art↑ suj_omitido↓ m_sust↑ m_pron↓ q_esqueleto↑ e_anafora↑ l_densidad↑ g_total↓ |
| BABEL: CANCIONES DE REDENCIÓN | 10 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ l_densidad↑ |
| CICLO HÍDRICO · GEROGLÍFICO UR | 10 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ q_esqueleto↑ q_apertura2↑ e_anafora↑ l_densidad↑ g_total↓ |
| EL UR CÓSMICO · DEL HIELO INTERESTELAR A LA GARGANTA | 10 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ l_densidad↑ |
| EPÍLOGO: PRECEDENTES Y BIBLIOGRAFÍA | 10 | suj_pronombre↓ suj_omitido↓ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ e_anafora↑ e_parent↑ l_densidad↑ g_total↓ |
| EUSKAL HERRIA · EL KOXKERO ERRANTE DE BAJA ALCURNIA | 10 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ s_fin_frase↓ q_esqueleto↑ e_anafora↑ f_sil_sd↓ l_densidad↑ |
| FRONTERA FRANCO-BELGA: DUNKERQUE · URBELTZ CELTA | 10 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ q_esqueleto↑ l_densidad↑ g_total↓ |
| I · UR: INTUICIÓN SIMBÓLICA | 10 | suj_art_sust↑ suj_abstracto_art↑ m_sust↑ m_pron↓ s_fin_frase↓ q_esqueleto↑ q_apertura2↑ r_cv↓ l_densidad↑ g_total↓ |
| III · UR: DEL LOGOS AL MITO · I. LA USURPACIÓN DEL ENGUR | 10 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ q_esqueleto↑ q_apertura2↑ e_anafora↑ l_densidad↑ g_total↓ |
| INDO-GANGES · HIMALAYA · EL GRAN RECEPTÁCULO SÓNICO | 10 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ q_esqueleto↑ r_cv↓ l_densidad↑ |
| LA MUERTE DE LA INTUICIÓN TENÍA UN PRECIO | 10 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ q_esqueleto↑ q_apertura2↑ e_anafora↑ l_densidad↑ |
| MESETA CENTRAL · DEL RIOJA AL ATLÁNTICO · UR VIAJERO | 10 | suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_sub_frase↓ e_parent↑ r_cv↓ f_sil_sd↓ l_densidad↑ g_total↓ |
| MESOPOTAMIA · LEVANTE · LA PRESA ORAL Y EL DIAPIRO PRIMORDIAL | 10 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ q_esqueleto↑ r_cv↓ l_densidad↑ |
| URABÁ · TAPÓN DE DARIÉN · RAÍCES INDÍGENAS | 10 | suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ e_anafora↑ f_sil_sd↓ l_densidad↑ |
| VENDÉE · FRANCIA ATLÁNTICA · EL ESCARPE Y LA FOSA | 10 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ e_anafora↑ r_cv↓ l_densidad↑ g_total↓ |
| HISTORIA DE LA EDUCACIÓN VICTORIANA | 11 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ l_densidad↑ g_total↓ |
| TUR: LA RAÍZ PREINDOEUROPEA · LA MATRIZ PANIBÉRICA | 11 | suj_art_sust↑ suj_abstracto_art↑ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ q_esqueleto↑ e_anafora↑ e_parent↑ l_densidad↑ g_total↓ |
| UR DELTA: TEOLOGÍA DE LA INTUICIÓN, HUÉRFANA DE DOCTRINA | 11 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ l_densidad↑ |
| WAI-MURI: EL AGUA DEL FUTURO | 11 | suj_art_sust↑ suj_pronombre↓ suj_omitido↓ m_sust↑ q_esqueleto↑ q_apertura2↑ e_anafora↑ r_cv↓ f_sil_sd↓ l_densidad↑ g_total↓ |
| ANTROPOLOGÍA RACIAL | 12 | suj_art_sust↑ suj_abstracto_art↑ suj_omitido↓ m_sust↑ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ f_sil_sd↓ l_densidad↑ g_total↓ |
| BONUS TRACK · DISTOPÍA VEGETAL | 12 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ l_densidad↑ g_total↓ |
| IA: FANTASÍA EN ÓRBITA LEO (HOMENAJE A TOM DISSEVELT) | 12 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ q_apertura2↑ e_anafora↑ l_densidad↑ |
| ISLANDIA II · LA GUERRA QUE SE CANTA | 12 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_sub_frase↓ q_esqueleto↑ e_anafora↑ f_sil_sd↓ l_densidad↑ g_total↓ |
| TURKANA · OURO SOGUI · WURO | 12 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_sub_frase↓ q_esqueleto↑ q_apertura2↑ e_anafora↑ f_sil_sd↓ l_densidad↑ |
| UR, EL CASTELLANO Y LA FRONTERA INVISIBLE | 12 | suj_art_sust↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ r_cv↓ f_sil_sd↓ l_densidad↑ g_total↓ |
| ÜRMÜZ: AHURA MAZDĀ · SABIDURÍA UR | 12 | suj_art_sust↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ f_sil_sd↓ l_densidad↑ g_total↓ |
| ANGOSTURA | 13 | suj_art_sust↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ r_cv↓ l_densidad↑ g_total↓ |
| CURACA · EL DIOS QUE HABLA | 13 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ q_esqueleto↑ e_anafora↑ r_cv↓ l_densidad↑ g_total↓ |
| DANUBIO ESTE · TURBINA NUCLEAR | 13 | suj_art_sust↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ f_sil_sd↓ l_densidad↑ g_total↓ |
| DIGITALISMO Y EL TEST GORILA | 13 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ q_apertura2↑ e_anafora↑ f_sil_sd↓ l_densidad↑ |
| III · UR: DEL LOGOS AL MITO · II. GOLGI, CAJAL Y LA CONSTELACIÓN | 13 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ f_sil_sd↓ l_densidad↑ g_total↓ |
| III · UR: DEL LOGOS AL MITO · III. EL RETORNO | 13 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ m_sust↑ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ q_apertura2↑ e_anafora↑ f_sil_sd↓ l_densidad↑ g_total↓ |
| ISLANDIA I · LA ISLA QUE RESPIRA | 13 | suj_art_sust↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ q_apertura2↑ e_anafora↑ f_sil_sd↓ l_densidad↑ g_total↓ |
| LOS VIAJES DE UR POR IBEROAMÉRICA | 13 | suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ r_cv↓ f_sil_sd↓ l_densidad↑ g_total↓ |
| TIMMUR: HIMALAYA VERTICAL | 13 | suj_art_sust↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ q_apertura2↑ e_anafora↑ l_densidad↑ g_total↓ |
| UR ANTES DE URBE: ENCUENTRO EN LAS TRES FASES | 13 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ l_densidad↑ g_total↓ |
| UR, EL EUSKERA Y LA FRONTERA INVISIBLE | 13 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_fin_frase↓ q_esqueleto↑ q_apertura2↑ e_anafora↑ f_sil_sd↓ l_densidad↑ g_total↓ |
| VILCABAMBA · EL RÍO QUE SE ESCONDE | 13 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ l_densidad↑ g_total↓ |
| ISLANDIA III · LA TIERRA DEBAJO DEL FUEGO | 14 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ f_sil_sd↓ l_densidad↑ g_total↓ |
| PLA-UR · EL VIENTRE DE LA TURBA | 14 | suj_art_sust↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ r_cv↓ f_sil_sd↓ l_densidad↑ g_total↓ |
| SIOUXSIE AND THE BANSHEES Y LA GUERRA DE LOS MUNDOS | 14 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ r_cv↓ f_sil_sd↓ l_densidad↑ g_total↓ |
| TUR · UN CONTINENTE EN TRÁNSITO | 14 | suj_art_sust↑ suj_abstracto_art↑ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ r_cv↓ f_sil_sd↓ l_densidad↑ g_total↓ |
| TUR: LA DAMA DE MARFIL | 14 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ e_anafora↑ f_sil_sd↓ l_densidad↑ g_total↓ |
| QUELCCAYA · LA GUERRA DEL AGUA | 15 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ q_apertura2↑ e_anafora↑ f_sil_sd↓ l_densidad↑ g_total↓ |
| TE UREWERA: EL BOSQUE QUE COMPARECE | 15 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ q_apertura2↑ e_anafora↑ r_cv↓ f_sil_sd↓ l_densidad↑ g_total↓ |
| WHANGANUI: EL RÍO QUE NOS NOMBRA | 15 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ q_apertura2↑ e_anafora↑ r_cv↓ f_sil_sd↓ l_densidad↑ |
| IV · UR: ANOMALÍA CIBERNÉTICA · I. EL DIQUE DEL SILENCIO | 16 | suj_art_sust↑ suj_abstracto_art↑ suj_pronombre↓ suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ s_sub_frase↓ s_fin_frase↓ q_esqueleto↑ q_apertura2↑ e_anafora↑ e_parent↑ r_cv↓ l_densidad↑ g_total↓ |

---

## Anexo C · Reproducción y límites

```
pip install spacy numpy
pip install https://github.com/explosion/spacy-models/releases/download/es_core_news_md-3.7.0/es_core_news_md-3.7.0-py3-none-any.whl
python3 herramientas/analisis-texto.py --html urtz.html --matriz --delta --cache /ruta/datos.pkl \
  --obra baroja_aurora=/ruta/aurora.pdf --hyph baroja_aurora ... --obra martin_santos=/ruta/tiempo.pdf --aparte martin_santos
python3 herramientas/analisis-texto.py --html urtz.html --dospuntos --obra ... (mismas obras)
```

Los PDF están en `origin/main`; no se versionan en esta rama. Con `--cache` las repeticiones tardan segundos; sin él, dos minutos.

**Cálculos de una sola vez**, hechos con el mismo código en el entorno de trabajo y descritos en el texto: los pasajes expositivos de Orwell (líneas 5466–5850 y 8005–8705 del texto extraído de *1984*; cuatro trozos de *Homenaje* elegidos por densidad de vocabulario político), las esdrújulas finales y los moldes más repetidos, la clasificación de gerundios por clase y la comparación de cuatro cortes del historial (commits `159bbcc`, `0930bfe`, `4ceedc2` y el estado actual).

**Límites.** El analizador es estadístico (modelo `es_core_news_md` de spaCy 3.7, español general) y comete errores en prosa literaria, neologismos y nombres propios de UR. Orwell está en traducción. El canon son siete obras de tres autores. Una ventana de 1.000 palabras es una muestra pequeña; la mediana de cien ventanas no lo es. La clasificación de los dos puntos y de los gerundios es aproximada. La perplejidad no se calcula. Ninguna cifra mide calidad.
