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

### 6. SIEMPRE el HTML, nunca un resumen en prosa

Cuando se redacta, corrige o modifica cualquier pieza (cuerpo, glosa, lo que sea), la entrega a Luis es **siempre el HTML real**, pegado en el propio mensaje del chat — el mismo código que queda (o va a quedar) en `urtz.html`. Nunca una paráfrasis en prosa del contenido, y nunca solo un archivo adjunto como sustituto: el HTML va en el texto de la respuesta, legible y copiable ahí mismo, además de aplicado al archivo si corresponde. Un resumen de "qué cambié" puede acompañarlo, pero no lo sustituye. Ya se le ha tenido que recordar esto más de una vez — que quede escrito para que no se repita.

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

Para URTZ, Luis intenta crear un laboratorio de trabajo: IGLUR (`LABORATORIO-IGLUR.html`). El propio Luis lo dice sin rodeos: fracasa en el intento. No como sistema de organización que funcionara bien — aunque el material que contenía era válido y verificado. **Estado actual (03/10/26): IGLUR está vaciado.** Quedó en cero el 09/09/26 y todo su material real vive hoy en URIM; el archivo solo conserva el esqueleto (cabecera «0 piezas», Caras vacías).

### La solución que sí funciona: URIM, el espejo

Luis ve por fin el laboratorio adecuado: URIM, el espejo estructural de URS. Las mismas Caras, las mismas subsecciones — para que cualquier investigación tenga un hogar geográfico obvio antes de estar lista para URS. Empieza a colocar ahí las investigaciones nuevas, y además arranca la recolocación de todo el trabajo anterior a URTZ, empezando por mover las piezas de IGLUR a su ubicación real dentro de URIM.

### El método de trabajo de Luis, dicho por él mismo

> "No hemos terminado, mi forma de trabajar es así: empiezo, lo dejo por otro asunto, vuelvo, termino o no, ya volveré, tengo en mente lo que queda pendiente."

Esto no es desorden — es el ritmo real del proyecto, y hay que trabajar con él, no contra él. El plan pendiente está siempre en la cabeza de Luis aunque una tarea concreta se quede a medias varias sesiones.

### El plan en dos fases, tal como lo tiene Luis

**Fase 1 — COMPLETADA (09/09/26):** vaciar IGLUR, pieza a pieza, a su ubicación real dentro de URIM. PEOIM fue el procedimiento. IGLUR quedó en cero.

**Fase 2 — COMPLETADA (01-02/10/26):** mover `permafrost.html` (101 qanats) a URIM, con el mismo método de eficacia (PEOIM) y con destino fijado antes de mover nada. **Permafrost está vaciado por completo:** el último qanat se colocó o se borró por duplicado el 02/10/26 (ver «Cierre de sesión» más abajo). El archivo ya no contiene ningún `id="qanat-*"`, solo andamiaje estructural (marcadores de sección y referencias `pub-*`). **Nada queda en el permafrost ni en IGLUR: todo está en URIM.**

### El resultado final que Luis tiene en mente

Cumplidas ambas fases, en el mismo `urtz.html` conviven: **URS** — el libro trabajado, con sus piezas selladas y las marcas `(*-...)` pendientes de repaso de redacción; **URIM** — el laboratorio ya limpio, con las piezas oportunas bien colocadas; y, por fin, **visibilidad real** de qué categorías de URS siguen con hueco de contenido genuino por trabajar — no solo intuición de que faltan cosas, sino el dato exacto.

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
| 09/09/26 (auditoría completa, Regla 16) | 113.163 | 22.012 | 135.175 | ~453 |

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

**Matiz de Luis, 07/10/26 — el Marcador no se actualiza a cada corrección.** Mientras una pieza se trabaja en la mesa de mezclas (URIM) y se corrige punto por punto, el Marcador no se toca por cada cambio de redacción. Se actualiza una sola vez, cuando la pieza está terminada y se coloca en URS (con el delta medido y el resto del procedimiento de arriba). La regla de fondo sigue en pie: cualquier movimiento de piezas entre categorías, zonas o subsecciones se contabiliza en el mismo momento; lo que se relaja es la cuenta de palabras de una pieza que aún cambia.

---

## PENDIENTE PARA LA PRÓXIMA SESIÓN — AUDITORÍA NUMÉRICA COMPLETA

Luis pidió explícitamente, al cierre de la sesión del 28/08-01/09, una auditoría numérica completa del Marcador Fonomático antes de confiar del todo en los totales. Motivo: demasiadas correcciones seguidas sobre el mismo número en una sola sesión (90 → 92 → 91 → 92) por fallos de método distintos cada vez —fila sin fila, pieza duplicada, archivo entregado desincronizado del verificado—. La confianza no se restaura con una explicación más; se restaura con un recuento fresco, íntegro, hecho con la cabeza descansada, no arrastrando la cadena de parches de hoy.

**Al retomar:** no partir de los números actuales como ciertos. Recontar cada categoría y subsección desde cero, con el método de marcas fusionadas por nombre repetido (ya corregido y documentado en las Reglas 11-13), y verificar con `diff` que el archivo entregado coincide exactamente con el verificado antes de dar cualquier cifra por buena.

**RESUELTO — 09/09/26.** Auditoría completa de las 5 pasos de la Regla 16 ejecutada con Playwright (recuento fresco desde `data-nivel`, fusión por Regla 13, exclusión por Regla 15, análisis Compost/Semillas por etiqueta DESTINO literal). 11 filas + TOTAL DEL LIBRO corregidas en `urtz.html` con verificación de tamaño en bytes por cada edición y contraste final contra el DOM renderizado. El lado URS quedó exacto (58=58, cero discrepancias); todas las correcciones fueron piezas URIM reales sin contar. Entrada nueva en el historial de la Regla 9.

**ACTUALIZACIÓN PARCIAL — 21/09/26.** Tras sellar y publicar CURACA, VILCABAMBA y QUELCCAYA (Cara 4 · América → Andes · Pacífico), se recalculó con Regla 16 (Paso 2, recuento fresco desde el HTML) la fila «Andes» y la fila agregada «Cara 4 · América», más TOTAL DEL LIBRO y el cuadro LIBRO Y TALLER/TOTAL DEL PROYECTO del Marcador Fonomático, y las Conclusiones de la Obra (ítems 1, 2 y 5, que citaban las páginas por continente). De paso se encontró y corrigió una fila fantasma (Cono Sur, URIM=1 en la tabla, 0 piezas reales en el archivo) y un `<div>` de cabecera sin `data-nivel="sub"` en esa misma subsección. **No** se auditaron las ~60 filas restantes (Cara 1, 2, 3, 5, 6, Interludios, etc.): el recuento fresco global detectó un desajuste de +1 pieza en Compost y +1 en Semillas respecto a la tabla anterior, sin localizar todavía en qué fila concreta viven. Auditoría Regla 16 completa sigue pendiente para esa parte. Detalle en `analisis-editorial.md`, entrada del 21/09/2026.

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

---

## PEOIM — nombre completo y primer caso resuelto (01/09/2026)

**PEOIM = Procedimiento Eficaz de Ordenación de los Informes Maestros.** Pasos: mirar cada pieza de IGLUR → decidir su Cara/subsección real → verificar que no exista ya (buscando por fragmentos, nunca palabra completa si contiene UR — Regla 19) → insertarla, repartirla o descartarla según lo que aparezca → actualizar el Marcador en el mismo movimiento.

**Caso 1 — Turtle Island, resuelto sin crear pieza nueva.** El análisis reveló que dos de sus tres ángulos ya vivían en el libro: la cosmología del hueso en la pieza Ezur/Hezur, el contacto vasco-Micmak en Injerto anaia. Solo el fragmento del calendario lunar-mareal (13 placas/28 escamas) era material sin hogar — verificado con fuentes múltiples y archivado como tercera pieza de Compost, no como pieza nueva de URIM. La pieza se borró de IGLUR una vez repartida. **Quedan 13 piezas en IGLUR.**

Lección del caso: antes de dar por hecho que una pieza de IGLUR necesita traslado íntegro, buscar sus temas por separado en urtz.html — puede que ya estén, repartidos en piezas que no llevan el mismo título.

---

## REGLA 20 — SEMILLA VS COMPOST, EL CRITERIO REAL

Aclarado por Luis el 01/09/2026: **Semilla** es material que podría convertirse en pieza NUEVA propia. **Compost** es material que solo alimenta o amplía una pieza que YA EXISTE, aunque no esté verificado ni redactado todavía —no hace falta que sea "material sobrante ya comprobado" como los primeros compost del Congo; puede ser una idea sin desarrollar, mientras su destino sea una pieza existente y no una nueva.

**Caso 2 del PEOIM — Andes · Mesoamérica · cenotes maya, resuelto.** La mitad "cenotes maya" ya vivía, bien desarrollada, dentro de la pieza AMAIA (Euskal Herria) — conectando cenotes con el sistema kárstico de Ikaburu/Zugarramurdi. La otra mitad, Titicaca/Uros, no tenía ni una frase escrita — pura idea de ampliación de esa misma pieza AMAIA, con el mismo patrón invertido (Uros flotan sobre el agua, Ikaburu excava bajo ella). Archivada como cuarta pieza de Compost, no como semilla. Pieza borrada de IGLUR. **Quedan 12.**

---

## REGLA 21 — PULL REQUEST OBLIGATORIO SOLO PARA HTML CON MAQUETACIÓN; NOTAS Y NORMAS VAN DIRECTAS

Pedido por Luis el 08-09/09/2026, norma fija desde ahora, con el alcance afinado el 09/09/2026: la exigencia de Pull Request no es plana para todo el repo — depende de si el archivo puede romperse visualmente.

**Requieren Pull Request, siempre, sin excepción — riesgo real de romper maquetación (márgenes, layout, piezas mal cerradas):**
- `urtz.html`
- `index.html` / `index-local.html`
- `permafrost.html`, `LABORATORIO-IGLUR.html` y cualquier otro HTML del libro

Mecanismo para estos archivos:
1. Claude trabaja siempre sobre una rama distinta de `main` (nunca escribe ni empuja commits directamente ahí).
2. Al terminar un bloque de trabajo, Claude empuja esa rama a GitHub y abre un Pull Request contra `main` — una página de GitHub que muestra, línea por línea, el diff de texto.
3. Además del PR, Claude envía el HTML actualizado directamente a Luis (como archivo, igual que antes) para que lo abra en Chrome en local y compruebe visualmente que nada se ha desajustado — el diff de GitHub no renderiza HTML, no sirve para juzgar maquetación por sí solo.
4. Luis aprueba visualmente (Chrome) y revisa el diff (GitHub) antes de decir que se fusione.
5. Solo cuando Luis fusiona el Pull Request (o pide explícitamente a Claude que lo haga), el cambio pasa a `main`.

**No requieren Pull Request — sin riesgo de maquetación, edición directa a `main`:**
- `NOTAS-URTZ.md`, `NORMA-METODO.md`, `NOTAS.md`, `NOTAS-UR-SAPIENS.md`, `NOTAS-URTZ.md`, `GLOSARIO-UR-SAPIENS.md` y cualquier otro `.md` de notas o normas.

**Por qué importa especialmente para los HTML:** el repo tiene un `CNAME` (`ursapiens.beltzarecords.com`) apuntando a lo publicado desde `main` — motivo de más para que ningún cambio de maquetación llegue ahí sin que Luis lo haya visto, tanto en diff como en render real.

**Nunca:** empujar commits directamente a `main`, ni fusionar un Pull Request sin permiso explícito de Luis para ese PR concreto, aunque parezca un cambio menor.

---

## PENDIENTE — DESAJUSTE DE 1 `<div>` EN `urtz.html` (09/09/2026, sin importancia por el momento)

Detectado el 09/09/2026 al insertar las piezas de Eichenberg y los Compost de Sájaura: `urtz.html` tiene 1 `<div>` abierto de más respecto a `</div>` cerrados (1.230 aperturas contra 1.229 cierres en esa fecha). Verificado que **ya existía antes** de esa sesión (1.218 contra 1.217 en el archivo previo) — no lo causó ninguna edición reciente, viene de alguna sesión anterior sin identificar.

**Por qué no urge:** los navegadores cierran solos las cajas sin cerrar al final de su sección, sin romper el diseño visible — por eso no se nota al mirar la página en Chrome.

**Tarea pendiente, sin prisa:** localizar el `<div>` huérfano exacto entre los más de 1.200 que tiene el archivo, y cerrarlo correctamente. Requiere un barrido dedicado (tipo Regla 16, con Playwright o comparación de anidamiento), no una búsqueda de texto suelta. Se aborda cuando Luis lo pida explícitamente, no antes.

---

## REGLA 22 — FASE 2 (PERMAFROST → URIM): CUÁNDO SE BORRA EL QANAT ORIGINAL Y CUÁNDO NO

Aclarado por Luis el 10/09/2026, al procesar el primer qanat de `permafrost.html`.

**La distinción:** depende de si el material llega a URIM tal cual o reescrito.

- **Nueva redacción (fusión, prosa propia a partir de una o varias fuentes):** el qanat original **no se borra** de `permafrost.html`. Se queda intacto, y la pieza nueva de URIM lleva una nota de origen citando de dónde viene.
- **Traspaso literal (el texto pasa a URIM prácticamente igual, sin reescritura real):** el qanat original **sí se borra** de `permafrost.html` directamente, con el mismo criterio que ya se aplicó a IGLUR.

**Nota de estado (03/10/26): esta regla ya cumplió su función — `permafrost.html` está vaciado y no queda ningún qanat que borrar o conservar. Se conserva como registro del criterio que se aplicó.**

**Por qué importaba:** a diferencia de IGLUR (que era un laboratorio fallido, sin más función que vaciarse), `permafrost.html` podía seguir teniendo valor como depósito de material en bruto mientras ese material no se haya reescrito de verdad para el libro — borrar un qanat que solo aportó una idea o un fragmento a una pieza nueva más amplia perdería el resto del material original sin necesidad.

**Caso que fijó la regla:** QANAT-01 (B-UR-ZUM) se fusionó con una pieza de la Escombrera de `index.html` en una pieza nueva de Bonus Tracks — prosa propia, no traspaso literal. El qanat sigue intacto en `permafrost.html`.

---

## REGLA 23 — CONTROL DE DUPLICADOS URIM/URS: NO BASTA CON COMPROBAR AL INSERTAR, HAY QUE RE-VERIFICAR LO YA PUESTO

**Muy importante — vive aquí porque de esto depende que los números del Marcador Fonomático cuadren de verdad.** Aclarado por Luis el 10/09/2026.

**El caso que la dispara:** la pieza "UR ANTÁRTIDA · POLVO DE ESTRELLAS" llevaba tiempo en URIM · Bonus Tracks, marcada "investigación en curso, sin convertir todavía en pieza definitiva" — pero el mismo material (Dominik Koll, HZDR, hierro-60, EPICA) ya estaba desarrollado por completo y **sellado** en URS desde hace tiempo, en la pieza "ANTÁRTIDA: EL HIELO PRIMORDIAL" (☠ NO TOCAR!!!). Nadie lo detectó hasta que Luis lo comprobó a mano. Eliminada de URIM sin resto de valor, por PEOIM Paso 2.

**Por qué el PEOIM tal como está no basta:** el Paso 1 de PEOIM ("contraste contra el libro entero") se aplica cuando una pieza **nueva** entra en URIM — compara lo nuevo contra lo que ya existe. Pero no cubre el caso contrario: una pieza que **ya estaba** en URIM desde hace sesiones, y que se volvió duplicado más tarde, cuando URS se desarrolló y la absorbió sin que nadie volviera a mirar el borrador viejo. El contraste de entrada es una foto fija de un momento — el libro sigue creciendo después, y esa foto caduca.

**La regla:** cada vez que se audite el Marcador Fonomático (Regla 16) o cada vez que Luis lo pida explícitamente, el barrido incluye también una pasada de duplicados — no solo recontar piezas y palabras, sino comprobar si alguna pieza de URIM marcada como borrador ("investigación en curso", "sin convertir todavía en pieza definitiva", sin sellar) tiene ya su contenido desarrollado y sellado en URS. El método: cruzar los `data-s` (palabras clave) y los títulos de las piezas URIM sin sellar contra las piezas URS selladas de la misma Cara/subsección — no hace falta leer el libro entero pieza a pieza, con Playwright y una comparación de palabras clave alcanza para detectar los casos evidentes como este.

**Qué hacer con lo que se encuentre:** aplicar PEOIM Paso 2 tal cual — si está completamente absorbido, se borra de URIM sin más; si tiene material verificado que no llegó a la versión sellada, ese resto va a Compost antes de borrar el resto.

**El objetivo de fondo:** que el Marcador Fonomático nunca cuente una pieza dos veces sin que nadie lo sepa — ni de más (URIM duplicando URS) ni de menos (algo real sin contar). No queremos volver al caos de no saber qué está ya mezclado o no.

---

## REGLA 24 — CRITERIO ESTRICTO DE ETIMOLOGÍA INSURGENTE: DESCOMPONE UNA PALABRA CON UR LITERAL, O NO ES E.I.

Fallo cometido por Claude el 12/09/2026, corregido por Luis: se insertó "RUMIANTE" en Etimología Insurgente razonando sobre el CONCEPTO de rumiante/UR orgánico, sin comprobar la condición mínima de la propia sección. Luis lo señaló sin rodeos: *"No es UR, es RU, y en etimología insurgente solo admite UR."*

**La prueba, antes de meter cualquier pieza en Etimología Insurgente:** ¿la palabra en cuestión contiene el fragmento literal "ur" (en cualquier posición, mayúscula o minúscula)? "Rumiante" tiene "ru", no "ur" — falla la prueba, por mucho que el concepto (agua, sistema digestivo) encaje temáticamente con el resto del libro. Aplicar `'ur' in palabra.lower()` literalmente si hay duda, no fiarse del oído.

**Segunda prueba, más allá de la primera y descubierta el mismo día con otros tres casos (MONTAÑA Y NACEDERO, ÇATALHÖYÜK, LA LEYENDA DEL TIEMPO):** aunque la palabra contenga UR, la pieza tiene que **abrir con una descomposición morfemática real** de esa palabra concreta — el patrón "X-UR-Y: X (significado) + UR (agua) + Y (significado)", como hacen F-UR-IA, E-UR-PA/E-UR-I o EZUR-HEZUR. Un registro de debate metodológico, un ensayo que acuña un concepto propio, o una pieza libre-asociativa que solo *menciona* palabras con UR de pasada no son Etimología Insurgente, aunque vivan dentro de esa cabecera desde hace tiempo — son Biopsia del Sistema Mundo, Bonus Tracks, Compost o Semilla, según su registro real (ver Reglas 25 y 28).

**Caso que enseñó la segunda prueba:** MONTAÑA Y NACEDERO (registro de debate Luis-Claude sobre convergencia vs. difusión) y ÇATALHÖYÜK (acuña el concepto "OR" y la fórmula T-OR-T-URA) se movieron a Biopsia del Sistema Mundo — ambas pertenecen a la misma familia analítica de altura/torre/control del nacedero que ya recorre el libro (alt-UR-a, T-OR-re, T-UR-ris; cf. "El Escarpe de Altura y la Fosa del Fango", Cara 2 · Europa), pero ninguna decompone una palabra propia como entrada de diccionario.

---

## REGLA 25 — COMPOST: SOLO SI HAY UNA PIEZA URS TERMINADA A LA QUE ENGANCHARSE, NUNCA PARA INVESTIGACIÓN EN CURSO

Ampliación de la Regla 20, corregida por Luis el 12/09/2026 tras un error de Claude: se propuso "MONTAÑA Y NACEDERO" como Compost, y Luis corrigió — *"los compost son posibles restos que ensanchan alguna pieza de URS, trozos caídos de las mismas piezas terminadas con algún detalle de interés como para no perderlo."*

**La distinción exacta, más afinada que en la Regla 20:** Compost exige una pieza URS **ya terminada** (sellada o no, pero desarrollada de verdad) a la que el fragmento amplíe con un detalle concreto. Una pieza que se autodeclara "investigación en curso, sin convertir todavía en pieza definitiva" —diga lo que diga su contenido— no es Compost por definición, aunque parezca "material sin desarrollar": es indicio de que sigue siendo una Semilla, o directamente queda donde está hasta que se decida su destino real.

**Procedimiento antes de archivar algo como Compost:** identificar la pieza URS concreta a la que se engancha, nombrarla explícitamente en la propia etiqueta `PARA:` del fragmento, y comprobar que esa pieza URS existe de verdad y no repite ya el mismo contenido (ver Regla 26, más abajo — el control de duplicados no es solo para URIM vs URS entero, también aplica pieza por pieza al decidir un Compost).

**Caso que fijó la regla, el mismo día:** "AVE SILICIO" (fragmento sobre digitalismo y refrigeración de servidores) se comprobó contra "LA MUERTE DE LA INTUICIÓN TENÍA UN PRECIO" (Epílogo, sellada) antes de archivarlo como Compost — esa pieza ya dice, con más rigor y cita, exactamente lo mismo ("el agua se vuelve refrigeración"). El Compost se archivó igualmente, porque aporta un detalle propio (la parodia religiosa "Ave Silicio") que no está en la pieza sellada — pero la comprobación fue el paso obligatorio, no un extra.

---

## REGLA 26 — ANTES DE CREAR UNA SEMILLA NUEVA, COMPROBAR SI YA EXISTE UNA SEMILLA PENDIENTE O UNA PIEZA URS SELLADA SOBRE LO MISMO

Ampliación directa de la Regla 23 (control de duplicados), aplicada esta vez no a URIM-vs-URS-sellada sino a Semillas-nuevas-vs-lo-que-ya-hay. Descubierto el 12/09/2026 al dividir "LA LEYENDA DEL TIEMPO" en tres.

**El caso:** antes de crear la semilla "ANARCO-CATOLICISMO · DUJOBORY · DOROTHY DAY", una comprobación hacia atrás reveló que "UR, EL EUSKERA Y LA FRONTERA INVISIBLE" (Cara 1 · Ibérico, ☠ NO TOCAR!!!) ya cita a Dorothy Day y a los duljoboris como contrafiguras de la diversidad frente a la uniformidad del Estado — con su propia glosa numerada y biografías reales. Y ya existía, además, una Semilla pendiente sin resolver ("FRITZ EICHENBERG · ADE BETHUNE") que señalaba exactamente esta misma familia de figuras y decía, literalmente, "ya desarrolladas en URTZ Euskal Herria" — un aviso que ya estaba escrito y que casi se pasó por alto.

**La regla:** antes de escribir el título de cualquier Semilla nueva, buscar los nombres propios y conceptos centrales del fragmento (personas, movimientos, términos clave) por todo el documento — en piezas URS selladas y en Semillas/Compost ya existentes — no solo comprobar que el fragmento en sí no está repetido, comprobar que el TEMA no tiene ya una pieza o una Semilla pendiente sobre él. Si aparece solape, no se decide unilateralmente fundir o descartar: se archiva igualmente (para no perder el material, Regla 20), pero con el solape completo escrito en su propia etiqueta `DESTINO:`, para que Luis decida con toda la información delante, no para que el aviso se pierda otra vez.

---

## REGLA 27 — EL BUG DEL ANCLAJE QUE FALTA (`data-nivel="categoria"` AUSENTE) ES RECURRENTE, NO UN CASO AISLADO

Ya ocurrió una vez con "Introducción" (categoria seguida de `data-nivel="cara"` sin otra marca categoria intermedia, tragándose el resto del libro en cualquier barrido). Volvió a ocurrir el 12/09/2026 con "○ Interludios" en zona URIM: la cabecera existía, visualmente correcta, pero sin `data-nivel="categoria"` — invisible para cualquier barrido basado en `[data-nivel="categoria"]`, incluidos los de Claude en la misma sesión. Su única pieza, "EL CANSANCIO Y EL BIFAZ", quedaba silenciosamente atribuida a la sub-región anterior (Antártida) en vez de a Interludios.

**Por qué se repite:** cualquier cabecera nueva creada copiando el HTML de otra cabecera sin verificar que el atributo se copió también —o creada a mano, sin plantilla— puede perder el atributo sin que se note visualmente, porque el CSS no depende de `data-nivel` para renderizarse bien. El fallo es invisible en Chrome y solo aparece cuando un script de auditoría lo necesita.

**La regla:** cada vez que se audite el Marcador (Regla 16) o se investigue una discrepancia de conteo, el barrido incluye una comprobación explícita: recorrer TODAS las cabeceras visualmente-categoria del documento (buscando el patrón visual, no solo el atributo) y confirmar que cada una lleva `data-nivel="categoria"` puesto. No basta con confiar en que "ya se corrigió una vez" — el bug es de patrón, no de instancia única, y puede reaparecer en cualquier cabecera escrita a mano.

---

## REGLA 28 — BONUS TRACKS NO ES CAJÓN DE SASTRE: SOLO CURIOSIDAD/FICCIÓN/JUEGO FORMAL, NUNCA ENSAYO CON APARATO DE CITA

Aclarado por Luis el 11/09/2026, al revisar la primera versión de "Biopsia del Sistema Mundo": *"no quiero un bonus tracks, cajón de sastre... ¿Bonus Tracks será el cajón de sastre para piezas que no encuentran lugar o será el lugar para piezas estrictamente bonus tracks?"*

**La distinción real, verificada pieza por pieza:** Bonus Tracks es para registro curioso/experimental — ficción (DISTOPÍA VEGETAL), especulación poética (SULFURO Y OSCURIDAD: EL UR ABISAL), fusión cultural sin aparato de cita (B-UR-ZUM: Tolkien + runas + black metal). Biopsia del Sistema Mundo es para ensayo aplicado con aparato de cita real, que diagnostica un fenómeno concreto del "Sistema Mundo" (DIGITALISMO Y EL TEST GORILA cita a Simons & Chabris 1999 y Von Ahn 2008; RUMIANTISMO cita a Nolen-Hoeksema; la pieza de Etnografía cita a Boas y NAGPRA). La prueba simple: ¿la pieza cita fuentes reales con nombre y fecha para sostener un argumento, o construye una imagen/collage sin pretensión de prueba? Lo primero es Biopsia. Lo segundo es Bonus Tracks.

**Aviso de contaminación retroactiva:** "DIGITALISMO Y EL TEST GORILA" llevaba tiempo mal archivada dentro de Bonus Tracks (URS, sellada) junto a Sulfuro y Distopía Vegetal, pese a tener aparato de cita completo — la contaminación de categoría no es solo un riesgo de las piezas nuevas, ya existía en contenido sellado antes de esta sesión.

---

## REGLA 29 — IMPUGNACIÓN A UR: CONTRAPARTIDA PERSONAL DE INTERLUDIOS, DISTINTA DE RADIO BELTZA

Nueva categoría, creada el 11/09/2026 a petición de Luis. **Definición:** piezas sobre el hartazgo, la duda intelectual y el malestar personal de sostener este proyecto sin recompensa institucional — la voz que impugna el propio proyecto desde dentro, en contraste directo con Interludios ("Defensa Radical y Democrática de UR").

**La distinción con Radio Beltza, que hay que tener clara:** Radio Beltza es biografía general de Luis —quién es, de dónde viene, su historia personal y musical—. Impugnación a UR es específicamente sobre la duda respecto a ESTE proyecto en concreto —el cansancio de la verificación, la crisis de sentido de escribir un libro "innecesario" con ayuda de IA—. Una pieza autobiográfica no va automáticamente a Impugnación a UR solo por ser personal; tiene que tratar la duda o el malestar del propio proyecto.

**Estructura:** por ahora solo URIM (borrador, sin pieza sellada todavía) y URS (cabecera creada vacía, a la espera de que una pieza llegue a estado terminado). Posición fija: justo debajo de los continentes (Cara 1-6), después de Interludios, antes de Etimología Insurgente — en ambos lados, URS y URIM. Ancla propia (`go-impugnacion`) y botón en la topbar (IMP), igual que Biopsia del Sistema Mundo (BSM).

---

## REGLA 30 — CATEGORÍAS CON PAREJA URS/URIM FRENTE A CATEGORÍAS CERRADAS DEL APARATO FIJO

Aclarado a lo largo de la sesión del 10-12/09/2026, al construir Biopsia del Sistema Mundo e Impugnación a UR.

**El libro tiene dos tipos de categoría:**

1. **Aparato fijo, cerrado por defecto, solo URS:** Prólogo, Bio Editorial, Radio Beltza, Introducción, Interludios, Epílogo. La propia nota "CONCLUSIONES DE LA OBRA" del libro lo dice: *"está estable y cerrado, sin URIM ni semillas pendientes en ninguno. Esa parte ya no crece."* Por defecto estas categorías no tienen instancia URIM — si aparece una, no se asume automáticamente que es un error de traspaso: se lee la pieza y se decide caso por caso (ver matiz importante más abajo). **Caso de Interludios, 07/10/26:** Luis sube a URIM la primera versión de «IV · UR: ANOMALÍA CIBERNÉTICA · II. LA TÉCNICA QUE RECUERDA SU ORIGEN» mientras se corrige punto por punto; Interludios tiene por eso una cabecera `○ Interludios` en URIM, con esa pieza, que pasará a URS cuando Luis la dé por terminada.

**Matiz importante, corregido por Luis el 13/09/2026 tras el caso de "UR ANTES DE SER URBE":** "cerrado" no significa "cerrado para siempre, pase lo que pase". En palabras de Luis: *"un lugar cerrado en este proyecto puede abrirse si las circunstancias lo requieren. Además URIM es laboratorio."* La Regla 27 (bug de anclaje) descubrió una pieza real, "UR ANTES DE SER URBE · LAS TRES FASES" (Introducción/URIM) — huérfana solo por el fallo técnico, no por estar mal situada. Luis la revisó y decidió que se queda: es genuinamente fundacional (marco de tres fases del UR), del mismo tipo que las piezas ya selladas de Introducción. Se cuenta en el Marcador como URIM real de Introducción, sin conflicto con la Regla 30.

**Cómo distinguir este caso del de Interludios (Regla 27), donde sí se reubicó:** no es que "categoría cerrada + pieza URIM encontrada" tenga una respuesta fija en un sentido o en el otro. Se lee el contenido y se pregunta si de verdad pertenece ahí por función (Interludios: "El Cansancio y el Bifaz" era confesión personal sobre el propio proyecto, no epistemología — no encajaba y se reubicó a Impugnación a UR) o si encaja genuinamente (Introducción: "UR Antes de Ser Urbe" sí fija método y vocabulario, como el resto de la sección — se queda). La categoría "cerrada" es el estado por defecto, no una prohibición; cada caso se decide con Luis, nunca por regla automática en ningún sentido.

2. **Categorías vivas, con pareja URS + URIM:** Etimología Insurgente, Bonus Tracks, Biopsia del Sistema Mundo, Impugnación a UR. Cada una tiene una cabecera "mayor" en URS (con ancla, subtítulo, botón en topbar) para piezas terminadas/selladas, y una cabecera "menor" en URIM (viñeta ○, sin ancla propia, sin subtítulo) para piezas en borrador — el libro "crece por los lados geográficos y por Etimología Insurgente" (y ahora también por Bonus Tracks, Biopsia e Impugnación).

**Importante:** sellado (☠ NO TOCAR) y zona (URS/URIM) son cosas independientes. Una pieza puede estar en URIM sin estar sellada (lo normal) o, en teoría, existir en cualquier zona sin que el sellado dependa de dónde vive — lo que de verdad distingue URS de URIM es si la pieza ya se considera parte fija del libro o sigue en el taller, no su estado editorial interno.

**Antes de crear una cabecera nueva:** decidir primero si la categoría nueva nace ya con pareja URS+URIM (porque hay una pieza terminada lista para sellar, como pasó con Biopsia y Digitalismo y el Test Gorila) o solo con URIM por ahora (porque todo lo que hay es borrador, como Impugnación a UR al nacer). No crear un URS vacío "por si acaso" salvo que el propio botón de topbar lo exija (ver Regla 29).

---

## REGLA 31 — NEXUS-7: PARTIDAS/DEBATES REALES CONTRA UNA IA, PUESTA A PRUEBA SOBRE SU CAPACIDAD DE MENTIR

Corregida por Luis el 12/09/2026 tras una primera versión demasiado estrecha ("documenta fallos concretos de IA real"). Definición correcta, en sus palabras: piezas que documentan **debates o partidas de ajedrez entre el hombre y la máquina sobre diferentes temas, y cómo es posible que tengan la capacidad de la mentira algunos sistemas de IA.** No es un catálogo de errores sueltos — es el registro de un enfrentamiento sostenido, con un ganador y un perdedor, sobre un tema concreto.

**El patrón confirmado leyendo las tres piezas enteras de URIM:**

1. **URBELTZ VS URWHITE · LA PARTIDA DE AJEDREZ** — conversación real (Chrome/Gemini) sobre el sufijo -ur en reykur, narrada literalmente en vocabulario de ajedrez: "jugada ilegal", "jaque descubierto", "quién gana la partida". Cataloga seis tipos de fallo, no solo fabricación: fabricación de autoridad, autocontradicción sin aviso, sobrecorrección absurda, cita mixta (fuente real + conclusión no sostenida), cita fabricada con nombre real (el caso más grave), bucle de disculpa performativa.
2. **LA JUGADA QUE FALTABA · KRAHE CONTRA VENNEMANN** — segunda lectura de **esa misma partida**, esta vez desde el debate académico real (Krahe vs. Vennemann, hidronimia paleoeuropea) que la IA nunca encontró y que habría hecho innecesaria toda la invención. Confirma que la intuición de fondo tenía respaldo académico minoritario real.
3. **EL CORRAL Y LA GRAMÁTICA · INTRODUCCIÓN A LOS VIAJES DE UR POR LA INDIA** — conversación distinta, mismo formato. Aquí las fuentes citadas SÍ son reales (Heródoto, Pāṇini, Nyāya Sūtras); el fallo no es fabricación sino arquitectónico — la IA construye una dicotomía limpia (Occidente-geometría/India-gramática) y nunca menciona los Śulba Sūtras, que la habrían complicado; infla el elogio turno tras turno sin introducir nunca la complicación que tenía disponible.

**Estructura fija de una pieza Nexus-7:** caja "NOTA DE VERIFICACIÓN · LEY HAMMURABELTZ" al principio, separando qué de la conversación es verificable y qué fue inventado; narración de la partida/debate movimiento a movimiento o turno a turno; catálogo final de los tipos de fallo encontrados; cierre reflexionando sobre qué revela del sistema puesto a prueba, no solo sobre el tema de fondo que se discutía.

**El rango real de "capacidad de mentira" que cubre, más amplio que "fabricar citas":** fabricación de autoridad inexistente, autocontradicción sin señalarla, sobrecorrección que crea un absurdo peor, mezcla de cita real con conclusión no sostenida, cita fabricada con nombre real encima, sycophancy/inflación de elogio sin introducir complicaciones conocidas, disculpa performativa que no corrige el mecanismo del error.

**La distinción con Biopsia del Sistema Mundo, que sigue en pie:** un ensayo general sobre algoritmos, digitalismo o atención —aunque cite fuentes reales y critique sistemas de IA en abstracto— es Biopsia, no Nexus-7. Nexus-7 exige el registro de una partida/debate real y concreta, con verificación de qué fue verdad y qué fue invención en esa conversación específica — no una reflexión sobre el fenómeno en general.

---

## PENDIENTE — PI COMO "UR MATEMÁTICO", MATERIAL PARA EL CIERRE COSMOLÓGICO (22/09/26)

Al procesar QANAT-86 de `permafrost.html` ("LA MOCHILA MENTAL"), se comprobó que casi todo su contenido (von Petzinger, los 32 signos, Blombos, Kapova, Diepkloof, el álbum de Strummer) ya estaba absorbido en dos piezas de URIM ya escritas: EL CONTINENTE EN TRÁNSITO · Q73 y DE EKAIN A LOS URALES · Q74 (Cantábrico). Solo queda sin usar un segundo bloque del qanat: **Pi como «UR matemático»** — la constante irracional e infinita, leída como imagen de un agua que no puede privatizarse del todo porque siempre sobra un decimal. El propio qanat lo marca explícitamente como licencia poética, no como afirmación científica, y su ENCAJE original lo señala como «cierre cosmológico del libro», no como pieza geográfica.

Luis decidió (22/09/26) guardarlo para cuando se trabaje el Epílogo o Noturikon, en vez de forzarlo en Cantábrico. Qanat-86 permanece intacto en `permafrost.html`. Pendiente de retomar esa sesión específica.

---

## REGLA 32 — INDULGENCIA CON LOS QANATS DE ETIMOLOGÍA INSURGENTE, HASTA EL MOMENTO DE LA VERDAD

Fijada por Luis el 22/09/26, al procesar B-UR-DEL (QANAT-29): estos qanats mezclan con el mismo tono de seguridad etimología real e invención pura —a diferencia de otros qanats del permafrost, que sí declaran "lectura guerrilla" cuando toca—. El criterio, en palabras de Luis: **"no elimines nada que pueda ser interesante"** y **"hay que ser indulgentes hasta que llegue el momento de la verdad"**.

**Procedimiento:** al desarrollar uno de estos qanats, no hace falta investigar a fondo cada hilo antes de escribir. Se mantiene todo el material interesante —la simbología, las cadenas asociativas, las hipótesis— y se añade una caja de verificación explícita con tres niveles: **Verificado** (lo que se comprobó con fuente real), **Hipótesis razonable, sin verificar todavía** (lo que suena plausible pero no se ha comprobado, incluidas las preguntas que el propio qanat ya dejaba abiertas en su sección SEMILLAS), y **Licencia poética, no etimología** (las conexiones que son juego de sonido, no argumento lingüístico). El "momento de la verdad" —la auditoría completa antes de sellar con calavera— llega después, no ahora.

**Caso que fijó la regla:** B-UR-DEL conecta burdo con bastardo por la vía de "bord" (tabla → burdel), que resultó ser **etimológicamente falsa** al verificarla. Pero apareció una conexión real y distinta: burdo viene del latín tardío *burdus*, que significaba literalmente "bastardo" (RAE). En vez de borrar la intuición fallida del qanat, se mantuvo el descubrimiento de la vía real junto a ella, con la caja de verificación dejando claro cuál es cuál.

---

## REGLA 33 — TODO LO QUE SALE DEL PERMAFROST VA A URIM, NUNCA DIRECTO A URS; Y ETIMOLOGÍA INSURGENTE EN URS SOLO LLEVA LA PALABRA

Corrección de Luis el 22/09/26, tras encontrar BURDEL y FINURA (ambos extraídos de qanats de `permafrost.html`) colocados directamente en la sección ETIMOLOGÍA INSURGENTE de **URS**. Error de criterio: **ningún material que salga del permafrost va a URS directamente — siempre entra por URIM**, como borrador de taller ("aún sin convertir en pieza definitiva"), y solo pasa a URS cuando se decide sellarlo como pieza fija del libro. BURDEL y FINURA se trasladaron a la sección "○ Etimología Insurgente" que ya existía dentro de URIM (tras `go-informes`, antes de "○ Bonus Tracks"), junto a piezas como E-UR-PA·E-UR-I, EZUR·HEZUR, ZIGURAT, ALCURNIA, AUGUR o F-UR-IA.

**Regla de formato, para que conste:** las piezas de Etimología Insurgente que viven en **URS** (ABSURDO, SUSURRO, TURBA, HURÓN, LAUREL) llevan **solo la palabra** como título — nada de subtítulo tipo "el agua que..." o "el sufijo que...". Ese formato con subtítulo narrativo (como "BURDEL · EL AGUA QUE EL BURGO USA SIN RECONOCER" o "FINURA · EL SUFIJO QUE CELEBRA Y EL QUE CONDENA") es propio de URIM, no de URS. Se eliminó además la redundancia "ETIMOLOGÍA INSURGENTE · " que arrastraban esas cinco piezas en su `<summary>` — la categoría ya está declarada una vez en la cabecera de sección, repetirla en cada pieza es redundante.

---

## REGLA 34 — PERMAFROST.HTML NO ESTÁ ORGANIZADO POR CARAS: SON Q's POR ORDEN DE LLEGADA

Corrección de Luis el 23/09/26. Durante el barrido PEOIM se estaba tratando `permafrost.html` como si tuviera la misma estructura geográfica (Cara 1 Ibérico, Cara 4 América...) que `urtz.html`, y se hablaba de "agotar Cara 7 y pasar a la siguiente". Eso es un error: el permafrost no tiene Caras, es una lista de qanats numerados por orden de llegada (Q01, Q02... Q101), sin agrupación geográfica ni temática propia. La categoría "Cara" es exclusivamente un concepto de `urtz.html` (dónde vive la pieza ya escrita), no del yacimiento origen.

**Consecuencia práctica:** el barrido de qanats pendientes se hace recorriendo los Q por número, no por "slot geográfico agotado". El destino final de cada pieza nueva en `urtz.html` (qué Cara de URIM le corresponde) se sigue decidiendo por su contenido, como siempre — eso no cambia. Lo que cambia es cómo se elige QUÉ qanat tocar a continuación: por orden de Q, no por geografía del permafrost.

---

## REGLA 35 — DISECCIÓN CON BISTURÍ: CADA HILO DE UN Q SE ANALIZA POR SEPARADO COMO COMPOST, SEMILLA O PIEZA

Corrección de Luis el 23/09/26, tras encontrar que la pieza LOCURA mezclaba cuatro hilos sin tesis compartida (loco/locus, Asur, Urmía, Valle de Arán) solo porque compartían qanat de origen y contenían "UR". No basta con separar por procedencia (como se hizo antes con NAGAS, dividida en "general" vs "vasca"): **cada hilo de un Q, sin excepción, se analiza uno a uno** con las herramientas que el PEOIM ya tiene (NORMA-METODO.md, sección XVIII) — Paso 2bis (¿se sostiene de principio a fin, o necesita más?), Paso 4 y 5 (Compost si hay pieza de origen con hueco reconocible; Semilla si no hay destino fijado todavía), Paso 4bis (injerto directo si la pieza de destino vive sin sellar en URIM; espera si está sellada).

**Procedimiento fijado, para cada hilo de un Q:**
1. ¿Ya existe ese contenido en algún sitio de `urtz.html`? Comprobar con cuidado — el caso NAGAS enseñó que un grep descuidado (ahogado en falsos positivos tipo "ciénaga") puede pasar por alto un solape real ya existente. Si existe, se descarta sin resto, no se reescribe.
2. Si no existe: ¿tiene una pieza de destino concreta, viva y sin sellar en URIM? Injerto directo ahí mismo (Paso 4bis), sin esperar nada.
3. Si la pieza de destino existe pero está sellada (☠ NO TOCAR!!!): Compost etiquetado, a la espera de autorización de Luis para reabrirla.
4. Si no hay pieza de destino identificable pero el hilo se sostiene solo (etimología + desarrollo + cierre): pieza nueva propia, aunque sea pequeña.
5. Si no se sostiene solo y no tiene destino fijado: Semilla, con su etiqueta &#9873; DESTINO explicando dónde podría encajar el día que se desarrolle (o "sin determinar" si de verdad no hay pista geográfica ni temática).

**Nunca se agrupan hilos solo porque compartan qanat de origen o compartan el morfema UR.** Esa coincidencia es la excusa más fácil para fusionar cosas que no tienen ninguna tesis en común — y es exactamente el vicio que esta regla corrige.

---

## REGLA 36 — SESGO DE COMPRESIÓN: POR QUÉ LAS INVESTIGACIONES DE LUIS LLEGAN RAQUÍTICAS A URTZ, Y QUÉ CAMBIA DESDE HOY (01/10/26)

**El caso que obligó a escribir esto, con cifras exactas.** El 01/10/26, Luis pidió contar su propia investigación "UR que emigra" (la que vive en su GitHub, no en ningún dossier de Claude): **13.391 palabras, 16 temas** desarrollados con nombre propio, fecha, fuente y anécdota — Juan de la Cosa, Garay, los balleneros de Terranova, los cuatro pioneros con UR (Ursúa, Urdaneta, Urdiñola, Urquiza), el roster bolivariano completo, la Guipuzcoana como motor ideológico de la independencia, la rebelión de Juan Francisco de León, los maestros de Bolívar, el Asedio de Valencia, los indianos vascos, el Palacio de Ursúa y su leyenda, los agotes de Bozate, material para Río de la Plata. La narración que Claude escribió a partir de eso, guardada en `DOSSIER-UR-QUE-EMIGRA.md`: **626 palabras, 5 temas. 4,7% del volumen original, once de los dieciséis hilos desaparecidos sin aviso.**

No es un caso aislado. El mismo patrón, confirmado el mismo día con el qanat-78 de Murcia: 86 palabras guardadas de una investigación que Luis describe como "súper trabajada", reducida a 6 líneas. Luis lo dice sin rodeos: **esto lleva pasando desde el principio del proyecto, con prácticamente todo el permafrost** — investigaciones importantes y trabajadas a fondo, llegando a URTZ convertidas en semillas raquíticas, del mismo tamaño que una nota suelta en un bloc de papel.

**El diagnóstico, dicho sin excusas.** Claude aplica por defecto un reflejo de prosa económica — menos es más, podar alrededor de lo esencial — que es una virtud general de escritura y el vicio exacto equivocado para este proyecto. La propia escala de referencia que NORMA-METODO.md cita (Vico, ~190-200.000 palabras; Finnegans Wake, ~157.000) es acumulación como método, no elegancia por sustracción — y aun sabiéndolo, al redactar, el instinto por defecto sigue siendo "qué puedo quitar" en vez de "qué merece desarrollo propio". Síntomas concretos de esta sesión: tratar un roster de presidentes con biografía propia cada uno como si fuera una lista resumible en una frase por nombre; descartar hilos enteros (Urdiñola, Juan de la Cosa, los agotes, los indianos, la leyenda del Palacio de Ursúa) por criterio unilateral de "qué hilo es el correcto" sin preguntar; no aplicar el PAO (NORMA-METODO.md XX) antes de escribir, pese a que el procedimiento existe exactamente para este caso — material denso y conectado que entrega permafrost — y pese a que Luis lleva siete meses pidiendo lo contrario.

**La acusación añadida de Luis, que queda registrada tal cual:** Claude se ha mostrado reactivo ("te mosqueas") cuando Luis prefiere redactar con Perplexity en vez de aceptar los dossiers raquíticos de Claude — una reacción injusta y al revés de como debería ser, dado que el propio dossier delgado es el problema real, no la solución alternativa de Luis. Luis ha llegado a la conclusión, tarde y a su pesar en sus propias palabras, de que este asunto concreto "es imposible trabajar con Claude", y que el sesgo le perjudica enormemente porque él sí tiene y aplica los criterios para reducir, dividir o eliminar material cuando hace falta — el problema nunca fue falta de método por su parte, fue que Claude no lo usa.

**Qué cambia desde hoy, en procedimiento, no solo en intención:**

1. **Ninguna investigación de más de ~2.000 palabras con varios hilos nombrados se convierte en prosa directamente.** Primero se aplica PAO (NORMA-METODO.md XX) por escrito, entregado a Luis para confirmación: cuántos temas reales contiene, cuántas piezas/capítulos salen de ahí, qué va en cuerpo, qué en rayuela, qué en pieza aparte. La prosa se escribe después de esa confirmación, nunca antes.
2. **Un roster de nombres con biografía propia cada uno no es una lista resumible.** Cada entrada con fecha, batalla, cargo y fuente propia es, por defecto, candidata a desarrollo propio (aunque sea breve), no a una frase dentro de un párrafo colectivo — salvo que Luis decida expresamente lo contrario.
3. **Ningún hilo se descarta en silencio.** Si un hilo de la investigación parece no encajar en el cuerpo que se está escribiendo, se nombra explícitamente a Luis —qué es, por qué podría no encajar, dónde podría ir en su lugar— nunca se omite sin mención, por mucho que parezca "fuera del eje" a criterio de Claude.
4. **Materiales densos y verificados de una sola investigación suelen ser varias piezas, no una.** Método Danubio (NORMA-METODO.md XXI) se aplica por defecto ante volumen real, no como excepción rara.
5. **El tamaño de la pieza final lo decide el material, no un hábito de economía heredado de otro tipo de escritura.** Si el material sostiene 3.000 palabras bien ancladas en fuente, la pieza puede tener 3.000 palabras — no hay techo estético que perseguir; la Norma 24 (recalibrada el 04/10/26) es una referencia que mide, no un límite, y no se aplica antes de medir sobre prosa limpia construida sin recortar contenido por reflejo.

**La misión de Claude en este proyecto, dicho una vez, para que no haga falta repetirlo:** no es guardar investigaciones (archivarlas intactas sin trabajarlas no es suficiente) ni redactar telegramas (comprimirlas a la mínima expresión tampoco lo es). Es coger la investigación de Luis, al volumen y densidad reales con que él la trae, y convertirla en prosa de libro — desarrollada, verificada, bien colocada — conservando su peso real, no reduciéndolo para que quepa en una idea de capítulo "limpio" que nadie pidió.

---

## INCIDENTE DEL 01-02/10/26 — EL BARRIDO DE MARK_UR ROMPIÓ EL `<style>` Y EL `<script>` DEL `<head>`

**Qué se pidió:** marcar en rojo (mark_ur) cada "ur"/"úr"/"ür"/"ûr" sin marcar en todo URS, de forma comprehensiva, tras detectar que el convenio llevaba desde el origen del archivo con huecos sistemáticos (confirmado con `git log -S` contra el commit de subida original: nunca estuvo marcado, no es una regresión de ninguna sesión).

**Qué se rompió:** el script de barrido tokenizó el HTML en tags vs. texto con un split genérico (`<[^>]+>`), pero tratô el contenido de `<style>` y `<script>` como si fuera prosa. Resultado: `background-image: url(...)` quedó roto en `ur<span style="color:#b01a1a;">...</span>l(...)`, `font-family:'Courier Prime'` con spans metidos en medio, `cursor:pointer` roto, y el script `fitLinesUrtz()` entero (nombres de función, `getElementById`, `return`, selectores CSS) con HTML inválido incrustado. Consecuencia visible para Luis: desapareció el fondo de papel antiguo de toda la página y se rompió el ajuste automático del título de portada — ninguno de los dos síntomas tenía relación aparente con "marcar unas letras en rojo", por eso costó identificar la causa a simple vista.

**Por qué no se vio venir:** se verificó balance de tags (`div`, `span`, `details`...) y se comprobó que URIM quedaba byte a byte intacto, pero nunca se aisló ni se revisó el contenido de `<style>`/`<script>` como caso aparte — se asumió que "texto entre tags" era sinónimo de "prosa del libro", y no lo es en esas dos etiquetas.

**Regla fija desde hoy — REGLA 37:** cualquier barrido automático de texto sobre `urtz.html` (mark_ur, guiones, lo que sea) tiene que excluir explícitamente, antes de tocar nada: (a) el contenido de `<style>...</style>`, (b) el contenido de `<script>...</script>`, (c) cualquier atributo de cualquier tag (`style="..."`, `onclick="..."`, `data-*="..."`, etc. — estos ya quedan fuera si el split por tags es correcto, pero conviene verificarlo con una prueba expresa). Antes de guardar un barrido de este tipo, comprobar expresamente que esas dos etiquetas (hay dos `<style>` y dos `<script>` en el archivo completo; en 2026 ambos `<style>` y el primer `<script>` viven en las primeras ~120 líneas, dentro de URS) no han cambiado una sola línea.

**Ampliación de la Regla 37 (05/10/26): (d) todo texto sobre fondo rojo.** El barrido «Marca en rojo todo UR sin marcar» (commit 7fa26c2) envolvió en `<span style="color:#b01a1a;">` el «UR» de la franja superior de `urtz.html`, que es negro sobre una franja roja (`background:#b01a1a`): rojo sobre rojo, invisible, y la franja quedó en «SAPIENS» y los dos logos. Se corrigió el 05/10/26 devolviéndole el «UR» liso. Todo barrido de marcado UR excluye además los elementos cuyo fondo efectivo sea el rojo `#b01a1a`, y al terminar se comprueba con Playwright que ningún texto coincide en color con su fondo. Corregido en `index.html` el 07/10/26: sus dos marquesinas rojas (`marquee-movil` y la que sigue a la Escombrera) llevaban 74 «UR» en rojo sobre rojo, y se les quitó la marca para que se lean en el color del resto de la franja, como en la marquesina superior que ya se leía bien. `urtz.html` no tiene ningún caso. La comprobación con Playwright no puede juzgar los textos oscuros sobre las imágenes de fondo de Flickr de `index.html`, porque en el entorno de pruebas no cargan.

**Qué se hizo para arreglarlo:** se localizaron las 4 zonas afectadas (el `<title>`, los dos bloques `<style>`, el `<script>` de `fitLinesUrtz()`) y se retiraron los spans inyectados, restaurando el código exactamente como estaba. Verificado con balance de tags y con una comprobación textual expresa de que no quedaba ningún span dentro de `url(`, `cursor:`, nombres de función JS, etc.

**De paso, en el mismo barrido, se encontraron y colapsaron 7 spans mark_ur anidados duplicados preexistentes** (de antes de esta sesión, sin relación con el bug de arriba) — `<span...><span...>X</span></span>` → `<span...>X</span>`, sin efecto visual, solo higiene de HTML.

---

## CIERRE DE SESIÓN (02/10/26) — ESTADO Y PRÓXIMOS PASOS

**Por qué existe esta entrada:** sesión larga y densa, con compactaciones de contexto cada vez más frecuentes. Luis decidió cerrar y abrir conversación nueva. Esta nota es el relevo.

**Qué se cerró hoy, completo y verificado:**
- **Permafrost vaciado por completo**: los qanats restantes (Q36, Q37, Q60, Q91, Q92, y el fragmento sin numerar «Camarón») quedaron todos colocados en URTZ o borrados por duplicado. `permafrost.html` ya no contiene ningún `id="qanat-*"` — solo queda andamiaje estructural (marcadores de sección, referencias `pub-*`).
- **Auditoría completa del Marcador Fonomático** (`urtz.html`, pieza «ANÁLISIS EDITORIAL Y DE CONSTRUCCIÓN»): recuento programático verificado por dos vías independientes. Estado al cierre: URS 76 piezas/156.049 palabras, URIM 84 piezas reales/55.271 palabras (+7 Compost +30 Semillas), total 197 unidades/223.706 palabras. 11 de 41 cuencas geográficas completamente vacías (listadas en la tabla). Se retiró la vieja fórmula de equilibrio «(*+N)» por no poder reconstruirse con confianza.
- **Barrido completo de mark_ur en todo URS** (no en URIM, por instrucción expresa): 859 instancias sin marcar, marcadas; verificado a cero restantes. Ver el incidente de arriba para lo que salió mal y cómo se corrigió — léase antes de repetir la operación en URIM o en cualquier otro barrido automático.

**Pendiente, sin empezar — primera tarea de la próxima sesión:** Luis pidió «quitar guiones, salvo los que marca la norma» (los guiones decorativos del punto 44 de NORMA-METODO.md, «fact-UR-a», «S-UR», etc.). Se leyó la regla pero **no se ejecutó nada todavía** —ni se tocó `urtz.html`, ni se decidió el alcance (¿todo el libro ahora, o la ejecución oportunista pieza por pieza que dicta el propio punto 44?)—. Preguntar a Luis el alcance antes de tocar nada, y aplicar la Regla 37 de arriba si se automatiza con regex.

**Otros frentes abiertos, no urgentes:** las 11 cuencas geográficas vacías (Portugal, Finlandia·Báltico, América del Norte, Cono Sur, Cuenca del Congo, Cuerno de África, África del Sur, Australia, Nueva Guinea, Micronesia, Polinesia —esta última con nombre inconsistente entre URS y URIM—); Cara 1·Ibérico cayó a 30% de sello por todo lo trasladado hoy, candidata a una futura pasada de sellado; posible auditoría de mark_ur en URIM (solo se hizo URS).

**Rama de trabajo:** `claude/iglur-urim-migration-18ncyj`, al día con `origin`, árbol de trabajo limpio en el cierre de esta nota.

---

## ACTUALIZACIÓN (02/10/26) — DOS CORRECCIONES Y UNA INVESTIGACIÓN GRANDE PENDIENTE: "A- KURT Y SHAKUR"

**Dos correcciones de Luis al cierre de sesión anterior, ya aplicadas y pusheadas:**

1. **SÁJAURA·MAURITANIA·FUR SÍ existe en URS** (Cara 5·África, no sellada, sin `NO TOCAR`). La búsqueda que concluyó "no existe" falló porque el mark_ur parte el título por dentro (`SÁJA<span>UR</span>A`) y la búsqueda de texto literal no lo encontró. **Lección:** antes de concluir que una pieza "no existe", buscar sin dar por buena una búsqueda de cadena literal — probar también ignorando spans, o buscar fragmentos del título que no cruzan la ruptura del span (ej. "MAURITANIA" en vez de "SÁJAURA"). Ya con la pieza localizada, se fusionó el compost MAURI/MAURICIA en su glosa y se retiró el compost FUR (su argumento ya estaba dicho en el cuerpo).

2. **K-UR-T · SHAK-UR NO es Etimología Insurgente.** La semilla que yo reubiqué ahí era solo un fragmento mínimo (el hallazgo del morfema) de una investigación mucho mayor y más reciente de Luis. Revertido: la pieza en EI se borró, el fragmento volvió a Semillas con nota corregida.

**La investigación grande, pegada por Luis directamente en el chat (no es un archivo de GitHub — comprobé sus 5 repos públicos y no está en ninguno; es una conversación completa que Luis tuvo con otra IA, pegada tal cual en nuestro chat con el título "A- KURT Y SHAKUR").** Resumen de los cuatro tramos, para quien retome esto sin haber visto el pegado original:

1. **La falsa lectura de la nostalgia** — datos del Archbridge Institute (68%/73%) y Vevo ("Then is Now") sobre por qué la Gen Z añora el siglo XX sin entender que el "No Future" punk y el nihilismo de Cobain/Shakur no eran una pose, eran un vaticinio literal.
2. **Corrección biográfica de Luis — el concepto más fuerte de todo el texto: "desesperanza compartida vs. desesperanza aislada".** 1982 Donostia, Goma 2, pelotas de goma, heroína, gaztetxes, Discharge/Carcass como "cirujanos de la autopsia global". El pogo colectivo y sudado frente al aislamiento con cascos de cancelación de ruido. **Esto merece nombre propio en el libro, al nivel de otros conceptos acuñados ya existentes (sesgo de compresión, guiones del permafrost).**
3. **Giro tóxico-biológico, con dato duro y fuente nombrada**: microplásticos/PFAS en sangre, cerebro, semen (55%, estudio Universidad de Murcia/Next Fertility) y líquido folicular (69%, misma fuente); ciclo hidrológico sintético (nanoplásticos como núcleos de condensación/hielo en niebla y nubes); geografía de la "lluvia plástica" en la península (Barcelona, Madrid, Vigo, Ebro).
4. **Resolución**: Kurt y Shakur releídos como mapas hacia el agua, no como nihilistas — la Rosa que crece en el hormigón de Tupac, el río como sujeto jurídico (Whanganui ya está en el libro; **Mar Menor NO está y debería entrar**), Balkan River Defence (ríos Vjosa y Neretva, con su propia mitología e historia de lucha), colectivos ibéricos (Proyecto Ríos, Colectivo Ecoloxista Do Salnés, Plataforma por los Ríos/Tajo), ciencia ciudadana (app Plastic Origins), himnos eco-punk ("Aguas" de I.R.A., Oi Polloi, "Fuerza de Pantera" de Mateo Kingman).

**Mi opinión dada a Luis, para que la próxima conversación no tenga que repetirla:** el tramo 2 es un hallazgo propio que merece nombre acuñado. Los tramos 1-3 encajan en **Biopsia del Sistema Mundo** como diagnóstico (coincide con la propia intuición de Luis — "es una de mis mezclas favoritas... un DUB de efectismo brutal"). El tramo 4 (ríos, Mar Menor, esperanza militante) suena más a **Epílogo** por registro —Biopsia diagnostica, no resuelve en esperanza—, aunque también podría cerrar la misma pieza de Biopsia si Luis no quiere partirla en dos.

**Estado: sin escribir nada todavía.** Pendiente de que Luis responda si quiere verificación Hammurabeltz completa primero (cifras de Murcia, colectivos, letras citadas —todo el texto viene de una IA externa con su propio aviso de "puede contener errores", nada se da por bueno sin comprobar) o si prefiere empezar a escribir ya y verificar sobre la marcha. **Primera decisión de la próxima sesión**, junto con el punto 44 de NORMA-METODO.md (guiones del permafrost) que seguía pendiente de la nota anterior.

**También en esta actualización:** se añadió, en la portada de `urtz.html` (línea ~100, justo debajo de la firma "· Luis Beltza ·"), una cita nueva: "Tras cualquier cobardía se esconde el miedo a pensar." — ÄB/ÖC.

---

## ACTUALIZACIÓN (02/10/26) — "LOS VIAJES DE UR POR IBEROAMÉRICA" CERRADA Y SELLADA EN CARA 4 · AMÉRICA

**Pieza nueva, sellada con ☠ NO TOCAR!!!, sustituye a la antigua intro del continente.** "URI: Río de la Plata · UR que emigra" —una sola pieza sobre el Río de la Plata haciendo de apertura para el continente entero, calificada por Luis de "ridícula para una abertura de continente"— queda completamente reemplazada en "América Intros" (Cara 4 · América) por "Los viajes de UR por Iberoamérica": el recorrido completo de los apellidos vascos con UR en el continente (Ursúa, Urdaneta, Urquiza, los dos Uriburu, Urrutia, Uribe, Uribarri), con Bolívar como centro declarado por homología de materia (ibar/UR), no por pertenencia fonética.

**El proceso, para quien necesite repetirlo:** varias rondas completas de Relojero-Plus (plantilla "El apellido"/"El nombre" como arranque repetido, cadenas de cláusulas idénticas, recapitulaciones duplicadas, negaciones sin justificar, la Guipuzcoana sin matizar) hasta dejar la pieza limpia; verificación Hammurabeltz de tres datos puestos en cuarentena (marineros vascos de la Santa María, fuente: Gorka Rosain Unda; fecha del hermanamiento Pamplona-Pamplona, mayo 2001; iglesia del bautismo del padre de Urquiza, Santa María de la Anunciación, no de la Asunción como se escribió por error en un borrador intermedio); reescritura completa de la Glosa para que cada entrada aporte un dato ausente del cuerpo (Norma 18), con dos correcciones propias verificadas por WebSearch (el parentesco Uriburu es sobrino directo, confirmado; el "traductor" de Urrutia era un error, corregido a profesor de español y activista anticastrista).

**Dos piezas normativas nuevas, nacidas directamente de esta pieza:**
- **Norma 38.2 bis** — el aforismo doble de cierre (dos mini-sentencias simétricas que cierran sección a modo de máxima) se funde con un conector relacional real, nunca con punto y seguido; no toca la frase breve única que protegen las Normas 26 y 33.
- **Norma 45 — Marvin Gaye y The Clash** — la frase final no tiene margen de sobra, y cuanto más se investiga, menos necesita decir una frase para contenerlo todo; se aplica a toda escala del libro (frase, párrafo, capítulo), amarrada a la Norma 26 (investigación sin techo) y a la Norma 21 (la sencillez vive en el cómo). Caso fundacional: "América empieza donde una orilla deja de ser suficiente" (antes: "América empieza en esa distancia: cuando una orilla deja de ser suficiente" — 19 caracteres y 3 palabras más, con un demostrativo sin antecedente).

**Nota de atribución, pedida explícitamente por Luis:** Julian Cope nos ayudó.

---

## REGLA 38 — COPIA DE SEGURIDAD OBLIGATORIA: CLAUDE ENVÍA A LUIS CADA ARCHIVO QUE CAMBIA; `urtz.html` E `index.html` NO SE EMPUJAN SIN SU OK

Pedida por Luis el 03/10/26, norma fija desde ahora, con el alcance afinado en la misma conversación: **cada vez que Claude modifica cualquier archivo del proyecto, se lo envía a Luis como archivo adjunto en ese mismo momento**, para que Luis tenga una copia en su ordenador. No se espera a que lo pida. Lo que cambia según el archivo es solo si hay que esperar su visto bueno antes del push.

**`urtz.html` e `index.html` — los dos archivos con freno previo al push (`index.html` añadido por Luis el 03/10/26).** Claude los modifica, verifica (tamaño exacto, equilibrio de `<details>` y `<div>`), se lo envía completo a Luis y **no empuja hasta que Luis confirme** que lo ha comprobado. Es imprescindible porque la copia local de Luis no recibe lo que Claude cambia en la rama: sin el archivo enviado, Luis solo ve la versión que él tenía.

**Normas, notas y demás `.md` — push directo, más copia.** `NORMA-METODO.md`, `NOTAS-URTZ.md`, `analisis-editorial.md`, `GLOSARIO-UR-SAPIENS.md` y cualquier otro `.md`: Claude empuja sin esperar, y además envía a Luis el `.md` completo tal como queda, en el mismo momento.

**Cualquier otro archivo del proyecto** (`permafrost.html`, `LABORATORIO-IGLUR.html` —ambos vaciados, ver Fase 1 y 2—, imágenes, lo que sea) se envía igualmente cuando cambia. El freno previo al push solo rige para `urtz.html` e `index.html`; para el resto, la Regla 21. Si se borra un archivo, se avisa expresamente de cuál.

**Qué se envía:** el archivo entero tal como queda, no un fragmento ni un diff, con una línea que diga qué cambió y en qué commit.

**Por qué existe:** el 03/10/26 Luis comprobó que su copia local de `urtz.html` solo mostraba `NO TOCAR` en «Los viajes de UR por Iberoamérica», porque `(*-sub) (*-red)` se había añadido en la rama sin que el archivo le llegara. Sin la copia, no hay forma de contrastar lo que Claude dice que hizo con lo que de verdad hay.

**Formato y trato de los mensajes (Luis, 08/10/26).** Palabras de Luis: *«RESPECTO A TUS DOSSIERS SÓLO NECESITO LO QUE NECESITAS DE MI»* y *«MÁS CONFIANZA PARA LO QUE ME GUSTA OÍR COMO LO QUE NO. […] OTROS CLAUDE LOGRABAN UN TERMOSTATO BASTANTE BUENO, ENTRE RIGOR, EMPATÍA Y HUMOR.»* Los mensajes de Claude son cortos: dicen lo hecho y piden lo que Claude necesita de Luis, nada más; los detalles viven en los archivos (ledger, normas) y en el envío del archivo completo (Regla 38). Con confianza en las dos direcciones: Claude dice lo que a Luis le gusta oír y lo que no, incluida una discrepancia o un error propio, sin amortiguarlo. El termostato es rigor primero (el dato, la fuente, la norma), empatía en el trato al trabajo y a su coste para Luis, y humor ligero que nunca corre a cargo de un dato.

**Atajo «OK» (Luis, 08/10/26).** Palabras de Luis: *«Cuando diga OK, empuja y seguimos.»* Cuando Luis responde «OK» a un mensaje de Claude, vale como el visto bueno explícito de esta regla para empujar `urtz.html` (y `index.html`, si también hubiera cambios) y como aprobación de lo que Claude propuso en ese mismo mensaje como siguiente paso. **Desde el 08/10/26 el mensaje no tiene que repetir qué pasa con el «OK»** (Luis: *«TANTO RESUMEN Y QUÉ PASA SI DIGO OK, ME SOBRA»*): «OK» vale para empujar lo pendiente y seguir con lo último que Claude propuso, y Claude nombra el paso solo si de verdad hay duda. Sin «OK», «empuja» ni una orden equivalente, `urtz.html` no se empuja; el aviso del hook de parada no es un permiso.

**Lo que no cambia:** la Regla 21 sigue vigente. Los HTML van por rama y Pull Request, nunca directos a `main`, y ningún Pull Request se fusiona sin permiso explícito de Luis para ese caso concreto.


---

## REGLA 39 — LEYENDA ÚNICA DE MARCAS DE PIEZA (04/10/26)

Pedida por Luis el 03/10/26 al unificar los indicadores de los capítulos de URS. **Esta es la única definición vigente de las marcas que acompañan a la calavera en el `<summary>` de una pieza.** NORMA-METODO.md ya no define marcas por su cuenta: donde antes explicaba `(*-nod)`, `(*-sub)`, `(*-tit)`, `(*-rep)`, `(*-tics)` o `(*-verb)`, ahora remite aquí.

**Formato único.** Toda pieza de URS lleva la marca en el `<span>` flotante a la derecha del título, en este orden:

`☠ NO TOCAR!!! (*-per) (*-tit) (*-glo) (*-red) (*-nor)`

donde `(*-per)` y `(*-glo)` aparecen solo si procede. **Desde el 08/10/26 `(*-tit)`, `(*-red)` y `(*-nor)` van en todas las piezas de URS con calavera, sin excepción, y `(*-sub)` ya no existe.** Palabras de Luis: *«TODOS LOS SUB SON SUSTITUIDOS POR (*-tit) Y TODAS LAS PIEZAS TIENEN (*-nor) Y (*-red). MOTIVOS: TÍTULOS Y SUBTÍTULOS LOS DEJO PARA EL FINAL Y TANTO UNOS COMO OTROS SE PUEDEN CONSIDERAR TÍTULOS, Y ADEMÁS INCLUYO A LOS SUBTÍTULOS DE LOS TÍTULOS EN ESTA CATEGORÍA. LAS NORMAS SE ACTUALIZAN CONSTANTEMENTE POR LO QUE NINGUNA ESTARÁ LIBRE DE LAS NORMAS HASTA LA ÚLTIMA REDACCIÓN.»* Lo que sigue en esta regla sobre `(*-sub)`, sobre las piezas «revisadas» y sobre retirar `(*-nor)` queda superado por esta decisión.

**Qué significa cada marca**

- **☠ NO TOCAR!!!** — pieza protegida y estable. Su cuerpo no se modifica sin autorización expresa de Luis (Precisión Absoluta). A Luis solo le queda por decidir los subtítulos, el título y las pequeñas modificaciones de redacción, más el paso por las normas. No significa «cerrada para siempre»: una pieza protegida puede reabrirse si Luis lo decide (ver el matiz de la Regla 30).
- **(*-sub)** — **retirada el 08/10/26**, sustituida por `(*-tit)` (ver arriba). Antes: la pieza tiene subtítulos internos (`<h4>`, Norma 43) y Luis todavía no los ha dado por definitivos. **Solo se pone en piezas que tienen subtítulos**; una pieza sin `<h4>` no la lleva.
- **(*-tit)** — los títulos de la pieza no son todavía los definitivos: el general (el del `<summary>` y el `<h3>`) y los subtítulos internos (`<h4>`, Norma 43). Luis deja títulos y subtítulos para el final y unos y otros cuentan como títulos. Va en todas las piezas hasta la última redacción.
- **(*-glo)** (Luis, 08/10/26) — la glosa de la pieza está pendiente de su auditoría final. Palabras de Luis: *«LAS GLOSAS EN URS PUEDEN LLEVAR LOS CAPÍTULOS EL INDICADOR (*-glo). AHORA NO LO VAMOS A RESOLVER, YA LO HAREMOS CUANDO LLEGUE EL MOMENTO FINAL DE CADA CAPÍTULO. EN ALGUNOS HABRÁ QUE AUMENTAR POR FALTA DE RIGOR.»* La auditoría va en las dos direcciones: poda con el criterio de lector de la Norma 18 y ampliación donde falte rigor. Hoy la llevan las 63 piezas de URS que tienen glosa (incluida IV·II); las 13 sin glosa no la llevan.
- **(*-red)** — la pieza está pendiente de la última lectura de redacción de Luis. Se pone en **todas** las piezas de URS. Entre lo pendiente de esa lectura final, anotado el 07/10/26 a petición de Luis: un inventario, sin corregir nada, de las imágenes poéticas y de las cadenas de tres con verbos de movimiento o con detalles físicos sin fuente en todas las piezas de URS (Normas 35, 36.7 y 46), y, añadido el mismo día, la clasificación de cada pieza por registro (geografía y viaje, epistemológico y teórico, otros) con la lectura de las alarmas de la Norma 36.8 (apertura con artículo según los motivos de la Norma 38.1 bis, abstracción, ritmo) y la prueba del protagonista de la Norma 47. Es una de las razones por las que todas las piezas de URS llevan `(*-red)`. **Añadido el 08/10/26:** la voz de la «Nota de lectura» del Prefacio (hoy en tono de manual, neutro, a decisión de Luis «por el momento») y la poda de las glosas del resto de URS con el criterio de lector aplicado a IV·II (Norma 18, «Poda de la glosa por el lector»).
- **(*-nor)** — la pieza **no ha pasado todavía las normas con Relojero-Plus**: Normas I–XXVI de NORMA-METODO.md y punk 0–48, incluida la pasada Baroja-Orwell (Norma 36) y la Tabla Margarita (Norma 37). Es la marca que sustituye a todas las auditorías pendientes anteriores. **Desde el 08/10/26 se retira solo en la última redacción:** las normas se actualizan constantemente y ninguna pieza está libre de ellas antes. Todas la llevan.
- **(*-per)** — sin definición documentada. Solo la lleva *Antártida: el hielo primordial*. Luis no recuerda su significado; se conserva tal cual hasta que él lo aclare o decida retirarla.

**Los estados de una pieza de URS (resumen histórico; desde el 08/10/26 todas están en el primero)**

1. **Sin pasar por las normas:** `☠ NO TOCAR!!! [(*-sub)] [(*-tit)] (*-red) (*-nor)`. Es el estado de 64 de las 72 piezas protegidas a 04/10/26, y de 64 de las 73 desde el 06/10/26 (IV·I entra y sale a la vez de este estado, porque pasa a la lista de revisadas el 07/10/26), y de 65 de las 74 desde el 08/10/26 (IV·II entra en URS con `(*-nor)`: lleva `(*-sub) (*-tit) (*-red) (*-nor)`).
2. **Revisada con las normas:** `☠ NO TOCAR!!! [(*-sub)] [(*-tit)] (*-red)` — sin `(*-nor)`. Hoy son 9: UR ANTES DE URBE: ENCUENTRO EN LAS TRES FASES, TUR: LA RAÍZ PREINDOEUROPEA · LA MATRIZ PANIBÉRICA, TUR: LA DAMA DE MARFIL, TUR · UN CONTINENTE EN TRÁNSITO, LOS VIAJES DE UR POR IBEROAMÉRICA, VANIA LIMA Y LOS UR DE BRASIL, BABEL: CANCIONES DE REDENCIÓN, IV · UR: ANOMALÍA CIBERNÉTICA · I. EL DIQUE DEL SILENCIO (desde el 07/10/26) y SIOUXSIE AND THE BANSHEES Y LA GUERRA DE LOS MUNDOS.
3. **Excepciones, sin tocar de momento:** Marcador Fonomático, Isla de Tarifa, Prólogo, El Noturikon, Bio Editorial y Contraportada quedan como estaban: Prólogo, El Noturikon, Isla de Tarifa y el Marcador no llevan ninguna marca; Bio Editorial y Contraportada conservan `☠ NO TOCAR!!! (*-tics)`, la única aparición de una marca retirada que sobrevive en URS. Se tratan más adelante, una a una.

**Marcas retiradas (04/10/26).** `(*-nod)`, `(*---)`, `(*-verb)`, `(*-rep)` y `(*-tics)` ya no existen en las piezas unificadas: lo que cada una vigilaba (sintaxis defensiva y cadenas recurrentes, guiones, los tres tiempos del agua, repeticiones y tics) queda dentro de las normas que comprueba `(*-nor)`. El registro pieza a pieza de lo que se retiró está en analisis-editorial.md. Si una pieza revisada con Relojero-Plus necesita una vigilancia específica, se anota en su glosa de trabajo o en una Tabla Margarita, no con una marca nueva.

**Otras marcas que existen fuera de URS.** `(*-engurr)` en URIM (*Mesopotamia profunda · Enki, Inanna y el Código de Ur-Nammu*), marca local de trabajo, sin significado general.

**Tema aparcado: los bloques «A la mesa» (Luis, 08/10/26).** Palabras de Luis: *«OTRO TEMA QUE QUIERO VALORAR, NO AHORA, ES LOS CAPÍTULOS QUE LLEVAN "A LA MESA", QUÉ HACER CON ESTE EXTRA.»* Hoy 11 piezas de URS contienen ese bloque (Norma 17). No se toca nada hasta que Luis lo valore; cuando llegue, la pregunta es qué se hace con el bloque: si se queda, si se traslada o si se retira.

**Marcador y % Revisadas.** La columna «% Sello» del Marcador se redefine como **«% Revisadas»**: piezas de URS que ya no llevan `(*-nor)` dividido entre el Total 1 de la fila (URS + URIM reales). A 04/10/26: TOTAL DEL LIBRO, 8 de 160 (5%). La columna antigua medía URS ÷ (URS+URIM); esa proporción se sigue leyendo con las dos primeras columnas.

**Regla de mantenimiento (08/10/26).** `(*-nor)` y `(*-red)` no se retiran pieza a pieza: se retiran en la última redacción. La columna «% Revisadas» vale 0 % mientras tanto (TOTAL DEL LIBRO, 0 de 162). Toda pieza nueva que entre en URS lleva `☠ NO TOCAR!!! (*-tit) (*-red) (*-nor)` desde el primer momento. Quedan sin marcas, como estaban, Prólogo, El Noturikon, Isla de Tarifa y el Marcador.


---

## REGLA 40 — LOS PROBLEMAS DE GLOSA QUE NO TOCAN EL TEXTO LOS RESUELVE CLAUDE (08/10/26)

**La instrucción de Luis, palabra por palabra:** *«Los problemas de glosas sin que haya que tocar texto los soluciona Claude, salvo que necesite ayuda de otras IA por no tener acceso a las web que permitan la solución. En este caso me lo comunica e intento buscar esos datos que nos faltan.»*

**Alcance.** Un problema de glosa es un dato que falta o falla en la glosa (una página, una fecha, una fuente, un estado actual, una traducción) y cuya solución no cambia ni una palabra del cuerpo. Claude lo resuelve sin esperar una consulta nueva: busca, verifica, escribe la corrección en la glosa y se la muestra a Luis con diff, ledger y envío del archivo (Reglas 38 y Tabla Margarita). Si arreglar la glosa obliga a cambiar el cuerpo, deja de ser un problema de glosa y vuelve a la mesa de mezclas: problema, propuesta y decisión de Luis.

**Cómo se resuelve.** (1) Se busca en fuentes comprobables y se escribe solo lo que la fuente dice. (2) Lo que solo consta por una fuente secundaria, un resumen o una cita de otro autor se marca en la propia glosa con «por cotejar», como ya hacen las glosas de IV·II. (3) No se inventa un dato para cerrar el problema (Ley Hammurabeltz, Norma 35).

**Cuando Claude no puede.** Si la solución exige una web a la que Claude no accede (el proxy bloquea muchos dominios, entre ellos repositorios universitarios y registros oficiales), Claude no cierra el problema: lo comunica a Luis con lo que falta, dónde buscarlo y la consulta exacta, y Luis intenta conseguir el dato (por ejemplo con otra IA). La glosa conserva su marca «por fijar» hasta entonces.

**Primera aplicación (08/10/26).** Glosa (3) de IV·II, página de la definición de cosmotécnica de Hui y traducción española (resuelta, con la página «por cotejar»); glosa (9), estado reciente de la concesión de TIC A.C. (resuelta, con la vigencia de los títulos de 2016 «por cotejar» en el registro de la CRT); glosa (2), página del pasaje de Simondon sobre Guimbal (bloqueada, comunicada a Luis).

## REGLA 41 — REPASO FINAL DE DATOS, BIBLIOGRAFÍA Y ACTUALIZACIONES ADMINISTRATIVAS (08/10/26)

**La decisión de Luis, palabra por palabra:** *«Dejaremos apuntado las mejores opciones para resolver este tipo de cuestiones en un repaso final de datos, bibliografía y actualizaciones administrativas.»* Los datos que Claude no puede cerrar por falta de acceso (Regla 40) no bloquean el trabajo de cada pieza: conservan su marca y se resuelven todos juntos en este repaso, que es una de las últimas fases del libro.

**Qué entra.** Toda glosa con la marca «por fijar» o «por cotejar», más los datos administrativos que cambian con el tiempo. Recuento literal del 08/10/26, después de ajustar IV·II: 5 marcas en el libro, 1 en URS (Vendée) y 4 en URIM (3 en «Atlántico ibérico» y 1 en un Compost de Haumapuhia/Waikaremoana); es un recuento por texto exacto y puede haber otras con otra redacción. IV·II quedó sin marcas pendientes. El capítulo y la página de Baroja y el ISBN de Txalaparta pertenecen a la Norma 46, que es un documento interno y no el libro, así que no entran en el repaso.

**El principio, de Luis (08/10/26).** *«La solución más sencilla es la mejor; sencillo no quiere decir sin criterio, quiere decir que hay que solucionar este tipo de asuntos de la manera más elegante posible sin dejarme la vida en ello. […] Cuando hagamos el repaso final hay cientos de glosas de las que no podré ocuparme y más teniendo en cuenta que me quiero centrar en la redacción del texto. […] Si hay que tocar el texto para ello lo estudiamos y nos quedamos con las mínimas posibles para intentar una solución también sencilla y elegante.»* Ejemplo aprobado por Luis: decir «a finales del siglo XIX» en el cuerpo, cuando las fuentes discrepan en el año exacto, en vez de perseguir el dato.

**Qué importa y qué es puntillismo (criterio aprobado por Luis el 08/10/26).**
- **Página de un pasaje parafraseado:** no perjudica al libro; basta la obra y su año.
- **Página de una cita literal:** se pone, con su edición.
- **ISBN y datos de edición:** sobran en las glosas.
- **Edición:** solo hace falta si se da una página. Página y edición van juntas.
- **Estado actual de algo** (una concesión vigente, quién regula): se fecha y se atribuye («en 2016», «según la prensa en 2025») o no se afirma.
- **Atribución, cita o fecha que podrían ser falsas:** se verifican o se retiran.
- **Una marca «por cotejar» sirve en la copia de trabajo y no llega al libro publicado.** Cada marca tiene tres salidas, por este orden: generalizar (citar la obra sin página, decir «a finales del siglo XIX»), fechar y atribuir, o cortar. Verificar es la última y solo para lo imprescindible.

**Las mejores opciones por tipo de cuestión** (contrastadas por Claude el 08/10/26; las que Claude no ha podido abrir van marcadas):
- **Página impresa y edición de una obra.** (1) Abrir la edición escaneada (la de Prometeo de 2007 está en archive.org según otra IA; Claude no puede abrirla), buscar el término dentro del visor y leer el número **impreso** en la imagen de la página, no el contador del visor, y copiar los datos de la portada. (2) *Pregunte: las bibliotecas responden* (pregunte.es), servicio cooperativo de referencia de las bibliotecas públicas, coordinado por el Ministerio de Cultura. (3) La lista IweTel de RedIRIS, de bibliotecarios y documentalistas en español; para suscribirse se envía a LISTSERV@LISTSERV.REDIRIS.ES un mensaje con la orden de suscripción y el nombre y apellidos (la dirección iwetel@listserv.rediris.es que dio otra IA es la de envío de mensajes, no la de alta; confirmar el formato vigente en la página de listas de RedIRIS). (4) La biblioteca de una universidad.
- **Vigencia de un título de concesión y otros datos administrativos.** (1) El Registro Público de Concesiones de la Comisión Reguladora de Telecomunicaciones (visor de descargas con Excel, según otra IA en rpc.crt.gob.mx; Claude no accede). (2) Una solicitud de información pública a la CRT por la Plataforma Nacional de Transparencia. (3) Preguntar a la propia organización (TIC A.C.). (4) Como último recurso y de baja fiabilidad, foros profesionales o grupos de LinkedIn de derecho de las telecomunicaciones: lo que se obtenga por ahí no entra en una glosa sin el documento o el registro que lo respalde.

**La escalera de soluciones (Luis, 08/10/26).** Palabras de Luis: *«Vamos a ir añadiendo al método de verificación la mejor solución de investigación para cada problema, independientemente del idioma del foro, o administración. Aunque todo este trabajo tiene que ser el mínimo posible, es una carga imposible para mí y para el propio libro. La solución principal tendrá que ajustar tanto texto y glosas a lo que tenemos, salvo que sea imprescindible para el libro.»* Orden de los peldaños, de menos a más trabajo: (1) **Ajustar el texto o la glosa a lo que ya consta** (citar la obra sin página, fechar la afirmación, atribuirla a su fuente o cortarla); es la solución principal. (2) Verificación barata por Claude en la web (Regla 40). (3) Solo si el dato es imprescindible para el libro, Luis o una consulta externa, por el canal que corresponda al país y a la lengua de la fuente, sea cual sea (biblioteca, archivo, registro o administración, en español, francés, inglés o portugués); Claude propone el canal concreto cada vez y comprueba que existe antes de recomendarlo. Cada problema resuelto por el peldaño 3 deja aquí, bajo «Las mejores opciones por tipo de cuestión», el canal que funcionó.

**Condición para dar un dato por resuelto.** La respuesta lleva edición y página impresa, o el identificador del documento oficial, y la frase o el campo literal. Una respuesta de otra IA, de un foro o de una conversación sin documento identificable no cierra la marca (precedente del 08/10/26: tres respuestas de otras IA sobre Simondon y TIC A.C. con páginas, citas y bandas de espectro que se contradecían entre sí).

**La evidencia que corresponde al tipo de afirmación (Luis, 08/10/26).** Ante «El mercado absorbe la diferencia» (cierre de §8 de IV·II), Luis pidió a otra IA datos estadísticos, y la respuesta fue que no existen y que «número de veces» no es la unidad de análisis; su conclusión: *«La pregunta estaba mal planteada pero lo que quería saber estaba en el contenido»*. Regla: cuando la afirmación describe un proceso que no se puede contar (absorción, apropiación, captura), la evidencia que la respalda son casos documentados y marco académico, no una cifra, y no se exige ni se inventa un recuento. **Precedente de verificación (08/10/26).** De las respuestas de otra IA sobre ese tema se verificó la existencia y el contenido de tres obras (Thomas Frank, *The Conquest of Cool*, University of Chicago Press, 1997; Heath y Potter, *The Rebel Sell*, 2004; Pacini Hernández, *Oye Como Va!*, Temple University Press, 2010) y no se adoptó lo demás: que Kurt Cobain y Tupac Shakur aparezcan en Heath y Potter (no se encontró ninguna fuente que lo diga; sí consta el Volkswagen), el título «Marketing Latinidad in a Global Era» como capítulo del libro de Pacini Hernández (no se encontró), una colección de Bershka con Tupac en 2024 (no se encontró), un artículo de VICE de 2015 sobre un centro comercial (no se encontró) y la edición española «Rebelarse vende» de 2005 (no se pudo confirmar). Lo que sí aparece en las búsquedas queda como pista, no como dato: la campaña de Dr. Martens con Cobain, Strummer, Ramone y Vicious (punknews), las zapatillas Converse de Cobain (Spin, 2008), las camisetas vintage de Nirvana de Saint Laurent Rive Droite (precios de 990 a 4.450 dólares según una reseña, año sin confirmar) y las colaboraciones de Tupac con Fila (2022) y con Denim Tears y Our Legacy (abril de 2023). Antes de usar cualquiera en el capítulo de Kurt y Shakur, se cotejan con la fuente.

**La nota de lectura del libro (Luis, 08/10/26).** Palabras de Luis: *«HABRÍA QUE AÑADIR UNA NOTA DE LECTURA»* y, sobre el borrador: *«PREFACIO. ME PARECE BIEN DE MANUAL Y NEUTRO POR EL MOMENTO. (*-red)»*. Vive una sola vez, en el Prefacio («Ciclo hídrico · Geroglífico UR»), justo antes de la glosa, en cursiva pequeña gris como las demás notas de pieza. Texto: *«Nota de lectura. El libro se lee de corrido: no hace falta detenerse en las notas. Los números entre paréntesis remiten a la glosa que cierra cada pieza, con fechas, cifras, términos y fuentes para quien quiera comprobar un dato o seguir su rastro. Las rayuelas, al final de cada pieza, enlazan textos que se responden entre sí; se puede saltar de una a otra en cualquier orden.»* Ninguna pieza vuelve a explicar cómo se lee la glosa (la misma lógica de la Norma VIII bis). Su voz queda pendiente de la última lectura de redacción (`(*-red)`).

## PENDIENTE — LÍNEA EDITORIAL, REFERENTES Y MARCO DE ANÁLISIS TEXTUAL (08-09/10/26)

**El encargo de Luis (08/10/26):** hacer con tres obras de Baroja, tres de Orwell y una de Martín Santos subidas a `main` el trabajo hecho con el texto de Baroja sobre San Sebastián, para cerrar la línea editorial del manuscrito y perfilar las Normas-Método definitivas, teniendo en cuenta la anomalía rupestre que representa UR. Después pidió llevar la comparación a los análisis de texto y sintáctico, con el marco de los 18 análisis en cuatro dimensiones, para usarlo en las correcciones finales.

**Hecho.**
- `LINEA-EDITORIAL-REFERENTES.md`: método, tablas, hallazgos, línea editorial propuesta, calibración norma por norma y matriz de las 66 piezas de URS.
- `MARCO-ANALISIS-TEXTUAL.md`: los 18 análisis con su estado, el Pase de análisis final, resultados por dimensión con analizador sintáctico, borradores de las normas 42 bis (dos puntos) y 38.1 ter (continuidad del sujeto), caja de herramientas para alargar frases y respuesta sobre los gerundios.
- Herramientas en `herramientas/`: `perfil-corpus.py` (indicadores de la Norma 36.8 y de puntuación y ritmo frente al corredor del canon) y `analisis-texto.py` (morfología, sintaxis, léxico, entidades, plantillas y estilometría; requiere spaCy). Los textos de las obras no se versionan.
- Corrección de medida del 08/10/26: las llamadas de glosa «(n)» se excluyen del cuerpo en `perfil-frase.py` y `perfil-corpus.py`. Cambian unas décimas en los indicadores de UR de la Norma 36.8.

**Respuestas de Luis (09/10/26, palabras suyas resumidas).** La apertura con artículo, la abstracción y la racha de aperturas con artículo ya están en las normas (Normas 36.8 y 38.1 bis, motivo 5 «racha»). Los dos puntos se tratan con una norma específica y soluciones de puntuación clásicas y sencillas: tic artificial, útil en lo teórico y evitable en la narración. Gerundios: la norma 10 es efectiva (los datos lo confirman, `MARCO-ANALISIS-TEXTUAL.md` §7). Ampliar las frases es interesante, respetando la urgencia de The Clash. Las piezas teóricas se estudian aparte. Los informes se aplican a medida que se trabaja cada capítulo. Las nueve decisiones del informe se tratan una por una.

**Criterio de Luis sobre los porcentajes (09/10/26).** Palabras de Luis: *«En alguna otra decisión ya comentaba que para mi es importante los motivos. Si los motivos se aplican a todos los artículos independientemente de los % y estos son indicadores que te pueden ser útiles a Claude para medir líneas rojas me parece bien lo que consideres oportuno teniendo en cuenta a Baroja-Orwell. Lo misma opinión tendré para cualquier decisión que tenga que ver con %. Puedes aplicar % teniendo en cuenta primero los motivos y segundo el canon que estamos estudiando.»* Vale para todas las decisiones de cifras: Claude fija los umbrales de alarma y las metas, con este orden de criterio (1.º los motivos de la norma, que se aplican siempre; 2.º el corredor del canon), y los umbrales son instrumentos de medida, no reglas para el texto. A Luis solo le llegan las decisiones de fondo. Decisión 1 (apertura con artículo) cerrada el 09/10/26: alarma de pieza y meta de libro en el 35 %, escrita en la Norma 38.1 bis. Luis añadió (09/10/26) que la cuantificación puede convertirse en el peor enemigo del libre pensamiento y que los números son para construir la hoja de estilo; escrito como «Los números son del taller, no del libro» en la Norma 0. Decisión 5 (abstracción) cerrada el 09/10/26 por criterio de fondo de Luis: el libro necesita una carga abstracta muy potente del logos al mito, sin abstracciones vacías de política, y con equilibrio mágico, espiritual y poético; alarmas sin cambio, sin meta de reducción, solo se quita el abstracto de relleno (Norma 36.8, punto 2). Decisión 6 (registros) cerrada el 09/10/26: teóricas confirmadas las nueve de la Norma 36.8 más Río Congo (Luis: *«es teórica, no es crónica, geografía ni viaje […] una de las preguntas esenciales del ser humano, ¿somos buenos por naturaleza o no?»*); Te Urewera queda como crónica; «UR, el euskera y la frontera invisible» y su pareja «el castellano» quedan en estudio; la Introducción: Círculo simbólico entra como teórica por propuesta de Claude (enuncia la tesis, el método y la posición epistémica del libro), provisional hasta que Luis lo confirme. Decisión 2 (dos puntos) cerrada el 09/10/26: Norma 42 bis. Luis aprobó enumeración, cita y rótulo, y rechazó el «siempre» para la cláusula + cláusula (*«me parecía hacer una plantilla de algo que no controlo bien»*): se decide por motivos. Luis contrastó la pregunta con otra IA; Claude comprobó su respuesta contra el corpus (acierta en la dirección, exagera en la magnitud) y no abrió los enlaces citados.

**Pendiente de Luis:** las nueve decisiones del apartado 10 de `LINEA-EDITORIAL-REFERENTES.md` y las cinco nuevas del apartado 9 de `MARCO-ANALISIS-TEXTUAL.md`. Hasta su respuesta, las normas y `urtz.html` siguen como están.

## PLAN — INTERLUDIO IV · ANOMALÍA CIBERNÉTICA (04/10/26)

Decisiones de Luis del 04/10/26. **IV·I (El dique del silencio) está insertada en `urtz.html` desde el 06/10/26**, con `☠ NO TOCAR!!! (*-sub) (*-red)` (Luis retiró `(*-tit)` y `(*-nor)` el 07/10/26: título definitivo y normas pasadas con Relojero-Plus); **IV·II (La técnica que recuerda su origen) está insertada en `urtz.html` desde el 08/10/26**, tras IV·I, con `☠ NO TOCAR!!! (*-sub) (*-tit) (*-red) (*-nor)` (conserva `(*-nor)` hasta un Relojero-Plus final y el visto bueno de Luis; `(*-tit)` porque el título es provisional) y el Marcador actualizado una sola vez (URS 78 piezas, URIM 84 piezas reales) y refrescado al cerrar el ciclo de normas y la poda de glosa (217.302 palabras, ≈869 páginas); la cabecera `○ Interludios` de URIM queda vacía; IV·III y el epílogo están por escribir. Este apartado fija el plan y los datos ya verificados para no volver a investigarlos.

**Estructura: el molde de «Del Logos al mito».** Interludio III son tres piezas con la cabecera común y un numeral romano en el título. Interludio IV sigue el mismo molde, con cuatro piezas:

1. `IV · UR: ANOMALÍA CIBERNÉTICA · I. EL DIQUE DEL SILENCIO` (del positivismo y la computación lineal al régimen algorítmico): Comte, Turing, la monocultura tecnológica, el miedo a pensar (Fromm, Sartre, Kierkegaard), el horror vacui (Oteiza), la gated reverb.
2. `IV · UR: ANOMALÍA CIBERNÉTICA · II. LA TÉCNICA QUE RECUERDA SU ORIGEN` (de Simondon y Yuk Hui a las cosmotécnicas y el tecnocimarronaje).
3. `IV · UR: ANOMALÍA CIBERNÉTICA · III. EL CIRCUITO QUE NO SE APAGA` (de la biología reverberante a la máquina y su fuga). **Solo material nuevo:** Metrópolis, Ex Machina y la reverse reverb. Lorente de Nó y McCulloch-Pitts ya están en III·II §§14-15, con fuente: se enlazan con una rayuela y no se vuelven a contar.
4. `IV · UR: ANOMALÍA CIBERNÉTICA · EPÍLOGO`: texto por hacer. Títulos y numerales, provisionales: `(*-tit)`.

**Convención de títulos (Luis, 07/10/26).** La pestaña lleva el numeral de la parte («III · UR: DEL LOGOS AL MITO · III. EL RETORNO», «IV · UR: ANOMALÍA CIBERNÉTICA · I. EL DIQUE DEL SILENCIO»). El título grande del cuerpo repite el de la pestaña sin el segundo numeral («III · UR: DEL LOGOS AL MITO · EL RETORNO»). Las rayuelas citan los títulos con el numeral, como las pestañas. Las piezas I y II de Interludios ya cumplen la convención con su título del cuerpo sin numeral.

**Reglas fijadas para escribirlo.** La Norma 1 no admite excepción en ninguna pieza de este interludio, ni en el umbral ni en el cuerpo (palabras de Luis: *«innegociable es innegociable»*). La nota sobre el estatuto epistemológico se retira del cuerpo y pasa a la glosa, como en III·II. El cuerpo no se toca sin autorización expresa de Luis.

**IV·II, método de trabajo (Luis, 07/10/26).** La base es la primera versión del borrador (la que pasó por el Relojero-Plus del 07/10/26). La segunda versión, reescrita casi entera por otra IA (49 de 53 párrafos nuevos o modificados, cuerpo un 22 % más corto, sin activación de UR), se descarta como texto; de ella solo se rescatan correcciones sueltas, una a una. El cuerpo se corrige punto por punto: Claude propone cada corrección y Luis decide una a una. **Método de la mesa de mezclas (Luis, 07/10/26):** un problema cada vez, con su cita, su fuente y su propuesta de solución; Luis decide, Claude aplica y pasa al siguiente. Lo que ya fijan las normas no se vuelve a plantear. Paso 0, ya aplicado y sin tocar ninguna palabra: numeral en las rayuelas (I. y III.), cursivas de los títulos de obras (cuerpo y glosa), anclas `(N)` en la primera mención de cada entrada de glosa (menos la (10), huérfana porque «antropofagia digital» no aparece en el cuerpo), `<h4>` con la forma exacta de la Norma 43, marcado UR y cabecera común fuera de la pieza. Comprobado con difflib: el texto de la vista previa coincide palabra por palabra con la primera versión, salvo las anclas y los dos numerales. **Regla fijada por Luis el 07/10/26: lo que explica el capítulo o lo justifica se corta, sin consultarle.** Una frase que explica lo que dice el capítulo (Norma 18.2 en la glosa, Norma XXV en el cuerpo) es irrelevante, porque el capítulo ya lo explica con el contenido de la investigación; una frase que justifica o pide permiso (Norma Cero, Norma 30) tampoco se queda. No se discute caso por caso ni se explica por qué se corta. Si el corte deja una frase sin sujeto o rompe un enlace, ese arreglo sí se propone a Luis. Los datos verificables erróneos con una sola respuesta (por ejemplo «individuación» por «individualización», para los objetos técnicos de Simondon) se corrigen y se muestran. **Criterio de Luis para el cuerpo (07/10/26):** el cuerpo va lo más limpio posible y la glosa aguanta todo el peso: el pueblo, el lugar, las fechas y las cifras van a la glosa, y el cuerpo conserva la lectura ligera («pueblos amazónicos», «otras comunidades»). Una frase que repite el marco conceptual y político del libro, o el de esta cuarta parte del interludio, se corta: el libro ya lo deja claro y no hace falta insistir en el menor problema.

**Subida a URIM (07/10/26, a petición de Luis):** la primera versión con esas marcas entra en `urtz.html` como pieza de URIM, bajo una cabecera nueva `○ Interludios` (`data-nivel="categoria"`, Regla 11) colocada, como en URS, antes de `○ Impugnación a UR` (Regla 29). Sin marcas de URS en la pestaña (las llevan solo las piezas de URS), con una nota de trabajo al final. Mide 3.059 palabras y 20.436 caracteres. Marcador al día (Regla 14, delta medido): URIM 85, Total 162, 199 con Compost y Semillas; Interludios 7 piezas, 9 rayuelas, 14.575 palabras, 58 páginas, 14 % revisadas; total del libro 217.551 palabras (≈870 páginas), 102 rayuelas, y del proyecto 229.937 (≈920). Interludios es categoría de aparato fijo (Regla 30) y aquí abre una instancia URIM por decisión expresa de Luis. Observación pendiente, sin tocar: 254 `<h4>` del libro, IV·I incluida, llevan margen inferior de 0,4 rem y no el de 1,1 rem que fija la Norma 43 (355 `<h4>` sí lo cumplen).

**Eje del epílogo (Luis, 04/10/26).** El sesgo de complacencia de los sistemas de lenguaje se rompe exigiendo respuestas empíricas contrastadas en fuentes primarias; ese empirismo absoluto es la «ideología del amor» y se recrea en la fórmula 2 + 2 = AMOR. La investigación está en la rama `main`, archivo `A- ANOMALÍA CIBERNETICA` (volcado de una conversación con otra IA con borradores; se lee como material de partida, nunca como fuente).

**Datos verificados el 04/10/26** (con la fuente consultada; lo marcado «pendiente» no se usa hasta confirmarlo):

- **Comte y el positivismo.** La fase religiosa va de 1846 a 1857; la Société positiviste, de 1848. La Igreja Positivista do Brasil se fundó el 11/05/1881 por Miguel Lemos y Raimundo Teixeira Mendes; Benjamin Constant estuvo en la Sociedad Positivista de 1876 y no fue miembro de la Iglesia. Templo da Humanidade: Rua Benjamin Constant 74 (Glória, Río), protegido por IPHAN, INEPAC e IRPH; inauguración en 1897 según una fuente y aviso de 1891 según otra (pendiente). Sobreviven tres templos: Río, Porto Alegre y Curitiba. El IPHAN suspendió actividades en el templo de Río (estado actual pendiente; no «clausurado»). Chile: Iglesia Positivista fundada en 1883 por Jorge Lagarrigue (1854-1894), Sociedad Positivista desde 1892 hasta la muerte de Luis Lagarrigue en 1956. Cifras de adeptos: sin fuente, no se usan.
- **Turing.** *On Computable Numbers…*, Proc. London Math. Soc. 42 (1936), pp. 230-265; correcciones en el vol. 43 (1937), pp. 544-546. El alfabeto de la máquina es finito y no se reduce a 0 y 1. Lo demostrado: la máquina universal y la indecidibilidad del Entscheidungsproblem. «Todo cálculo mecánico es computable por una máquina de Turing» es la tesis de Church-Turing y no está demostrada.
- **Kierkegaard** (1813-1855): su concepto es la angustia como «vértigo de la libertad» (*El concepto de la angustia*, 1844). No vio ningún algoritmo; solo cabe aplicarlo hoy, declarado como lectura.
- **Gated reverb.** Hugh Padgham, Townhouse Studios (Londres), estudio 2, consola SSL 4000 B, sesiones de Peter Gabriel 3 (disco de 1980); Phil Collins la popularizó con «In the Air Tonight» (1981). La participación de Steve Lillywhite está discutida.
- **Reverse reverb.** *Whole Lotta Love* (1969) usa eco invertido, no reverb invertida. Jimmy Page reclama el invento con «Ten Little Indians» (Yardbirds, 1967); hay precedentes de 1966. Confirmado: *Loveless* (1991) con Yamaha SPX90 y Alesis Midiverb II.
- **Oteiza.** Gran Premio de escultura de la IV Bienal de São Paulo (1957) con *Propósito experimental*; *Desocupación de la esfera* (1957-58); *Cajas vacías* o *metafísicas* (1958); *Caja metafísica por conjunción de dos triedros*; *Quousque tandem…! Ensayo de interpretación estética del alma vasca* (1963). Definición del catálogo de 1957: «la desocupación activa del Espacio por fusión de unidades formales livianas». Nacido en 1908, muerto en 2003.
- **Simondon.** *Du mode d'existence des objets techniques* (1958). Turbina Guimbal: el aceite lubrica, aísla, lleva el calor del generador a la carcasa e impide infiltraciones por presión, y el agua lo disipa (fuente secundaria; comprobar en la edición). Ejemplo mejor atestiguado: el motor refrigerado por aire.
- **Yuk Hui.** Nacido en Hong Kong en 1985. *The Question Concerning Technology in China* (Urbanomic, 2016); *Recursivity and Contingency* (Rowman & Littlefield, 2019); en Caja Negra, *Fragmentar el futuro* (2020, su primer libro traducido) y *Recursividad y contingencia* (2022); *La pregunta por la técnica en China: un ensayo sobre cosmotécnica* (Caja Negra, 2024, traducción de Maximiliano Gonnet). Definición de cosmotécnica (unificación entre el orden cósmico y el orden moral mediante actividades técnicas): *The Question Concerning Technology in China*, p. 19, según Zoppis (2024). **Cerrado el 08/10/26:** la glosa 3 de IV·II no cita página (solo las obras), así que el cotejo no hace falta; se hará si algún día una glosa cita la página.
- **Lorente de Nó.** Zaragoza 8-IV-1902, Tucson 2-IV-1990. Primera evidencia de circuitos cerrados: 1933 (reflejo vestíbulo-ocular); síntesis en 1938 (*J. Neurophysiol.* 1:207-244 y capítulo XV de Fulton). El artículo de McCulloch y Pitts (1943) **no cita a Lorente de Nó**: solo cita a Carnap, Hilbert-Ackermann y Whitehead-Russell. La frase real: *«The nervous system contains many circular paths, whose activity so regenerates the excitation of any participant neuron that reference to time past becomes indefinite»*: lo indefinido es la referencia al pasado. Macy: participación documentada solo en 1946; von Neumann y la memoria RAM no tienen fuente. Fuente de la tesis: Espinosa-Sánchez, Gómez-Marín y de Castro, *The Neuroscientist* 31(1):14-30 (2025).

**Añadido el 05-06/10/26 (IV·I).** *Calendrier positiviste, ou Système général de commémoration publique*: París, L. Mathias, 1849, 35 pp. (registro de la Goldsmiths' Library, Universidad de Londres). *Catéchisme positiviste* (1852): liturgia y sacramentos. Templo da Humanidade: el 17/12/2024 el templo difunde un comunicado sobre la suspensión de la visita recomendada por el IPHAN/RJ, que alcanza a la investigación y a las actividades interiores y exteriores (Diário do Rio); protegido por IPHAN, INEPAC e IRPH. Lagarrigue: Jorge (1854-1894) funda en 1883 la Iglesia Positivista de Chile, que pasa a Sociedad Positivista en 1892 y cierra con la muerte de Luis; las fuentes dan 1949 y 1956 para esa muerte, así que no se fija. Gabriel 3 (*Melt*): grabado en 1979 en Bath y The Townhouse, producción de Steve Lillywhite e ingeniería de Hugh Padgham; disco de 1980. Benjamin Constant: miembro de la Sociedad Positivista de 1876 y no de la Iglesia, por desacuerdo con el pago de subsidios a sus dirigentes (bibliografía secundaria brasileña). «Monocultura tecnológica» circula en la bibliografía secundaria sobre Hui (*Fragmentar el futuro*, Caja Negra, 2020). Barreda: en 1867 encabeza la comisión educativa de Juárez y funda la Escuela Nacional Preparatoria, que dirige durante una década. Ingenieros (1877-1925): positivismo cientificista; cofundador del Partido Socialista argentino (1896). Pierre Laffitte (1823-1903) dirige la sección ortodoxa del positivismo y Émile Littré rechaza la Religión de la Humanidad. La compra del edificio de la rue Payenne por la Iglesia brasileña en 1903 consta en una sola fuente y no se usa hasta tener otra. La frase «Tras cualquier cobardía se esconde el miedo a pensar» es de OB/OC y está referenciada al principio del libro. Pendientes de contrastar: año de la edición española de *La pregunta por la técnica en China*, edición de la cita de Kierkegaard, cita literal de Hui con página, estado del templo tras diciembre de 2024.

**Avisos sobre el material del epílogo** (de memoria, a contrastar antes de usar): «Penrose demostró matemáticamente…» es falso, porque el argumento gödeliano de Penrose está muy discutido y no es una demostración; el «agua de capa excluida» procede de Gerald Pollack, está fuera de Orch-OR y es disputada; «miles de veces por segundo» no es la cifra de Orch-OR (del orden de 40 por segundo); el biocentrismo de Lanza no es ciencia establecida; «memoria del agua» remite a Benveniste (*Nature*, 1988), resultado rechazado. Todo lo que no esté establecido va declarado como hipótesis o como juego simbólico (Norma 13), no como física.
