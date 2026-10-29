# RESULTADOS.md · qué umbrales saltan en textos humanos

Una fila por medida y por control (los textos están descritos en `LEEME.md`, sin su contenido). «Salta» = ALARMA o AVISO de `ultra-medidas.py --texto`. Banco del grupo A: **6 textos (4.029 palabras), n insuficiente** (regla 4 de `LEEME.md`): los umbrales de VI.2 no cambian todavía.

## Resultados por texto (29/10/26)
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

## Cuántos controles disparan cada medida (grupo A, n = 6, insuficiente)
| Norma | Medida | Salta en | Estado |
|---|---|---|---|
| 26 | párrafos cortos (≤ 25 palabras) | 5 de 6 | líneas finales, notas a pie, viñetas y comentarios: **efecto de la estructura** |
| 26 | media de palabras por párrafo | 4 de 6 | AVISO: textos con pocos párrafos o de comentarios |
| 4 | frases con tres o más «y» | 4 de 6 | AVISO |
| 10 | gerundio tras coma | 4 de 6 | AVISO |
| 3 | «aquí» / «aparece» | 3 de 6 | 1 real (T9: «aquí tenemos…») y falsos positivos de locución |
| 1 | no X, sino Y | 3 de 6 | 1 real (T9) y 2 falsos positivos del patrón |
| 32/32 bis | coberturas | 3 de 6 | AVISO |
| 50/56 | años y cifras | 3 de 6 | falsos positivos (nombres, precios, años de discos) |
| 5 | andamios de entrada | 1 de 6 | real (T9) |
| 41.1 | frases con tres o más «que» | 1 de 6 | AVISO (T9) |
| 59 | molde de la anterioridad | 1 de 6 | coincidencia del patrón (T9) |
| adenda 17/10 | «alguien» | 1 de 6 | falso positivo (T9) |
| 36.8 | punto y coma por mil palabras | 1 de 6 | AVISO: viñetas con «;» (T4) |

## Pista (no resultado)
- **Un texto de 2010, con fecha pública, de un autor que no usó IA, salta en 6 alarmas** (3 reales: antítesis «no X, sino Y», «aquí», andamios; 3 de estructura o de patrón). Los tics de las normas 1, 3, 5 y 59 son decisiones de estilo de UR, no marcas de la IA: **estas medidas sirven para corregir el estilo, no para probar autoría** (VI.4).
- Las medidas de **párrafo** (26) y de **«y»** (4) saltan en tres de cuatro textos del grupo A y las de **gerundio** (10) en dos: son las más sensibles al género (blog, lista, texto breve).
- Las medidas de **tics** 1, 3 y 5 saltan en el ensayo de 2024 (T8) y las 3 y «alguien» en una crónica (T6): tienen falsos positivos reales en prosa humana de ensayo y de crónica.
- Cuatro de los falsos positivos son defectos de la propia medida (patrón «no X, sino Y»; un número dentro de un nombre contado como cifra; cifras de precio, horario, años y discos). Convendrá afinarla cuando haya más textos.
- Los textos de menos de unas 300 palabras solo sirven para medidas léxicas.
