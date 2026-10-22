# MATRIZ DEL RELOJERO-PLUS (22/10/26)

Pedida por Luis el 22/10/26, al ver que el recuento de la Norma 47, la Tabla Margarita (37) y las revisiones de las Normas 32, 32 bis, 41, 42 y 42 bis no se habían pasado en CULTURA: *«no lo repasó el relojero, el procedimiento está mal diseñado y permite la negligencia. Arregla el procedimiento del relojero-plus para cumplir todas las normas que se puedan solucionar antes de la redacción final.»*

**Qué es.** La lista completa de normas, cada una con su tipo, su forma de comprobarse y el momento en que se comprueba. El Relojero-Plus ya no deja a criterio de quien revisa qué normas «tocan» cada línea: **toda norma de esta matriz se comprueba en cada revisión, y el informe trae la matriz entera con el estado de cada fila.** Una fila que falta en el informe es un informe inválido. Una norma que no tiene fila no existe todavía para el procedimiento: al escribir una norma nueva se añade su fila en el mismo paso.

**Procedimiento de cada revisión** (el texto vigente está en NORMA-METODO.md, «Relojero-Plus v2»):
1. Pasada 0. Comprobación previa (VIII ter: ¿la pieza activa UR?).
2. Pasada 1. Baroja-Orwell de corrido (Norma 36), con los moldes de las Normas 59 y 60.
3. Pasada 2. **Medidas (tipo M), con el script** `python3 herramientas/relojero-plus-medidas.py "<fragmento del data-s>"`. Sus resultados se copian al informe. Un OK del script no sustituye la lectura de las filas L, S y O.
4. Pasada 3. Línea por línea (tipo L), cuerpo y glosa: todas las filas L, sin seleccionar por intuición.
5. Pasada 4. **Sentido (tipo S):** para cada frase, ¿quién hace qué, para qué y tiene sentido? («las élites tenían que saber quién lo había producido»: las élites ya lo saben).
6. Pasada 5. Automatismos (tipo A): se aplican sin consulta y se muestran en antes y después con lo que cambia en negrita (Regla 42).
7. Informe: la matriz completa, con cada fila en uno de estos estados: **cumple**, **hallazgo** (con cita, número de casos y gravedad), **no aplica** (con el motivo), **diferida** (con la cita exacta de Luis que la difiere), **de Luis** (tipo O: se señala y decide él).

**Tipos.**
- **A** automatismo que Luis concedió sin consulta: se aplica y se muestra.
- **M** medible con el script: valor y umbral de la norma en el informe.
- **L** lectura línea por línea (cuerpo y glosa).
- **S** sentido y lógica de la frase.
- **O** criterio de Luis (oído, gusto, qué imagen vale): Claude señala con cita y propone, no decide.
- **D** diferida por decisión de Luis, con cita; solo estas pueden quedar fuera de la revisión previa.
- **N** depende del tipo de pieza: se dice si aplica o no y por qué.
- **X** de proceso: no se comprueba en el texto de la pieza (se cumple al revisar, informar o publicar).

**Una norma solo se difiere con una frase de Luis que lo diga.** Si no hay cita, no está diferida: se pasa antes de la redacción final.

| Norma | Nombre | Tipo | Cómo se comprueba | Cuándo |
|---|---|---|---|---|
| Fundacional | Aplicación total, sin excepción silenciosa | X | ninguna norma se salta sin que conste en el informe | siempre |
| Cero | UR no mendiga legitimidad | L, S | ninguna frase pide permiso ni explica qué es UR | previa |
| Narrativa/ensayo | Resolución del 28/08/26 | L, O | el registro de la pieza lo decide Luis (pregunta única al empezar) | previa |
| I a XII | Marco del libro: definición, estructura, hipótesis, estilo, doble fondo, núcleo filosófico, comparativa, clasificación, estética, método | L, O | se leen una vez al encuadrar; se cita solo si la pieza choca | previa |
| VIII bis | UR como símbolo declarado una sola vez | L | la pieza no vuelve a declarar qué es UR | previa |
| VIII ter | Activación de UR | L | comprobación previa: ¿activa UR con el peso del resto del libro? | previa |
| VIII quater | Protagonistas: UR frente a URBE y la 'T' | L | la 'T' no se explica antes de la glosa (4) (Luis, 22/10/26) | previa |
| XIV | Topónimos UR como anclas, no como paradas | L | cada topónimo ancla algo | línea |
| XV a XVII | Epistemología de la intuición, sistema radical, etimología radical | L | afirmaciones de UR declaradas, no justificadas | línea |
| XVIII a XX, XXVI | PEOIM, PAO, mesa de mezclas | X | procedimientos de ordenamiento, no de texto | n/a |
| XXI | Método Danubio (techo) | N | solo si la pieza supera el techo | n/a |
| XXII | Menos palabras, más acción, menos sintaxis defensiva | L, A | palabrería: extirpación inmediata (Norma 46) | línea |
| XXIII | Cadenas recurrentes | M, L | enumeraciones de 4 o más elementos del script, leídas | medidas |
| XXV | Prohibida la justificación narrativa | L, S | el texto no explica sus propias decisiones | línea |
| XXVII | Marco de análisis y pase final | D (parcial) | «en el momento final de cada capítulo» (NORMA-METODO, sección XXVII). **Antes de la redacción final se hacen sus partes medibles** (protagonistas, términos propios frente al glosario, persona y tiempo del narrador, voz); el pase completo, no | final |
| 0 | Las normas se saltan si el salto se defiende mejor | X | se anota el salto y su defensa | siempre |
| 1 | El descarte «no X, sino Y» | M, A | script | medidas |
| 2 | Verbos en presente de indicativo | L | junto con la Norma 28 | línea |
| 3 | «Aquí» y «aparece» | M, A | script | medidas |
| 4 | Saturación de la «y» | M | script | medidas |
| 5 | Andamios de entrada | M | script | medidas |
| 6 | El principio activo: el amor por estandarte | O | Luis | línea |
| 7 | Arquitectura sántrica (dos actos, cierre opcional) | L | | línea |
| 8 | La ley del típex | L | | línea |
| 9 | Carpintería del aparato crítico | L | glosa | línea |
| 10 | Gerundio de posterioridad | M, L | script | medidas |
| 11 | Honestidad epistémica | L | | línea |
| 12 | Crítica de la homonimia | L | | línea |
| 13 | Los tres registros | L, O | hecho, especulación o dadá, declarado | línea |
| 14 | Contra la moralina | L | | línea |
| 15 | Marcado UR | M | script (UR sin rojo, `<span>` desequilibrado) | medidas |
| 16 | Cursivas | L | | línea |
| 17 | El bloque a la mesa | N | | n/a |
| 18 | La glosa | A, M | llamadas y entradas en orden; encabezado de la entrada igual a la palabra del cuerpo | medidas |
| 19 | Contra el buen salvaje | L | | línea |
| 20 | La economía por defecto | L | | línea |
| 21 | La ideología de la sencillez | L | | línea |
| 22 | La excepción del jeroglífico | O | Luis | línea |
| 23 | La glosa como termómetro | M | entradas, referencia 10-15 | medidas |
| 24 | Los tres números del capítulo sano | M | script (referencia, no veredicto) | medidas |
| 25 | El respirador como anzuelo | M, L, O | cantidad de subtítulos (M); preguntas 1 a 4 (L); preguntas 5 y 6, respiración y título, son de Luis (O) | medidas |
| 26 | El párrafo como unidad | M, L | párrafos cortos y media, script | medidas |
| 27 | El aburrimiento como alarma (tics) | M, O | palabras repetidas, script; alarma de oído de Luis | medidas |
| 28 | Los tres tiempos del agua | A, L, O | pasado para hechos únicos sin consulta; excepciones (a) a (e) a Luis | automatismo |
| 29 | La ley de la escasez | L | un solo término opaco sin glosar | línea |
| 30 | UR no se justifica, se declara | L | | línea |
| 31 | Párrafos terminales de resumen | A, M | última frase de la pieza y de cada párrafo, leídas | automatismo |
| 32 y 32 bis | El «podría» bajo sospecha y la cobertura repetida | M, L | coberturas del script, cada una con argumento | medidas |
| 33 | La síncopa sintáctica | M, O | frases cortas y desviación típica | medidas |
| 34 | La vía libre del desborde | O | Luis | línea |
| 35 | La mirada del zahorí | L, S | ningún detalle físico inventado | línea |
| 36 | Baroja-Orwell: pasada previa | L | de corrido, antes que nada | pasada 1 |
| 36.7 | Enumeraciones y cadenas simétricas | M, A | script y lectura | medidas |
| 36.8 | Perfil medido | M | desviación, punto y coma, abstracción | medidas |
| 36.8 | Registro de la pieza y respiración | O | Luis | línea |
| 36.9, 59 | Plantilla de la anterioridad | M, A | script | medidas |
| 36.9, 60 | Plantilla «Quien X decide Y» | M, A | script | medidas |
| 37 | La Tabla Margarita | X | **toda crítica externa o de lectores pasa por «¿real o falso positivo? ¿se queda o se corrige?» con su ledger, en el mismo paso en que llega** | siempre |
| 38 | La muleta de apertura y la frase-consigna | M, A | aperturas con artículo y con «En», script | medidas |
| 39 | La frontera del marcapáginas | M | razón entre tramos, script | medidas |
| 40 | El oro y el estaño | L | lo investigado sin comprobar queda en el estaño | línea |
| 41 | Cinco guías del autoanálisis de Luis | M, L | relativas, conectores, preguntas retóricas, tecnicismos, «mientras» | medidas |
| 42 | La densidad de pulido | M | antítesis, aforismos, binomios | medidas |
| 42 bis | Los dos puntos | M | por mil palabras, script | medidas |
| 43 | El subtítulo interno | M | forma `<h4>`, script | medidas |
| 44 | Guiones del Permafrost | N, M | palabras partidas por guion | medidas |
| 45 | Marvin Gaye y The Clash | N, L | piezas de música | línea |
| 46 | Las imágenes poéticas | L, A, O | inventario de imágenes de la pieza **después de compactar y antes de la lectura de lectores**; decide Luis cuáles tienen fuerza descomunal; la palabrería sin dato se corta sin consulta (extirpación inmediata, acotada) | tras compactar |
| 47 | Los protagonistas son el sujeto | M, A | recuento formal por lectura de frases con sujeto abstracto | medidas |
| 48 | Las correcciones no rebajan la densidad | S | guarda de todo cambio | siempre |
| 49 | «Memoria» | M | por 10.000 palabras, control 40 | medidas |
| 50 | Cifras generalizadas en el cuerpo | M, A | años y cifras del cuerpo | medidas |
| 51 | Informes: «texto» o «glosa» en cada cambio | X | toda propuesta lo dice | informe |
| 52 | La glosa no explica el arte | L | glosa | línea |
| 53 | La narración se adecúa a la estantería | A, D | fusión de párrafos y subtítulos: se ejecuta en la compactación (Normas 25, 26, 39 y 43). Puntos 3 a 5 (imágenes de Oteiza y Chillida, frases musicales, densidad): «hasta la revisión final de cada capítulo» (Norma 53) | compactación; final |
| 54 | «Cuerpo» | M | script | medidas |
| 55 | La glosa telegráfica de dos niveles | A, M | | automatismo |
| 56 | Pegada política: cifras, años, términos y nombres | M, A | inventario del cuerpo | tras compactar |
| 57 | El estaño se juzga por el texto | L | prueba en tres pasos | línea |
| 58 | Etimología insurgente | N | piezas EI | n/a |
| 59 | Plantilla de la anterioridad | M, A | | medidas |
| 60 | Plantilla del reparto de poder | M, A | | medidas |
| Regla 14 | Marcador al día | A | | cada cambio |
| Regla 38 | Guardar y publicar | X | solo con el OK de Luis | publicación |
| Regla 39 | Leyenda de marcas | X | `(*-tit) (*-red) (*-nor)` | publicación |
| Regla 42 | Antes y después con la negrita | X | informes | informe |
| Regla 43 | Procedimiento de mejora final | X | | siempre |

**Lo que el script no hace** (v1, 22/10/26). Mide formas. No juzga sentido (S), ni la carga mitopoética (Norma 48), ni las excepciones de las Normas 28, 59 y 60; por eso marca «ALARMA» o «AVISO» cuando se cruza un umbral y la lectura decide si el caso cae en una excepción. Probado en CULTURA el 22/10/26, encontró un fallo real que la lectura no había visto (el «ur» sin marcar de «escritura» en un subtítulo) y tres falsos positivos de forma (dos instancias de las Normas 59 y 60 que caen en excepción, y un «hasta que» que no era de anterioridad).
