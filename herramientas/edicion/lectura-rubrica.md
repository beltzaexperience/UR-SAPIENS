# Lectura de ocho lectores independientes: protocolo

Reconstrucción del protocolo con el que se leyeron las piezas (el texto exacto de las instrucciones a los lectores no se conservó; la Norma 55, en su registro, ya lo describe como «rúbrica reconstruida»). Resumen de las notas con `lectura-resumen.py`.

**Lectores.** Ocho subagentes nuevos por ronda, sin conocer al autor, la historia de la pieza ni las rondas anteriores. Cada uno recibe el cuerpo y la glosa de la pieza evaluada y las dos piezas de calibración (`calibracion/angostura.txt` e `islandia1.txt`), en orden rotado entre lectores.

**Puntuación de 1 a 5, con medios puntos, en nueve criterios.**
- Calidad: *aporte* a la tesis y originalidad; *prosa* (voz, ritmo, imagen; se penalizan muletillas y relleno); *evidencia* (hechos, fuentes, glosa; se penalizan la pseudociencia y las etimologías presentadas como hecho).
- Impacto: *público* (gancho, claridad, carga emocional y política); *editores* (singularidad, valor citable, papel en la estructura; baja si hay riesgo legal o reputacional o si es redundante).
- Añadidos el 20/10/26: *entrada* (las primeras frases); *emoción* (intensidad sostenida); *no especialista* (lector que se salta los términos técnicos); *memorabilidad*.

**Nota** = 60 % calidad + 40 % impacto. **α** desde 3,34; **β** de 2,74 a 3,33; **γ** por debajo. Ajuste de calibración: se suma la diferencia entre la nota oficial de las piezas de referencia (Angostura 3,50, Islandia I 3,16) y la que les dio ese lector.

**Formato de respuesta de cada lector** (una línea por pieza leída, una carpeta con un .txt por lector):
```
pieza|aporte|prosa|evidencia|publico|editores|entrada|emocion|noespecialista|memorabilidad
angostura|…
islandia1|…
ENGANCHA: frase que más engancha
FRIO: tramos donde se enfría
VIVO: tramo más vivo
REPAROS: reparos repetidos
SACA: frases que sacan al lector
```

**Cautelas.** Los lectores son subagentes del mismo modelo, no personas: sirven para comparar versiones entre sí. La dispersión entre lectores es de ≈0,1 a 0,2 puntos de nota; diferencias entre rondas menores de ≈0,1 son ruido. La lectura vale más por los reparos que señala, que se convierten en deberes de la pieza, que por la nota: una ronda al empezar, como diagnóstico, y otra al final, para la nota; las intermedias aportaron poco a la nota (CULTURA, 24/10/26).
