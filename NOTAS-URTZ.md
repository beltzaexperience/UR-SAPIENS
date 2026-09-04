# NOTAS-URTZ.MD — INCIDENTES TÉCNICOS Y REGLAS DE SEGURIDAD AL TOCAR CÓDIGO

> No es la primera vez que perdemos tiempo valioso por tocar el HTML sin verificar antes de guardar. Este archivo existe para que deje de serlo.

---

## REGLAS FIJAS, EFECTIVAS DESDE HOY

### 1. Nunca tocar código de memoria

Antes de cualquier edición estructural (mover bloques, insertar piezas, cortar y pegar), leer el estado real del archivo —con `grep`, con Playwright, con lo que haga falta— nunca asumir dónde está algo porque "debería estar ahí" según lo que recuerdo de sesiones anteriores.

### 2. Nunca a ciegas, nunca automático sin pensar

Ninguna operación de corte y pegado se ejecuta sin antes: localizar los límites exactos del bloque, confirmar qué hay inmediatamente antes y después del punto de corte y del punto de inserción, y prever el tamaño resultante antes de escribir nada en disco.

### 3. Red de seguridad obligatoria: verificación de tamaño exacto

Toda operación que mueva contenido de un sitio a otro (no que añada ni quite) debe comprobar, antes de guardar, que el tamaño final del archivo es idéntico al tamaño inicial. Si no cuadra ni un carácter, la operación se detiene y no se guarda nada — como pasó hoy mismo, cuando un salto de línea de más frenó el primer intento antes de tocar el archivo real.

### 4. Frontera URS/URIM: marca inequívoca en el propio HTML

Ya no basta con la posición relativa de un ancla (`go-informes`) para decidir qué es URS y qué es URIM — hoy se demostró frágil: un banner mal colocado partió URS en dos sin que nadie lo notara durante semanas de sesiones. La solución permanente: un comentario HTML explícito en la frontera real:

```html
<!-- ============================================== -->
<!-- FRONTERA REAL URS / URIM — NO MOVER SIN VERIFICAR -->
<!-- Todo lo ANTERIOR a este comentario es URS.        -->
<!-- Todo lo POSTERIOR a este comentario es URIM.      -->
<!-- ============================================== -->
```

Colocado inmediatamente antes de `<a id="go-informes">`. Cualquier duda futura sobre si algo es URS o URIM se resuelve mirando en qué lado de este comentario está — no interpretando estilos, ni bullets, ni suposiciones.

### 5. Preguntar siempre que haya la más mínima duda

Antes de colocar cualquier pieza nueva, si no está clara su pertenencia a URS o a URIM, preguntar a Luis explícitamente en vez de decidir por intuición o por dónde "parece que toca". No volver a asumir.

---

## INCIDENTE DE HOY — REGISTRO COMPLETO

### Qué se pidió originalmente

Contar cuántos apartados (subsecciones geográficas) de URS estaban vacíos, para que Luis pudiera ver de un vistazo qué huecos reales quedan por rellenar desde URIM.

### Qué se encontró en el camino, no lo que se buscaba

El conteo automático daba resultados contradictorios en varios intentos sucesivos. La causa, tras varias rondas de investigación:

1. **Símbolos de cabecera inconsistentes.** Las subsecciones geográficas se construyeron a lo largo de la sesión (y de sesiones anteriores) usando tres símbolos distintos para el mismo nivel jerárquico (`&#9675;`, `&#9679;`, `&#9702;`), sin que hubiera una marca única y fiable.
2. **El banner "Informes Maestros" estaba mal colocado.** Su ancla (`go-informes`) llevaba tiempo insertada en mitad del contenido de URS, no al final. Esto hacía que un tramo grande de contenido legítimo de URS (continuación de varias Caras, y la sección "Al Yazirat Tarif" con la pieza "Isla de Tarifa", que Luis confirmó que SÍ es URIM) quedara mal clasificado en cualquier conteo automático basado en la posición de esa ancla.
3. **Búsquedas de texto plano poco fiables.** Varias comprobaciones a lo largo del proceso encontraron menciones sueltas de un texto (como "Cara 1 · Ibérico" citado dentro de una rayuela en otra pieza) y las confundieron con la cabecera real, generando diagnósticos erróneos que hubo que descartar y rehacer.

### Qué se resolvió

- Las 37 subsecciones geográficas conocidas hasta ese momento (más tarde se sumaría una octava en Cara 1, ver más abajo) y las 6 Caras quedaron marcadas con un atributo `data-nivel="sub"` / `data-nivel="cara"` inequívoco, verificado con HTML válido tras corregir un primer intento fallido (el atributo se insertó al principio dentro del propio `style="..."`, generando HTML inválido — detectado y corregido antes de continuar).
- **Primer intento, erróneo, y corregido después de que Luis lo señalara:** el banner "Informes Maestros" se movió a una posición equivocada —justo antes de "Al Yazirat Tarif"—, partiendo de la idea incorrecta de que ese era el problema real. Luis lo detectó de inmediato ("lo has fastidiado, estaba bien") y se revirtió con la misma red de seguridad de tamaño exacto. **Posición correcta y definitiva, confirmada por Luis:** el banner va inmediatamente después del Marcador Fonomático, no antes de Al Yazirat Tarif. Al Yazirat Tarif —con la pieza Isla de Tarifa— es URIM real, del mismo modo que todo el resto de Informes Maestros: por estar después del banner, no por ninguna operación de recolocación.
- Se verificó con una comprobación de posición DOM limpia (Playwright, sobre todas las anclas principales en un solo barrido) que el orden real del documento es monótono y correcto: Bio → Prólogo → Prefacio → Introducción → Cara 1 → Interludios → Etimología → Contraportada → Marcador Fonomático → Informes Maestros (banner en su posición original, correcta).
- Se añadió el comentario HTML de frontera (Regla 4, arriba) para que este tipo de confusión no vuelva a producirse.

### Qué queda pendiente — actualizado tras el resto de la sesión

El conteo original sí se completó más tarde, en la misma sesión: tabla "Análisis de Construcción" con las 18 categorías reales de URS, las 37 subsecciones geográficas más una octava recién descubierta en Cara 1 (Ibero Intros — ver más abajo), y el mapeo por título de Compost y Semillas. Lo que sigue pendiente de verdad: rellenar las columnas URS/URIM/TOTAL con cifras reales, categoría por categoría, con Luis confirmando cada una — nada de scripts que recorran el documento entero de golpe.

### Lección de fondo

El tiempo perdido hoy no vino de un solo error — vino de una cadena de asunciones no verificadas, acumuladas a lo largo de muchas sesiones, que nadie había puesto a prueba hasta que se intentó construir algo que dependía de que todas fueran ciertas a la vez. Verificar cuesta tiempo en el momento; no verificar cuesta mucho más tiempo después, cuando el error ya está enterrado bajo capas de trabajo posterior.

---

## HISTORIA ORGÁNICA DEL PROYECTO — DE INDEX.HTML A URTZ

> Esto no es norma-método (esa regula qué tipo de libro es UR y con qué método literario se escribe). Esto es el proyecto a nivel orgánico y pragmático: de dónde viene, por qué existe cada pieza del sistema actual, y qué queda por hacer en qué orden.

### El origen: index.html

El proyecto empieza en `index.html` — por el momento, público y proto libro editorial. Es un fanzine hídrico completo, con su propia arquitectura: UR-book (con sidebar propio, `id="sidebar"`), Alpha-UR (diccionario, `id="ur-alfabeto"`), y Escombrera (segundo sidebar, `id="escombrera-aside"`). Tiene su propio muro glaciar de material en bruto — un `permafrost.html` de qanats, pensado para desarrollarse hacia dentro de `index.html`.

### El giro: nace URTZ

Luis se da cuenta de que `index.html` funciona bien como fanzine, pero carece del rigor que va adquiriendo poco a poco. Decide empezar de cero un libro sobre UR con todos los requisitos: rigurosidad de hierro y radio libre multidisciplinar a la vez. De ahí nace URTZ (`urtz.html`) — un reto descomunal, inspirado en la idea de "Vida Total" de Tom Wolfe, como el resto de los trabajos vitales de Luis.

### El primer intento de laboratorio: IGLUR, y su fracaso

Para URTZ, Luis intenta crear un laboratorio de trabajo: IGLUR (`LABORATORIO-IGLUR.html`). El propio Luis lo dice sin rodeos: fracasa en el intento. No como sistema de organización que funcionara bien — aunque el material que contiene sigue siendo válido y verificado, y hoy quedan 14 piezas todavía por vaciar de ahí.

### La solución que sí funciona: URIM, el espejo

Luis ve por fin el laboratorio adecuado: URIM, el espejo estructural de URS. Las mismas Caras, las mismas subsecciones — para que cualquier investigación tenga un hogar geográfico obvio antes de estar lista para URS. Empieza a colocar ahí las investigaciones nuevas, y además arranca la recolocación de todo el trabajo anterior a URTZ, empezando por mover las piezas de IGLUR a su ubicación real dentro de URIM.

### El método de trabajo de Luis, dicho por él mismo

> "No hemos terminado, mi forma de trabajar es así: empiezo, lo dejo por otro asunto, vuelvo, termino o no, ya volveré, tengo en mente lo que queda pendiente."

Esto no es desorden — es el ritmo real del proyecto, y hay que trabajar con él, no contra él. El plan pendiente está siempre en la cabeza de Luis aunque una tarea concreta se quede a medias varias sesiones.

### El plan en dos fases, tal como lo tiene Luis

**Fase 1 — en curso ahora mismo:** terminar de vaciar IGLUR, pieza a pieza, a su ubicación real dentro de URIM. PEOIM es el procedimiento; las 14 piezas restantes son el trabajo pendiente inmediato.

**Fase 2 — después de que la Fase 1 esté completa, no antes:** mover `permafrost.html` (101 qanats) a URIM, con el mismo método de eficacia (PEOIM) y con destino fijado antes de mover nada. **Permafrost todavía no ha empezado a vaciarse** — está en cola, detrás de IGLUR, no en paralelo.

### El resultado final que Luis tiene en mente

Al terminar ambas fases, en el mismo `urtz.html` convivirán: **URS** — el libro trabajado, con sus piezas selladas y las marcas `(*-...)` pendientes de repaso de redacción; **URIM** — el laboratorio ya limpio, con las piezas oportunas bien colocadas; y, por fin, **visibilidad real** de qué categorías de URS siguen con hueco de contenido genuino por trabajar — no solo intuición de que faltan cosas, sino el dato exacto.

### La pestaña — construida parcialmente

El panel "Análisis de Construcción" dentro del Marcador Fonomático ya existe, con la estructura completa: 18 categorías de URS, 38 subsecciones geográficas reales (37 + Ibero Intros, descubierta más tarde en la propia sesión), y dos tablas de mapeo por título para Compost y Semillas. Lo que falta: las cifras reales de URS/URIM/TOTAL, todavía sin rellenar — la estructura ya no es el problema, el dato sí.

---

## REGLA 6 — UN SOLO PATRÓN VISUAL, SIEMPRE EL MISMO

Cabecera, subcabecera, pestaña: `<details class="pieza">` con su `<summary>`. Ese es el patrón de todo el libro, URS y URIM por igual. No se inventan formatos nuevos porque el contenido sea distinto —un marcador de estado, un panel de datos, una tabla— cuando el patrón existente ya resuelve el problema.

**Lo que pasó, dos veces seguidas en la misma tarde:** el primer Marcador Fonomático se construyó como bloque suelto de `<p>` sin `<details>`, distinto a cualquier otra pieza del libro. Corregido a petición de Luis, el segundo intento fue un sistema de pestañas con radio buttons y CSS propio —funcional, probado, pero igual de ajeno al patrón real. Luis lo señaló directamente: *"no sé de dónde sacas el formato al aire... ni el formato de dos marcadores al aire"*. La solución correcta era la más simple: dos piezas `<details>` normales, iguales a cualquier otra del documento.

**La pregunta que hay que hacerse antes de diseñar nada nuevo:** ¿el patrón que ya existe resuelve esto? Si la respuesta es sí —y casi siempre lo es—, no hace falta innovar. Se despliega igual, se busca igual, se cuenta igual que el resto.

---

## REGLA 7 — PIEZA ABSORBIDA POR URS: ELIMINACIÓN INMEDIATA DE URIM

Cuando una pieza de URIM (Semilla, Compost, o cualquier otra) queda absorbida por una pieza real de URS —su contenido ya vive, desarrollado, dentro del libro—, se elimina de URIM de inmediato. No se deja marcada como "absorbida" indefinidamente: esa marca es un paso intermedio, no un estado final. URIM no es archivo histórico de lo que ya se usó — es taller de lo que todavía hace falta trabajar. Guardar ahí una pieza ya absorbida ocupa espacio que confunde el recuento real de lo pendiente.

**Procedimiento:** confirmar que el contenido está genuinamente ya en URS (no solo el título o la idea, el desarrollo real) → eliminar la pieza de URIM con la misma red de seguridad de siempre (tamaño exacto verificado antes de guardar) → no dejar rastro salvo, si acaso, una nota breve aquí mismo si el caso lo merece.

---

## REGLA 8 — CRITERIO PARA DECIDIR DÓNDE VA CADA NORMA: NORMA-MÉTODO O NOTAS-URTZ

Distinción fundamental, señalada por Luis: **NORMA-METODO.md implica a tres actores** —Luis, Claude, Perplexity—; es todo lo que cualquiera de los tres necesita conocer para escribir bien una pieza del libro: método literario, registro, verificación, redacción. **`notas-urtz.md` implica solo a dos** —Luis y Claude—; es todo lo que hace falta para no romper el archivo técnico: seguridad al tocar código, mecánica de URS/URIM, incidentes, reparto de funciones entre archivos.

**La prueba, antes de escribir cualquier norma nueva:** ¿le serviría esto a Perplexity si tuviera que redactar una pieza del libro mañana? Si sí, va en `NORMA-METODO.md`. Si la respuesta depende de tocar el HTML directamente —algo que Perplexity nunca hace—, va en `notas-urtz.md`. La Regla 7 de aquí arriba es el ejemplo que enseñó esta distinción: nació mal colocada en norma-método, y el propio Luis señaló el error antes de que se asentara.

---

## REGLA 9 — MECÁNICA DEL MARCADOR FONOMÁTICO (trasladada desde norma-método, misma corrección de la Regla 8)

Vive en `urtz.html`, entre El Noturikon y los Informes Maestros, con su propio enlace en la topband (MFO). Cada actualización es una entrada nueva, no una sustitución — el historial de mediciones queda visible, sesión tras sesión.

**Regla de actualización:** no se actualiza en fecha fija ni obligatoriamente al final de cada sesión — se actualiza cuando Luis lo pida, o cuando a él se le ocurra que toca revisarlo.

**Cómo se mide, cada vez:**
1. Contraste directo sobre el documento renderizado (Playwright, no grep sobre HTML crudo) — recorrer todas las piezas, separar URS de URIM por posición relativa a la frontera marcada (el comentario HTML, no ya el ancla sola — ver Regla 4), sumar caracteres y palabras reales de cada lado.
2. URSURIM es la suma de los dos.
3. Estimación de páginas: 250 palabras/página (densidad real de *Finnegans Wake*, dato de referencia en `NORMA-METODO.md` XIX), aplicada a URS y URSURIM por igual, siempre etiquetada como estimación.
4. Comparación contra Vico en porcentaje: palabras de URS ÷ punto medio de la horquilla de Vico, expresado como rango.
5. La entrada nueva se añade después de la última existente — nunca sustituye. Formato de fecha: "A DD/MM/AA d.C." con resumen breve de qué se construyó esa sesión.

**Regla fija de formato — las cifras de Vico, siempre en rojo:** `color:#b01a1a` en cada mención, sin excepción, sin que haga falta pedirlo de nuevo.

**Historial de mediciones hasta la fecha:**

| Fecha | URS (palabras) | URIM (palabras) | URSURIM (palabras) | Páginas URS (est.) |
|---|---|---|---|---|
| 23/08/26 | 94.915 | 17.676 | 112.591 | ~380 |
| 26/08/26 | 101.327 | 18.528 | 119.855 | ~405 |
| 26/08/26 (corrección) | 99.000 | 18.528 | 117.528 | ~396 |

---

## REGLA 10 — UNA LISTA "CANÓNICA" PROPIA NO ES VERDAD VERIFICADA, ES UNA HIPÓTESIS QUE HAY QUE SEGUIR COMPROBANDO

Distinta de la Regla 1 (no tocar de memoria). Esta es más concreta y más cara: **una lista que yo mismo construí y verifiqué en un momento de la sesión puede seguir estando incompleta**, si esa verificación se apoyó en una búsqueda de nombres conocidos en vez de mirar el documento entero de verdad.

**El caso que enseñó esto:** se construyó una lista de 37 subsecciones geográficas, verificada con el atributo `data-nivel` y confirmada varias veces durante la tarde. Parecía sólida — HTML válido, conteo estable, sin contradicciones internas. Pero esa lista nunca se preguntó **qué más podría existir que no estuviera ya en ella**. Luis señaló que Cara 1 tiene una octava sección real —"El Continente en Miniatura" / Ibero Intros, con tres piezas completas (CUL-T-UR/A·LEC-T-UR/A, El euskera, El castellano)— que la búsqueda por nombres conocidos jamás iba a encontrar, porque no llevaba la marca `data-nivel` y su nombre no estaba en ninguna lista previa.

**La diferencia con la Regla 1:** no tocar de memoria evita inventar dónde está algo. Esta regla va un paso más allá: evita dar por cerrada una lista solo porque cada elemento de ella, uno a uno, se verificó bien. **Una lista puede estar hecha de piezas verificadas y aun así estar incompleta como conjunto.** La pregunta correcta no es "¿está bien cada entrada de mi lista?" — es "¿qué hay en el documento que mi lista no contempla?".

**Procedimiento cuando se necesite un recuento estructural completo:** no partir de una lista de nombres esperados y buscar cada uno. Recorrer el documento de principio a fin, cabecera por cabecera, y dejar que la lista se construya desde lo que hay, no desde lo que se espera encontrar.

---

## REGLA 11 — `data-nivel` ES MÉTODO FIJO DESDE HOY, NO PARCHE DE UNA SOLA SESIÓN

Toda cabecera nueva —de Cara, de subsección, de categoría— lleva su atributo `data-nivel` puesto en el mismo momento en que se crea, nunca como paso posterior. `data-nivel="cara"`, `data-nivel="sub"` o `data-nivel="categoria"`, según corresponda.

**Por qué hacía falta esta regla:** casi todo el trabajo de hoy fue encontrar cabeceras reales, bien escritas, correctamente situadas — que llevaban semanas o meses existiendo sin la marca, porque `data-nivel` nació hoy mismo y nadie volvió atrás a ponérsela a lo ya escrito hasta que hizo falta contar algo. No fue un fallo de construcción del libro. Fue una herramienta nueva aplicada tarde sobre contenido viejo.

**La lección de fondo, más allá de esta marca en concreto:** cualquier convención técnica nueva que se decida a partir de ahora —de nombrado, de estructura, de marcado— se aplica also hacia atrás, sobre lo ya existente, en la misma sesión en que se decide. No se deja para "cuando haga falta contar algo" — ese "cuando haga falta" siempre llega, y cuesta más tarde que ahora.

---

## REGLA 12 — `class="pieza"` TAMBIÉN PUEDE FALTAR, NO SOLO `data-nivel`

El mismo problema de la Regla 11 —marcas técnicas nuevas nunca aplicadas hacia atrás sobre contenido viejo— no se limita a las cabeceras. Las piezas de contenido también pueden carecer de `class="pieza"`, y eso hace que cualquier barrido que cuente `el.classList.contains('pieza')` las salte, sin más que dejarlas invisibles.

**El caso de hoy:** 34 `<details>` con `<summary>` real carecían de la clase. De esas, solo 6 eran piezas independientes de verdad —cinco de Etimología Insurgente (Absurdo, Susurro, Turba, Hurón, Laurel) y una de Bonus Tracks (Sulfuro y Oscuridad)—. Las otras 28 eran notas de bibliografía anidadas dentro de dos piezas de Epílogo, correctamente sin clase propia, porque no son piezas independientes — son sub-entradas de una pieza mayor que ya cuenta por sí sola.

**La distinción que hay que hacer siempre antes de marcar:** un `<details>` sin clase no es automáticamente un error. Antes de añadir `class="pieza"` a cualquiera, comprobar con `.closest('details.pieza')` si ya vive dentro de otra pieza mayor. Si tiene padre-pieza, se queda como está — es una nota interna, no una pieza nueva. Si no tiene padre, es una huérfana real y necesita la clase.

**Procedimiento de verificación completa, de ahora en adelante:** cuando se dude de la fiabilidad de un conteo, comprobar dos cosas por separado, nunca solo una — cabeceras con `data-nivel` (Regla 11) y piezas con `class="pieza"` (esta regla). Un documento puede tener las cabeceras perfectas y las piezas rotas, o al revés.

**Por qué las búsquedas de texto plano seguían fallando incluso con el título correcto:** las seis piezas huérfanas de hoy llevaban el propio UR marcado en rojo dentro del título —"ABS<span>UR</span>DO", "S<span>UR</span>O" de Sulfuro—, la firma visual del libro rompiendo, una vez más, cualquier búsqueda que no la contemple. La solución que funcionó: localizar por posición exacta del `<details>` compartido, verificando el texto en una ventana amplia después, no buscando el título como cadena única.

---

## REGLA 13 — LAS CABECERAS SE REPITEN POR CADA PIEZA AÑADIDA, NO SE COMPARTEN

URIM tiene un espejo completo de las 37 subsecciones y las 6 Caras, construido una sola vez, al principio de la zona URIM, justo tras Informes Maestros. Esto no estaba en duda y nunca debió estarlo.

**Lo que sí generó confusión real durante horas:** cada vez que una pieza nueva se añadió a una subsección de URIM a lo largo de meses de trabajo, el propio texto de la cabecera ("◦ Euskal Herria", por ejemplo) se repite justo antes de la pieza nueva, en vez de compartir una sola cabecera para todas las piezas del grupo. Tres piezas de Euskal Herria significan tres repeticiones de "◦ Euskal Herria", una delante de cada una — no una cabecera con tres piezas debajo.

**Por qué esto rompió el conteo durante toda la sesión:** cualquier barrido que trate "la siguiente marca con nombre distinto" como el límite de una sección malinterpreta cada repetición del mismo nombre como si fuera ruido, o —peor— cuenta solo hasta la primera repetición, dejando fuera las piezas siguientes del mismo grupo.

**La solución correcta, ya aplicada:** al recorrer las marcas `data-nivel` en orden, fusionar las que tengan el mismo nombre y la misma zona si aparecen consecutivas, tratándolas como una sola sección continua. Solo un cambio real de nombre marca el final de verdad.

**El coste de no haberlo visto antes:** una tarde entera de correcciones sobre correcciones, incluyendo la creación de cabeceras nuevas donde ya existían —repetidas, correctamente— cabeceras reales sin marcar. Luis lo dijo con toda razón: URIM siempre fue el espejo completo, nada faltaba, lo que faltaba era entender cómo se repite dentro de él.

---

## REGLA 14 — CUMPLIMIENTO ESTRICTO: NINGÚN MOVIMIENTO SIN CONTABILIZAR EN EL MARCADOR

A partir de hoy, sin excepción: **cualquier cambio que altere el número de piezas de una categoría o subsección —crear, mover, fusionar, borrar, renombrar con piezas dentro— actualiza el Marcador Fonomático en el mismo momento**, no después, no "cuando se acumulen varios cambios". Dejarlo pasar es lo que produjo el desajuste de hoy: el total decía 90 cuando el recuento real daba 92, porque una fila (Antártida) se quedó en 0 después de un movimiento que no se reflejó en la tabla.

**Procedimiento obligatorio tras cualquier operación que toque piezas:**
1. Identificar qué fila o filas de la tabla se ven afectadas por el cambio.
2. Recalcular esa fila con el método fiable (marcas `data-nivel` fusionadas por nombre repetido, nunca de memoria).
3. Actualizar la fila de categoría/subsección Y la fila de total de la Cara correspondiente si aplica.
4. Actualizar TOTAL DEL LIBRO en el mismo paso, no en uno posterior.
5. Verificar con un recuento fresco cuando haya dudas — no fiarse de la suma acumulada de operaciones anteriores.

**Nunca dejar un "ya lo actualizaré después" para un cambio de piezas.** El coste de posponerlo es exactamente lo que pasó hoy: una fila desactualizada que nadie recuerda revisar hasta que alguien pregunta por qué el total no cuadra.

---

## PENDIENTE PARA LA PRÓXIMA SESIÓN — AUDITORÍA NUMÉRICA COMPLETA

Luis pidió explícitamente, al cierre de la sesión del 28/08-01/09, una auditoría numérica completa del Marcador Fonomático antes de confiar del todo en los totales. Motivo: demasiadas correcciones seguidas sobre el mismo número en una sola sesión (90 → 92 → 91 → 92) por fallos de método distintos cada vez —fila sin fila, pieza duplicada, archivo entregado desincronizado del verificado—. La confianza no se restaura con una explicación más; se restaura con un recuento fresco, íntegro, hecho con la cabeza descansada, no arrastrando la cadena de parches de hoy.

**Al retomar:** no partir de los números actuales como ciertos. Recontar cada categoría y subsección desde cero, con el método de marcas fusionadas por nombre repetido (ya corregido y documentado en las Reglas 11-13), y verificar con `diff` que el archivo entregado coincide exactamente con el verificado antes de dar cualquier cifra por buena.

---

## REGLA 15 — `data-excluir-total="true"` PARA LO QUE NO ES LIBRO

Marcador Fonomático y Al Yazirat Tarif tienen marca `data-nivel="categoria"` porque estructuralmente delimitan una zona del documento —hace falta para que el conteo por marcas no se desborde hacia ellas—, pero **nunca cuentan en el total del libro**: no son narrativa, son panel de control y valoración económica del propio trabajo.

Ambas llevan ahora el atributo `data-excluir-total="true"` en el mismo div de su cabecera. Cualquier script de auditoría futuro debe filtrar por este atributo —`:not([data-excluir-total])`— en vez de mantener una lista de nombres excluidos a mano en el propio script. La lista a mano es exactamente el tipo de cosa que se olvida entre sesiones; el atributo en el documento no se olvida nunca, porque vive donde vive el dato.

Si en el futuro aparece una tercera categoría de este tipo —estructural pero no narrativa—, lleva el mismo atributo desde el momento en que se crea, no como parche posterior.

---

## REGLA 16 — MÉTODO DE AUDITORÍA COMPLETA, PASO A PASO (usado el 01/09/2026)

Procedimiento exacto para verificar toda la tabla de Análisis de Construcción contra la realidad del HTML, sin depender de memoria ni de parches sueltos. Resultado de la primera auditoría completa: **56 filas, 10 columnas numéricas, 1 sola discrepancia real** (Etimología Insurgente, Semillas 2→1).

**Paso 1 — Fotografiar la tabla actual, tal cual está, sin tocarla.** Extraer las 56 filas × 11 columnas con Playwright, guardar como JSON de referencia. Este es el "antes" con el que se compara todo lo demás.

**Paso 2 — Recalcular desde cero, sin mirar la tabla, usando SOLO el HTML.** Recorrer todas las marcas `data-nivel`, fusionar las consecutivas del mismo nombre+zona (Regla 13), excluir cualquier marca con `data-excluir-total="true"` (Regla 15), y para cada marca resultante contar: piezas `class="pieza"`, cuántas llevan "NO TOCAR" (selladas), cuántas llevan "RAYUELAS", palabras totales. Fusionar después URS+URIM del mismo nombre en minúsculas para tener el total por categoría/subsección.

**Paso 3 — Recalcular Compost y Semillas por separado, leyendo etiquetas DESTINO reales.** Estas no se derivan de `data-nivel` —dependen de una etiqueta de texto libre dentro de cada pieza de Semillas/Compost—. Localizar cada `DESTINO:` en el HTML crudo, cortar en el `</div>` que la cierra (nunca fiarse de textContent plano, mezcla piezas distintas sin separador). Asignar solo las que tengan destino claro a una subsección; las que digan "proyecto propio" o "sin destino" no cuentan en ninguna fila.

**Paso 4 — Comparar campo a campo, fila a fila.** Restar tabla actual menos recálculo fresco en las seis columnas numéricas (URS, URIM, Total1, Compost, Semillas, Total2) y las cuatro añadidas (%Sello, Rayuelas, Palabras, Páginas). Cualquier diferencia es una discrepancia a revisar antes de dar la tabla por buena.

**Aviso real de esta sesión:** al comparar Páginas, una función de limpieza de número trató "0.3" como separador de miles y lo leyó como "3.0" — falso positivo. Antes de reportar una discrepancia como real, comprobar el valor bruto de la celda directamente, no fiarse ciegamente del script de comparación tampoco a él.

**Paso 5 — Corregir solo lo que de verdad discrepa, con verificación de tamaño en cada cambio**, igual que cualquier otra edición del documento. Nunca reescribir una fila entera si el fallo es de una sola celda.

---

## RESOLUCIÓN PRIORITARIA PENDIENTE — TIMMUR: HIMALAYA VERTICAL, mesa de mezclas

Marcada explícitamente por Luis como importante y prioritaria (01/09/2026). La pieza vive en URS, Asia del Sur · Indo-Ganges, con marcas `(*-sub) (*-amp)` en el título — la segunda es nueva, significa "ampliación pendiente, prioritaria, ya documentada en dossier propio dentro de la pieza".

**El asunto real:** la investigación completa de Exity sobre las guerras sino-nepalesa y anglo-nepalesa contiene material —Betrawati 1792, el asedio de Nalapani 1814, los tratados fijando ríos como frontera literal— que es, según la propia lectura de Luis, "casi un capítulo entero sobre agua-como-arma-de-guerra que el libro no tiene todavía" y que encaja con la tesis central del libro más que buena parte de lo ya escrito. El dossier completo, con los nueve hallazgos ordenados por gravedad, vive dentro de la propia pieza en urtz.html, debajo de las glosas.

**La decisión que falta, en mesa de mezclas aparte:** si ese material se incorpora al cuerpo actual, se convierte en una segunda pestaña dentro de la misma subsección, o ambas cosas a la vez. No se decide sin Luis delante, y el propio dossier ya advierte que el volumen del material pesará en esa decisión.

---

## ACTUALIZACIÓN — RESOLUCIÓN PRIORITARIA TIMMUR, mayormente cerrada (01/09/2026)

La pieza se reescribió con Betrawati, Nalapani y el Tratado de Sugauli integrados directamente en el cuerpo (secciones 3, 4 y 5). Los tres hallazgos más graves del dossier anterior —"Betrawati no está", "Nalapani no está", "los tratados no lo dicen"— quedan resueltos: ya están, con nombre propio, dentro del capítulo.

**Lo que queda pendiente, de menor prioridad, sin dossier propio todavía:** los elefantes como puentes vivos en el Gandak, la emboscada fluvial de Jitgadh, la guerrilla nocturna usando el ruido del río como camuflaje, la ingeniería hídrica de los fuertes gorkha (cisternas, acueductos de bambú) y la enfermedad por agua contaminada como causa de bajas. Sigue siendo material real y verificado, pero ya no es "lo más grave que falta" — es ampliación posible, no urgencia.

La pieza lleva las marcas `(*-sub) (*-amp)` en el título, a la derecha, formato correcto confirmado contra el de otras piezas selladas.

---

## REGLA 17 — MAQUETACIÓN FIJA DE PIEZA, DE CONSULTA OBLIGATORIA ANTES DE ESCRIBIR

El fallo del 01/09/2026 con Timmur: se improvisó una estructura interna de pieza —h3 repetido por cada subsección, sin título dentro del cuerpo, marcas mal colocadas— en vez de consultar el formato ya establecido. No fue una decisión estética nueva; fue no mirar antes de escribir, el mismo fallo de proceso que ya costó una tarde entera con los números del Marcador, aplicado esta vez a maquetación. No hay motivo para que esa parte del trabajo escape a la misma disciplina.

**A partir de ahora, esto no se revisa capítulo a capítulo. Se consulta aquí, siempre, antes de escribir cualquier pieza nueva:**

Estructura fija de una pieza (`<details class="pieza">`):

```
<details class="pieza" data-s="[palabras clave]" style="margin:0;">
<summary style="font-family:'Courier Prime',monospace; font-size:0.88rem; color:#b01a1a; cursor:pointer; padding:0.4rem 0; letter-spacing:0.05em; list-style:none; border-bottom:1px dotted rgba(176,26,26,0.3);">
<span style="font-size:0.7rem; margin-right:0.5rem;">&#9654;</span>TÍTULO<span style="float:right; color:#b01a1a; font-weight:bold;">[&#9760; NO TOCAR!!! solo si está sellada] (*-marca) (*-marca)</span>
</summary>
<div style="padding:0.5rem clamp(2rem,5vw,4rem) 1rem;">
<div style="height:4px; background:#b01a1a; width:100%; margin:3rem 0 1.5rem 0;"></div>
<h3 style="font-family:'Bebas Neue',Impact,'Arial Narrow',sans-serif; font-size:clamp(1.6rem,4vw,3.4rem); line-height:0.95; letter-spacing:0.02em; color:#1a1a1a; margin:0 0 0.5rem 0;">TÍTULO (repetido, idéntico al de la pestaña, una sola vez)</h3>
[opcional: subtítulo en <div style="font-family:'Courier Prime',monospace; font-style:italic; font-size:0.95rem; color:#555; margin:0 0 1.5rem 0;"> — SOLO si Luis lo da, nunca inventado]
[por cada subsección interna:]
<h4 style="font-family:'Bebas Neue',sans-serif; font-size:1.15rem; letter-spacing:0.1em; color:#1a1a1a; margin:2.2rem 0 1.1rem 0; border-top:1px solid rgba(176,26,26,0.2); padding-top:1.1rem;">Título de sección</h4>
<p style="font-family:'Courier Prime',monospace; font-size:1.02rem; color:#222; line-height:1.85; margin-bottom:1.1rem;">Párrafo.</p>
</div>
</details>
```

**Puntos que no admiten variación:** el h3 grande aparece UNA sola vez, para el título de toda la pieza — nunca se repite por subsección. Cada subsección interna usa h4, pequeño (1.15rem), nunca h3. Las marcas `(*-...)` van siempre dentro de un `<span style="float:right;...">` en el propio summary, nunca como texto plano después del título. El título vive tanto en el summary como repetido dentro del cuerpo — nunca solo en uno de los dos sitios.

**Verificado byte a byte contra Islandia I (`islandia isla que respira`) el 01/09/2026** — cualquier duda futura sobre el formato se resuelve comparando contra esta regla, no releyendo un capítulo al azar cada vez.

---

## REGLA 18 — EL SISTEMA REAL DE GLOSA: NUMERADA, CON SUPERÍNDICES EN EL CUERPO

Verificado contra 30 piezas reales del libro el 01/09/2026, tras un segundo fallo de maquetación en Timmur (la Regla 17 cubrió el título y las subsecciones, pero no cubrió esto). No existe una sección "GLOSAS" con párrafos sueltos sin numerar — eso fue, otra vez, una invención sin comprobar.

**El sistema real, exacto:**

En el cuerpo del texto, cada término que va a tener glosa lleva un superíndice numerado en su primera aparición:
```
...el río Betrawati<sup class="gr">(4)</sup>, afluente del Trishuli...
```

Al final de la pieza, una sola cabecera "GLOSA" (**singular**, nunca "GLOSAS") con el título de la pieza:
```html
<div style="font-family:'Bebas Neue',sans-serif; font-size:0.95rem; letter-spacing:0.25em; color:#b01a1a; margin-bottom:0.7rem;">GLOSA &middot; [TÍTULO DE LA PIEZA]</div>
```

Seguida de una lista `<ul>`, con cada entrada numerada en el mismo orden en que aparecen los superíndices en el cuerpo:
```html
<ul style="font-family:'Courier Prime',monospace; font-size:0.92rem; line-height:1.7; color:#444; padding-left:1.1rem; margin:0;">
<li><span style="color:#b01a1a; font-size:0.78em;">(1)</span> <strong>Término</strong>: definición.</li>
</ul>
```

**No todas las piezas llevan glosa** — Islandia I no tiene ninguna, Indo-Ganges tiene doce. Se usa cuando el texto tiene términos propios, técnicos o mitológicos que necesitan definirse aparte sin cortar la prosa narrativa.

**El h4 de subsección (Regla 17) ya estaba bien verificado y confirmado de nuevo**: negro (#1a1a1a), sin cursiva, 1.15rem. No hay ningún subtítulo rojo en cursiva encontrado en las piezas comprobadas hasta ahora — pendiente de que Luis señale dónde lo ve exactamente, antes de inventar una tercera variante sin comprobar.

---

## REGLA 19 — BUSCAR TEXTO CON "UR" NUNCA COMO PALABRA CONTIGUA

Hallazgo del 01/09/2026: seis párrafos sueltos (ZIGURAT, RESURRECCIÓN, DICTADURA, LUJURIA, SABIDURÍA, TURISMO) llevaban tres sesiones "desaparecidos" de cualquier búsqueda en URS, pese a estar físicamente ahí, flotando fuera de cualquier pieza entre Susurro y Turba. El motivo: cada palabra con UR dentro lleva el fragmento coloreado en su propio `<span>` — "ZIG<span>UR</span>AT", nunca "ZIGURAT" contiguo. Cualquier `content.find("ZIGURAT")` falla siempre, por diseño del propio libro, no por error de búsqueda.

**Regla:** al buscar cualquier término que contenga las letras U-R en cualquier posición, buscar por fragmentos (`'ZIG'` y `'AT'` por separado, o usar Playwright leyendo `textContent` ya renderizado, que sí une los fragmentos) — nunca dar por buena una ausencia de resultado de una búsqueda de texto plano sin antes comprobar si la palabra contiene UR.

**Aviso serio sobre el propio método de borrado:** en el primer intento de localizar el cierre de este bloque, un patrón de búsqueda que no encontró nada devolvió `-1`, y usar ese `-1` como límite de un `rfind()` posterior buscó "hacia atrás casi hasta el final del archivo", a punto de borrar 744.974 caracteres en vez de 1.682. Se detectó antes de guardar por la propia verificación de tamaño (Regla ya existente), pero confirma por qué esa verificación nunca es opcional: cualquier búsqueda que pueda devolver -1 sin comprobarlo antes de usarla en otra operación es una bomba silenciosa.
