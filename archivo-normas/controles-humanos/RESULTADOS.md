# RESULTADOS.md · qué umbrales saltan en textos humanos

Una fila por medida y por control (los textos están descritos en `LEEME.md`, sin su contenido). «Salta» = ALARMA o AVISO de `ultra-medidas.py --texto`. Banco del grupo A: **7 textos (5.575 palabras), n insuficiente** (regla 4 de `LEEME.md`): los umbrales de VI.2 no cambian todavía.

## Resultados por texto (29/10/26, medidos antes del afinado de los contadores)
| Id | Palabras de cuerpo | Alarmas | Avisos | Qué saltó |
|---|---|---|---|---|
| T1 | 562 | 1 | 3 | norma 3 (falso positivo: «aquí» en la locución «de aquí»); 26 párrafos cortos (línea final sin terminar); 10 gerundio tras coma; 4 frases con tres «y» |
| T2 | 689 | 2 | 6 | 26 párrafos cortos (línea de despedida); 1 «no X, sino Y» (**falso positivo del patrón**: casó «no es …, que es …»); 26 media por párrafo (138); 10 gerundio; 32/32 bis coberturas (3); 4 frases con tres «y» (3); 50/56 cifras (**falso positivo**: un número que forma parte de un nombre) |
| T3 | 81 | 0 | 2 | 26 media por párrafo (2 párrafos); 4 frase con tres «y» |
| T4 | 209 | 1 | 2 | 26 párrafos cortos (2 de 7); 26 media por párrafo; 36.8 punto y coma (19,1 por mil: viñetas terminadas en «;»); todo por la estructura de lista |
| T5 | 170 | 0 | 1 | 50/56 cifras (**falso positivo**: precio y horario en un anuncio) |
| T6 | 667 | 2 | 3 | 3 «aquí» (**falso positivo**: «Aquí se acaba…»); adenda 17/10 «alguien» (**falso positivo**: pregunta directa al lector); 26 párrafos cortos (17 %, uno es el título); 10 gerundio; 4 frases con tres «y» |
| T7 | 674 | 0 | 4 | 10 gerundio; 41.1 frase con tres «que»; 4 frase con tres «y»; 50/56 cifras (**falso positivo**: años y nombres de discos en una crónica musical) |
| T9 | 1.648 | 6 | 5 | artículo de 2010, ver abajo |
| T10 | 819 | 3 | 4 | comentarios de 2010 (41 párrafos de una o dos líneas): 26 párrafos cortos (76 %) y media por párrafo (20); 1 «no X, sino Y» (**falso positivo**: «pero este es…»); 3 «hasta aquí» (**falso positivo**: locución); 10 gerundio; 32/32 bis coberturas (3); 50/56 cifras y años |
| T11 | 1.546 | 5 | 5 | artículo de 2010, ver abajo |
| T8 | 3.597 | 3 | 7 | ver abajo |

## T8 (ensayo de Carlos G. De Marcos, 2024; primeras 3.597 palabras; no se copia)
| Norma | Medida | Valor | Estado | Lectura |
|---|---|---|---|---|
| 1 | no X, sino Y | 5 | ALARMA | 2 son la antítesis real; las otras 3, coincidencias del patrón |
| 3 | «aquí» / «aparece» | 4 | ALARMA | el verbo «aparece» en su uso normal y «He aquí» en una cita bíblica: **falsos positivos** |
| 5 | andamios de entrada | 4 | ALARMA | «se trata de», «hay que», «no deberíamos olvidar»: aparecen en prosa ensayística humana |
| 26 | media de palabras por párrafo | 300 | AVISO | párrafos muy largos de ensayo en web |
| 10, 32/32 bis, 41.1, 4, «a veces», 50/56 | gerundio (6), coberturas (11), tres «que» (13), tres «y» (10), «a veces» (2), años y cifras (3 y 7) | | AVISO | prosa ensayística larga con citas y paréntesis |

No saltaron: artículo inicial (16 % frente a 35 %), desviación de frase (31,0 frente a 9,8) ni punto y coma (4,4 por mil).

## T9 (artículo de Carlos G. De Marcos, Beltza, 18/06/2010; 1.648 palabras de cuerpo; no se copia)
**6 ALARMAS y 5 AVISOS en un texto humano publicado en 2010**, anterior a la IA y con fecha pública comprobable:
| Norma | Medida | Valor | Estado | Lectura |
|---|---|---|---|---|
| 26 | párrafos cortos | 10 de 26 (38 %) | ALARMA | **estructural**: las 9 notas a pie y un subtítulo cuentan como párrafos cortos |
| 1 | no X, sino Y | 1 | ALARMA | **real**: «no ha sido todo esto, sino un simple gesto» |
| 3 | «aquí» / «aparece» | 3 | ALARMA | «aquí tenemos», «recordar aquí», «a partir de aquí»: andamios reales de ensayo |
| 5 | andamios de entrada | 4 | ALARMA | «todo hay que decirlo», «hay que dar», «se trata de»: reales |
| 59 | molde de la anterioridad | 2 | ALARMA | «ya estaba sellada» y una construcción con «no ha sido… sino»: coincidencias del patrón, no el molde de UR |
| adenda 17/10 | «alguien» | 1 | ALARMA | **falso positivo**: «alguien como Bob Dylan» es una referencia concreta, no voz anónima |
| 10, 32/32 bis, 41.1, 4, 50/56 | gerundio (2), coberturas (8), tres «que» (7), tres «y» (3), cifras (20: años de discos y notas) | | AVISO | prosa de ensayo y de crítica |

No saltaron: artículo inicial (11 % frente a 35 %), desviación de frase (13,6 frente a 9,8).

## T11 (artículo de Carlos G. De Marcos, Beltza, 07/05/2010; 1.546 palabras de cuerpo; no se copia)
**5 ALARMAS y 5 AVISOS** en un texto humano de 2010: párrafos cortos (5 de 19, 26 %: las notas a pie), «no X, sino Y» (3), «aquí» (2), andamios (1), «alguien» (1: «antes de que alguien me lo pregunte», referencia natural); avisos de gerundio (3), coberturas (6), tres «que» (3), tres «y» (2) y años y cifras (20: **falso positivo**, son las llamadas de nota «(1)» a «(10)» contadas como cifras). No saltaron: artículo inicial (12 % frente a 35 %) ni desviación de frase (11,9 frente a 9,8).

## Afinado de los contadores (29/10/26)
Tras los resultados anteriores se afinaron en `ultra-medidas.py` cuatro contadores que daban alarmas falsas. **No se tocó ningún umbral ni ninguna norma**; solo qué se cuenta.
| Contador | Antes contaba de más | Ahora no cuenta | Efecto en los controles |
|---|---|---|---|
| Norma 1 («no X, sino Y») | cualquier «no es … es» y «no solo … es», aunque el segundo verbo abriera una oración de relativo («no es X, que es Y»); y «no solo … sino también» | oraciones de relativo; la suma «no solo … sino también» | quita 1 falso positivo (T2); en las piezas del libro quita 4 coincidencias que no eran antítesis |
| Norma 3 («aquí» / «aparece») | toda aparición de «aquí» | las locuciones «de / hasta / por / desde aquí», «he aquí», «a partir de aquí» | quita las alarmas por locución (T1, T10 y parte de T8, T9, T11); en el libro quita 15 locuciones |
| Norma 26 (párrafos cortos y media por párrafo) | notas a pie «(1) …», viñetas «.- …» y títulos en mayúsculas | esas líneas | T9 pasa de 10 de 26 párrafos cortos (ALARMA) a 3 de 16 (AVISO); T11 de 5 de 19 (ALARMA) a 0 de 9 (OK) |
| Norma 50/56 (años y cifras) | las llamadas de nota «(1)» y el número que forma parte de un nombre («Felipe 6», «Reactor 1») | esas dos clases | T11 pasa de 20 cifras a 0; T9 de 20 a 2 |

**Qué sigue contando (a propósito):** los años y precios en prosa son aciertos de la Norma 50, no falsos positivos; la norma pide generalizarlos y llevar el exacto a la glosa. Corrijo así lo que dije antes de que fueran falsos positivos los años de discos y los precios: eran aciertos de la norma sobre un texto de crónica.

**Recall comprobado en el libro:** sobre las 221 piezas de `urtz.html`, el contador de la Norma 1 no pierde ninguna antítesis real («no es X: es Y», «no es X —es Y», «no X, sino Y») y **gana 11** que antes se le escapaban por usar «fue» («No fue un fin del mundo: fue un cambio…»).

## Cuántos controles disparan cada medida (grupo A, n = 7, insuficiente; tras el afinado)
| Norma | Medida | Salta en | Estado |
|---|---|---|---|
| 26 | párrafos cortos (≤ 25 palabras) | 5 de 7 | líneas finales y comentarios: efecto de la estructura |
| 10 | gerundio tras coma | 5 de 7 | AVISO |
| 4 | frases con tres o más «y» | 5 de 7 | AVISO |
| 26 | media de palabras por párrafo | 4 de 7 | AVISO: textos con pocos párrafos o de comentarios |
| 32/32 bis | coberturas | 4 de 7 | AVISO |
| 1 | no X, sino Y | 3 de 7 | antítesis reales (T9, T11) y una coincidencia («pero este es…», T10) |
| 3 | «aquí» / «aparece» | 2 de 7 | reales («aquí tenemos…», T9, T11) |
| 5 | andamios de entrada | 2 de 7 | reales |
| 41.1 | frases con tres o más «que» | 2 de 7 | AVISO |
| adenda 17/10 | «alguien» | 2 de 7 | referencias concretas («alguien como…») |
| 36.8 | punto y coma por mil palabras | 1 de 7 | AVISO: viñetas con «;» |
| 59 | molde de la anterioridad | 1 de 7 | coincidencia del patrón |
| 50/56 | años y cifras | 0 de 7 | — |

## Pista (no resultado)
- **Un texto de 2010, con fecha pública, de un autor que no usó IA, salta en 6 alarmas** (3 reales: antítesis «no X, sino Y», «aquí», andamios; 3 de estructura o de patrón). Los tics de las normas 1, 3, 5 y 59 son decisiones de estilo de UR, no marcas de la IA: **estas medidas sirven para corregir el estilo, no para probar autoría** (VI.4).
- Las medidas de **párrafo** (26) y de **«y»** (4) saltan en tres de cuatro textos del grupo A y las de **gerundio** (10) en dos: son las más sensibles al género (blog, lista, texto breve).
- Las medidas de **tics** 1, 3 y 5 saltan en el ensayo de 2024 (T8) y las 3 y «alguien» en una crónica (T6): tienen falsos positivos reales en prosa humana de ensayo y de crónica.
- Cuatro de los falsos positivos son defectos de la propia medida (patrón «no X, sino Y»; un número dentro de un nombre contado como cifra; cifras de precio, horario, años y discos). Convendrá afinarla cuando haya más textos.
- Los textos de menos de unas 300 palabras solo sirven para medidas léxicas.
