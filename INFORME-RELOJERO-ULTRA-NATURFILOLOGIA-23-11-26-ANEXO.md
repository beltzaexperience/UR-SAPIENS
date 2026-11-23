# Anexo · los 18 análisis medidos con el canon (23/11/2026)

Salida íntegra de `herramientas/ultra-18-analisis.py` con el caché del canon rehecho (Baroja, Orwell y Martín Santos, solo narración, ventanas de 1.000 palabras) y spaCy 3.8.18 con `es_core_news_md` 3.8.0. Columnas: valor de la pieza; corredor del canon (p10 · p50 · p90); corredor de las piezas de URS; ↑ sobre p90, ↓ bajo p10. Cautela: el analizador es estadístico y se equivoca en prosa literaria y en los neologismos de UR; una pieza de unas 2.000 palabras son dos ventanas.

## Pieza 1

<!-- NATURFILOLOGÍA · EL ESTUDIO DE LA LENGUA DE LA VIDA · ventanas 2 · palabras 2326 -->
| análisis | indicador | pieza | corredor p10 · p50 · p90 | UR p10 · p50 · p90 | fuera (↑ sobre p90, ↓ bajo p10) |
|---|---|---|---|---|---|
| 1 | sílabas por frase (media) | 42.0 | 30.5 · 40.4 · 53.2 | 28.3 · 36.7 · 50.9 | — |
| 1 | sílabas por frase (desviación) | 24.7 | 17.8 · 23.0 · 32.2 | 14.3 · 18.6 · 25.6 | — |
| 1 | % de frases que acaban en palabra aguda | 19.7 | 10.9 · 16.9 · 23.9 | 11.1 · 18.6 · 28.4 | — |
| 1 | % de frases que acaban en esdrújula | 3.2 | 0.0 · 4.2 · 9.1 | 2.4 · 7.3 · 14.3 | — |
| 1 | % de frases que riman en asonante con la anterior | 15.2 | 2.4 · 6.6 · 12.1 | 1.5 · 6.2 · 11.8 | ↑ |
| 1 | aliteración (pares por 100 palabras) | 7.8 | 4.1 · 5.1 · 6.2 | 4.4 · 5.5 · 7.1 | ↑ |
| 2 | sustantivos por 100 palabras | 24.9 | 19.0 · 20.8 · 22.9 | 22.8 · 26.3 · 29.3 | ↑ |
| 2 | verbos por 100 palabras | 12.3 | 13.5 · 16.3 · 19.0 | 10.9 · 13.8 · 18.1 | ↓ |
| 2 | adjetivos por 100 | 9.5 | 5.3 · 7.2 · 9.4 | 5.4 · 8.1 · 11.2 | ↑ |
| 2 | adverbios por 100 | 2.4 | 3.3 · 4.9 · 6.3 | 1.5 · 2.6 · 4.6 | ↓ |
| 2 | preposiciones por 100 | 15.3 | 14.4 · 16.2 · 17.9 | 11.6 · 13.6 · 16.8 | — |
| 2 | determinantes por 100 | 16.0 | 13.7 · 15.5 · 17.1 | 15.8 · 18.6 · 21.2 | — |
| 2 | pronombres por 100 | 5.9 | 5.3 · 7.0 · 8.5 | 2.4 · 3.8 · 6.0 | — |
| 2 | conjunciones coordinantes por 100 | 5.2 | 3.4 · 4.2 · 5.3 | 2.7 · 3.8 · 5.0 | — |
| 2 | conjunciones subordinantes por 100 | 2.0 | 1.6 · 2.6 · 3.6 | 0.9 · 1.5 · 2.9 | — |
| 2 | nombres propios por 100 | 5.6 | 1.8 · 4.2 · 7.2 | 2.1 · 5.5 · 9.5 | — |
| 2 | adjetivos por sustantivo | 0.4 | 0.3 · 0.4 · 0.4 | 0.2 · 0.3 · 0.4 | — |
| 2 | % de verbos finitos en presente | 89.4 | 1.8 · 7.6 · 40.2 | 56.2 · 86.6 · 97.2 | ↑ |
| 2 | % en pasado (pretérito + imperfecto) | 7.8 | 55.0 · 88.7 · 96.1 | 1.9 · 11.3 · 42.9 | ↓ |
| 2 | % en futuro | 0.0 | 0.0 · 0.0 · 1.8 | 0.0 · 0.0 · 1.7 | — |
| 2 | % en condicional | 2.3 | 0.0 · 2.4 · 5.7 | 0.0 · 0.0 · 2.0 | — |
| 2 | % en subjuntivo | 4.6 | 1.7 · 5.3 · 11.1 | 0.0 · 2.8 · 6.2 | — |
| 2 | % en primera persona | 0.9 | 0.0 · 1.3 · 13.0 | 0.0 · 0.0 · 2.2 | — |
| 2 | % en tercera persona | 98.2 | 86.8 · 98.4 · 100.0 | 96.0 · 99.2 · 100.0 | — |
| 2 | infinitivos por 100 | 1.9 | 1.9 · 3.0 · 4.1 | 1.1 · 2.3 · 4.5 | — |
| 2 | participios por 100 | 0.3 | 0.3 · 1.0 · 1.9 | 0.0 · 0.3 · 0.8 | — |
| 3 | profundidad máxima del árbol (media por frase) | 4.5 | 3.8 · 4.5 · 5.0 | 3.7 · 4.3 · 5.0 | — |
| 3 | distancia media de dependencia | 3.0 | 2.4 · 2.6 · 2.9 | 2.0 · 2.2 · 2.7 | ↑ |
| 3 | verbos finitos por frase | 2.2 | 1.9 · 2.2 · 2.7 | 1.5 · 1.9 · 2.3 | — |
| 3 | subordinadas por frase | 1.1 | 1.0 · 1.4 · 1.9 | 0.6 · 1.1 · 1.6 | — |
| 3 | % de frases sin verbo finito | 2.9 | 0.0 · 0.6 · 3.6 | 0.0 · 1.6 · 4.6 | — |
| 3 | pasivas por 1.000 palabras | 5.5 | 1.9 · 4.9 · 9.1 | 0.0 · 2.8 · 6.0 | — |
| 3 | sujeto principal: % nombre propio | 24.0 | 2.2 · 13.9 · 31.7 | 8.1 · 20.0 · 33.3 | — |
| 3 | sujeto principal: % pronombre | 4.0 | 0.0 · 5.1 · 10.2 | 0.0 · 0.0 · 4.2 | — |
| 3 | sujeto principal: % artículo + sustantivo | 38.6 | 13.7 · 23.2 · 35.1 | 29.3 · 44.6 · 59.6 | ↑ |
| 3 | sujeto principal: % artículo + abstracto | 2.8 | 0.0 · 1.7 · 6.2 | 2.5 · 7.2 · 17.2 | — |
| 3 | sujeto principal: % sustantivo sin artículo | 8.9 | 3.0 · 8.7 · 14.8 | 3.3 · 8.3 · 15.7 | — |
| 3 | sujeto principal: % omitido | 12.0 | 17.5 · 28.0 · 39.6 | 2.9 · 8.8 · 19.4 | ↓ |
| 3 | gerundios por 10.000 | 13.7 | 24.4 · 59.6 · 113.4 | 0.0 · 19.0 · 49.0 | ↓ |
| 3 | gerundio tras coma y tras su verbo (candidato Norma 10) por 10.000 | 4.7 | 0.0 · 9.2 · 30.0 | 0.0 · 0.0 · 18.4 | — |
| 3 | gerundio posterior sin coma por 10.000 | 0.0 | 0.0 · 18.0 · 39.7 | 0.0 · 0.0 · 22.6 | — |
| 3 | gerundio antepuesto por 10.000 | 0.0 | 0.0 · 0.0 · 14.5 | 0.0 · 0.0 · 0.0 | — |
| 3 | gerundio en perífrasis (estar, ir, seguir…) por 10.000 | 0.0 | 0.0 · 0.0 · 19.5 | 0.0 · 0.0 · 14.8 | — |
| 3 | otros gerundios por 10.000 | 9.1 | 0.0 · 19.6 · 46.2 | 0.0 · 0.0 · 12.9 | — |
| 4 | densidad léxica (% de palabras de contenido) | 51.8 | 47.9 · 49.7 · 51.5 | 51.6 · 55.3 · 58.5 | ↑ |
| 4 | diversidad léxica (MATTR 500) | 0.5 | 0.5 · 0.5 · 0.6 | 0.5 · 0.5 · 0.6 | ↓ |
| 4 | % de palabras distintas que aparecen una vez | 68.3 | 72.2 · 76.1 · 78.6 | 70.6 · 74.7 · 80.8 | ↓ |
| 4 | % de palabras de contenido que repiten otra de las 50 anteriores | 26.5 | 10.8 · 14.5 · 19.4 | 8.4 · 13.3 · 20.4 | ↑ |
| 4 | % de las palabras de contenido que son las 10 más usadas | 16.8 | 10.7 · 13.5 · 16.8 | 9.1 · 12.4 · 16.8 | — |
| 4 | abstractos (-ción, -dad…) por 100 | 2.8 | 1.0 · 1.7 · 2.9 | 2.1 · 4.0 · 7.1 | — |
| 5 | solape léxico con la frase anterior (%) | 6.1 | 0.9 · 1.9 · 3.4 | 0.6 · 1.4 · 3.6 | ↑ |
| 5 | % de frases sin ninguna palabra en común con la anterior | 46.3 | 59.4 · 76.3 · 88.7 | 60.0 · 80.0 · 91.7 | ↓ |
| 5 | % de frases con el mismo sujeto que la anterior | 3.9 | 0.0 · 3.8 · 14.7 | 0.0 · 0.0 · 4.5 | — |
| 5 | demostrativos por 1.000 | 3.2 | 3.4 · 6.2 · 10.6 | 2.3 · 5.7 · 12.3 | ↓ |
| 5 | conectores aditivos por 1.000 | 2.2 | 0.0 · 1.8 · 4.9 | 0.0 · 1.1 · 4.6 | — |
| 5 | conectores consecutivos por 1.000 | 2.7 | 0.0 · 1.0 · 2.9 | 0.0 · 0.9 · 2.6 | — |
| 5 | marcadores temporales por 1.000 | 3.7 | 4.8 · 9.1 · 14.6 | 3.6 · 8.4 · 14.4 | ↓ |
| 8 | preguntas retóricas (¿) por 10.000 | 76.2 | 0.0 · 0.0 · 24.2 | 0.0 · 0.0 · 19.8 | ↑ |
| 8 | exclamaciones (¡) por 10.000 | 0.0 | 0.0 · 0.0 · 29.9 | 0.0 · 0.0 · 0.0 | — |
| 8 | paréntesis por 10.000 | 134.6 | 0.0 · 0.0 · 21.9 | 0.0 · 0.0 · 34.6 | ↑ |
| 8 | rayas por 10.000 | 18.1 | 0.0 · 0.0 · 44.3 | 0.0 · 0.0 · 58.9 | — |
| 8 | % de frases que abren con la misma palabra que la anterior | 9.2 | 0.0 · 2.7 · 7.3 | 2.9 · 10.4 · 19.5 | ↑ |
| 9 | Fernández Huerta | 84.4 | 75.7 · 80.7 · 86.4 | 63.3 · 75.4 · 83.0 | — |
| 9 | Szigriszt-Pazos (INFLESZ) | 63.2 | 51.6 · 61.1 · 70.1 | 48.6 · 57.3 · 67.0 | — |
| 9 | sílabas por palabra | 2.0 | 1.9 · 2.0 · 2.1 | 2.0 · 2.1 · 2.3 | — |
| 9 | % de palabras de 4+ sílabas | 11.8 | 9.1 · 11.9 · 15.5 | 9.8 · 13.7 · 18.5 | — |
| 10 | imperativos por 10.000 | 4.4 | 0.0 · 0.0 · 8.3 | 0.0 · 0.0 · 10.1 | — |
| 10 | % de verbos en segunda persona | 0.9 | 0.0 · 0.0 · 0.9 | 0.0 · 0.0 · 1.4 | ↑ |
| 16 | entidades por 100 palabras | 5.1 | 4.0 · 5.5 · 7.4 | 4.1 · 6.5 · 8.6 | — |
| 16 | personas por 100 | 1.4 | 0.4 · 1.9 · 3.9 | 0.2 · 1.0 · 2.4 | — |
| 16 | lugares por 100 | 1.5 | 0.3 · 0.8 · 2.0 | 0.4 · 2.0 · 4.0 | — |
| 16 | organizaciones por 100 | 0.1 | 0.0 · 0.3 · 1.0 | 0.0 · 0.2 · 0.5 | — |
| 16 | otras entidades por 100 | 2.1 | 1.2 · 2.1 · 3.0 | 1.9 · 2.7 · 4.3 | — |
| 16 | % de frases con entidad o cifra | 63.6 | 62.6 · 72.1 · 83.3 | 58.5 · 78.9 · 86.2 | — |
| 16 | cifras por 100 palabras | 0.1 | 0.0 · 0.0 · 0.5 | 0.0 · 0.3 · 1.1 | — |
| 17 | ráfaga: coeficiente de variación de la longitud de frase | 0.6 | 0.5 · 0.6 · 0.7 | 0.4 · 0.5 · 0.6 | — |
| 17 | ráfaga: salto medio entre frases consecutivas / longitud media | 0.6 | 0.5 · 0.6 · 0.7 | 0.5 · 0.6 · 0.7 | — |
| 17 | % de secuencias de 4 palabras que se repiten | 1.9 | 0.0 · 0.7 · 1.9 | 0.0 · 0.4 · 2.1 | — |
| 17 | % de frases con esqueleto gramatical repetido (≥4 veces) | 4.7 | 0.0 · 0.0 · 7.4 | 0.0 · 16.7 · 41.3 | — |
| 17 | % de frases cuyas dos primeras palabras se repiten (≥3 veces) | 3.1 | 0.0 · 0.0 · 8.2 | 0.0 · 4.5 · 15.3 | — |

Alarmas del marco fuera del corredor (8 de 17): suj_art_sust↑ suj_omitido↓ m_sust↑ m_verbo↓ e_anafora↑ e_parent↑ l_densidad↑ g_total↓

Delta de Burrows de la pieza: al perfil medio de UR 0.53; obras más cercanas: martin_santos 0.74, baroja_zalacai 0.78, baroja_aurora 0.79
Distancias de las piezas de URS al perfil medio: mediana 0.51, p90 0.67, máxima 0.92 (aviso en 0,7)


## Pieza 2

<!-- NATURFILOLOGÍA · EL SENTIDO Y EL SÍMBOLO · ventanas 2 · palabras 1863 -->
| análisis | indicador | pieza | corredor p10 · p50 · p90 | UR p10 · p50 · p90 | fuera (↑ sobre p90, ↓ bajo p10) |
|---|---|---|---|---|---|
| 1 | sílabas por frase (media) | 47.5 | 30.5 · 40.4 · 53.2 | 28.3 · 36.7 · 50.9 | — |
| 1 | sílabas por frase (desviación) | 23.0 | 17.8 · 23.0 · 32.2 | 14.3 · 18.6 · 25.6 | — |
| 1 | % de frases que acaban en palabra aguda | 14.0 | 10.9 · 16.9 · 23.9 | 11.1 · 18.6 · 28.4 | — |
| 1 | % de frases que acaban en esdrújula | 4.2 | 0.0 · 4.2 · 9.1 | 2.4 · 7.3 · 14.3 | — |
| 1 | % de frases que riman en asonante con la anterior | 3.2 | 2.4 · 6.6 · 12.1 | 1.5 · 6.2 · 11.8 | — |
| 1 | aliteración (pares por 100 palabras) | 6.1 | 4.1 · 5.1 · 6.2 | 4.4 · 5.5 · 7.1 | — |
| 2 | sustantivos por 100 palabras | 24.7 | 19.0 · 20.8 · 22.9 | 22.8 · 26.3 · 29.3 | ↑ |
| 2 | verbos por 100 palabras | 12.4 | 13.5 · 16.3 · 19.0 | 10.9 · 13.8 · 18.1 | ↓ |
| 2 | adjetivos por 100 | 7.6 | 5.3 · 7.2 · 9.4 | 5.4 · 8.1 · 11.2 | — |
| 2 | adverbios por 100 | 3.0 | 3.3 · 4.9 · 6.3 | 1.5 · 2.6 · 4.6 | ↓ |
| 2 | preposiciones por 100 | 14.3 | 14.4 · 16.2 · 17.9 | 11.6 · 13.6 · 16.8 | ↓ |
| 2 | determinantes por 100 | 17.8 | 13.7 · 15.5 · 17.1 | 15.8 · 18.6 · 21.2 | ↑ |
| 2 | pronombres por 100 | 5.1 | 5.3 · 7.0 · 8.5 | 2.4 · 3.8 · 6.0 | ↓ |
| 2 | conjunciones coordinantes por 100 | 4.8 | 3.4 · 4.2 · 5.3 | 2.7 · 3.8 · 5.0 | — |
| 2 | conjunciones subordinantes por 100 | 2.5 | 1.6 · 2.6 · 3.6 | 0.9 · 1.5 · 2.9 | — |
| 2 | nombres propios por 100 | 6.9 | 1.8 · 4.2 · 7.2 | 2.1 · 5.5 · 9.5 | — |
| 2 | adjetivos por sustantivo | 0.3 | 0.3 · 0.4 · 0.4 | 0.2 · 0.3 · 0.4 | — |
| 2 | % de verbos finitos en presente | 89.5 | 1.8 · 7.6 · 40.2 | 56.2 · 86.6 · 97.2 | ↑ |
| 2 | % en pasado (pretérito + imperfecto) | 7.3 | 55.0 · 88.7 · 96.1 | 1.9 · 11.3 · 42.9 | ↓ |
| 2 | % en futuro | 0.5 | 0.0 · 0.0 · 1.8 | 0.0 · 0.0 · 1.7 | — |
| 2 | % en condicional | 1.7 | 0.0 · 2.4 · 5.7 | 0.0 · 0.0 · 2.0 | — |
| 2 | % en subjuntivo | 1.9 | 1.7 · 5.3 · 11.1 | 0.0 · 2.8 · 6.2 | — |
| 2 | % en primera persona | 2.1 | 0.0 · 1.3 · 13.0 | 0.0 · 0.0 · 2.2 | — |
| 2 | % en tercera persona | 96.5 | 86.8 · 98.4 · 100.0 | 96.0 · 99.2 · 100.0 | — |
| 2 | infinitivos por 100 | 2.1 | 1.9 · 3.0 · 4.1 | 1.1 · 2.3 · 4.5 | — |
| 2 | participios por 100 | 0.0 | 0.3 · 1.0 · 1.9 | 0.0 · 0.3 · 0.8 | ↓ |
| 3 | profundidad máxima del árbol (media por frase) | 4.9 | 3.8 · 4.5 · 5.0 | 3.7 · 4.3 · 5.0 | — |
| 3 | distancia media de dependencia | 3.0 | 2.4 · 2.6 · 2.9 | 2.0 · 2.2 · 2.7 | ↑ |
| 3 | verbos finitos por frase | 2.4 | 1.9 · 2.2 · 2.7 | 1.5 · 1.9 · 2.3 | — |
| 3 | subordinadas por frase | 1.4 | 1.0 · 1.4 · 1.9 | 0.6 · 1.1 · 1.6 | — |
| 3 | % de frases sin verbo finito | 2.4 | 0.0 · 0.6 · 3.6 | 0.0 · 1.6 · 4.6 | — |
| 3 | pasivas por 1.000 palabras | 2.2 | 1.9 · 4.9 · 9.1 | 0.0 · 2.8 · 6.0 | — |
| 3 | sujeto principal: % nombre propio | 23.6 | 2.2 · 13.9 · 31.7 | 8.1 · 20.0 · 33.3 | — |
| 3 | sujeto principal: % pronombre | 3.9 | 0.0 · 5.1 · 10.2 | 0.0 · 0.0 · 4.2 | — |
| 3 | sujeto principal: % artículo + sustantivo | 33.5 | 13.7 · 23.2 · 35.1 | 29.3 · 44.6 · 59.6 | — |
| 3 | sujeto principal: % artículo + abstracto | 2.7 | 0.0 · 1.7 · 6.2 | 2.5 · 7.2 · 17.2 | — |
| 3 | sujeto principal: % sustantivo sin artículo | 9.5 | 3.0 · 8.7 · 14.8 | 3.3 · 8.3 · 15.7 | — |
| 3 | sujeto principal: % omitido | 15.1 | 17.5 · 28.0 · 39.6 | 2.9 · 8.8 · 19.4 | ↓ |
| 3 | gerundios por 10.000 | 9.5 | 24.4 · 59.6 · 113.4 | 0.0 · 19.0 · 49.0 | ↓ |
| 3 | gerundio tras coma y tras su verbo (candidato Norma 10) por 10.000 | 0.0 | 0.0 · 9.2 · 30.0 | 0.0 · 0.0 · 18.4 | — |
| 3 | gerundio posterior sin coma por 10.000 | 4.8 | 0.0 · 18.0 · 39.7 | 0.0 · 0.0 · 22.6 | — |
| 3 | gerundio antepuesto por 10.000 | 0.0 | 0.0 · 0.0 · 14.5 | 0.0 · 0.0 · 0.0 | — |
| 3 | gerundio en perífrasis (estar, ir, seguir…) por 10.000 | 4.8 | 0.0 · 0.0 · 19.5 | 0.0 · 0.0 · 14.8 | — |
| 3 | otros gerundios por 10.000 | 0.0 | 0.0 · 19.6 · 46.2 | 0.0 · 0.0 · 12.9 | — |
| 4 | densidad léxica (% de palabras de contenido) | 51.5 | 47.9 · 49.7 · 51.5 | 51.6 · 55.3 · 58.5 | — |
| 4 | diversidad léxica (MATTR 500) | 0.5 | 0.5 · 0.5 · 0.6 | 0.5 · 0.5 · 0.6 | ↓ |
| 4 | % de palabras distintas que aparecen una vez | 69.4 | 72.2 · 76.1 · 78.6 | 70.6 · 74.7 · 80.8 | ↓ |
| 4 | % de palabras de contenido que repiten otra de las 50 anteriores | 22.5 | 10.8 · 14.5 · 19.4 | 8.4 · 13.3 · 20.4 | ↑ |
| 4 | % de las palabras de contenido que son las 10 más usadas | 18.3 | 10.7 · 13.5 · 16.8 | 9.1 · 12.4 · 16.8 | ↑ |
| 4 | abstractos (-ción, -dad…) por 100 | 3.3 | 1.0 · 1.7 · 2.9 | 2.1 · 4.0 · 7.1 | ↑ |
| 5 | solape léxico con la frase anterior (%) | 4.8 | 0.9 · 1.9 · 3.4 | 0.6 · 1.4 · 3.6 | ↑ |
| 5 | % de frases sin ninguna palabra en común con la anterior | 38.3 | 59.4 · 76.3 · 88.7 | 60.0 · 80.0 · 91.7 | ↓ |
| 5 | % de frases con el mismo sujeto que la anterior | 1.9 | 0.0 · 3.8 · 14.7 | 0.0 · 0.0 · 4.5 | — |
| 5 | demostrativos por 1.000 | 5.2 | 3.4 · 6.2 · 10.6 | 2.3 · 5.7 · 12.3 | — |
| 5 | conectores aditivos por 1.000 | 2.2 | 0.0 · 1.8 · 4.9 | 0.0 · 1.1 · 4.6 | — |
| 5 | conectores consecutivos por 1.000 | 1.1 | 0.0 · 1.0 · 2.9 | 0.0 · 0.9 · 2.6 | — |
| 5 | marcadores temporales por 1.000 | 4.2 | 4.8 · 9.1 · 14.6 | 3.6 · 8.4 · 14.4 | ↓ |
| 8 | preguntas retóricas (¿) por 10.000 | 25.3 | 0.0 · 0.0 · 24.2 | 0.0 · 0.0 · 19.8 | ↑ |
| 8 | exclamaciones (¡) por 10.000 | 0.0 | 0.0 · 0.0 · 29.9 | 0.0 · 0.0 · 0.0 | — |
| 8 | paréntesis por 10.000 | 42.9 | 0.0 · 0.0 · 21.9 | 0.0 · 0.0 · 34.6 | ↑ |
| 8 | rayas por 10.000 | 62.6 | 0.0 · 0.0 · 44.3 | 0.0 · 0.0 · 58.9 | ↑ |
| 8 | % de frases que abren con la misma palabra que la anterior | 7.9 | 0.0 · 2.7 · 7.3 | 2.9 · 10.4 · 19.5 | ↑ |
| 9 | Fernández Huerta | 83.8 | 75.7 · 80.7 · 86.4 | 63.3 · 75.4 · 83.0 | — |
| 9 | Szigriszt-Pazos (INFLESZ) | 59.5 | 51.6 · 61.1 · 70.1 | 48.6 · 57.3 · 67.0 | — |
| 9 | sílabas por palabra | 2.0 | 1.9 · 2.0 · 2.1 | 2.0 · 2.1 · 2.3 | — |
| 9 | % de palabras de 4+ sílabas | 11.9 | 9.1 · 11.9 · 15.5 | 9.8 · 13.7 · 18.5 | — |
| 10 | imperativos por 10.000 | 9.5 | 0.0 · 0.0 · 8.3 | 0.0 · 0.0 · 10.1 | ↑ |
| 10 | % de verbos en segunda persona | 1.4 | 0.0 · 0.0 · 0.9 | 0.0 · 0.0 · 1.4 | ↑ |
| 16 | entidades por 100 palabras | 5.1 | 4.0 · 5.5 · 7.4 | 4.1 · 6.5 · 8.6 | — |
| 16 | personas por 100 | 2.5 | 0.4 · 1.9 · 3.9 | 0.2 · 1.0 · 2.4 | — |
| 16 | lugares por 100 | 0.7 | 0.3 · 0.8 · 2.0 | 0.4 · 2.0 · 4.0 | — |
| 16 | organizaciones por 100 | 0.1 | 0.0 · 0.3 · 1.0 | 0.0 · 0.2 · 0.5 | — |
| 16 | otras entidades por 100 | 1.8 | 1.2 · 2.1 · 3.0 | 1.9 · 2.7 · 4.3 | — |
| 16 | % de frases con entidad o cifra | 66.0 | 62.6 · 72.1 · 83.3 | 58.5 · 78.9 · 86.2 | — |
| 16 | cifras por 100 palabras | 0.4 | 0.0 · 0.0 · 0.5 | 0.0 · 0.3 · 1.1 | — |
| 17 | ráfaga: coeficiente de variación de la longitud de frase | 0.5 | 0.5 · 0.6 · 0.7 | 0.4 · 0.5 · 0.6 | — |
| 17 | ráfaga: salto medio entre frases consecutivas / longitud media | 0.5 | 0.5 · 0.6 · 0.7 | 0.5 · 0.6 · 0.7 | — |
| 17 | % de secuencias de 4 palabras que se repiten | 0.6 | 0.0 · 0.7 · 1.9 | 0.0 · 0.4 · 2.1 | — |
| 17 | % de frases con esqueleto gramatical repetido (≥4 veces) | 0.0 | 0.0 · 0.0 · 7.4 | 0.0 · 16.7 · 41.3 | — |
| 17 | % de frases cuyas dos primeras palabras se repiten (≥3 veces) | 0.0 | 0.0 · 0.0 · 8.2 | 0.0 · 4.5 · 15.3 | — |

Alarmas del marco fuera del corredor (7 de 17): suj_omitido↓ m_sust↑ m_verbo↓ m_pron↓ e_anafora↑ e_parent↑ g_total↓

Delta de Burrows de la pieza: al perfil medio de UR 0.51; obras más cercanas: martin_santos 0.67, baroja_aurora 0.71, orwell_1984 0.73
Distancias de las piezas de URS al perfil medio: mediana 0.51, p90 0.67, máxima 0.92 (aviso en 0,7)

