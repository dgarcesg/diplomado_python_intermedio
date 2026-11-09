---
name: limpiando-enaho
description: Limpia y valida los microdatos de la ENAHO 2024 del INEI (módulo 34 sumaria y módulo 02 miembros). Filtra residentes habituales, une personas y hogares, pondera con los factores de expansión y calcula la pobreza monetaria nacional, urbana/rural, por sexo, edad y departamento. Úsala cuando pidan limpiar, preparar o validar la ENAHO, cifras de pobreza del Perú en 2024, o cuando otra skill necesite salidas/personas_2024.parquet.
argument-hint: [año]
---

# Limpiar la ENAHO

Todo se corre desde la raíz del proyecto (`tarea_4/`).

1. Comprueba que existan `datos/966-Modulo34.zip` y `datos/966-Modulo02.zip` (966 = ENAHO 2024). Si faltan, bájalos:

   ```bash
   curl -L -o datos/966-Modulo34.zip https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip
   curl -L -o datos/966-Modulo02.zip https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip
   ```

2. Corre exactamente, sin reescribir el pipeline:

   ```bash
   uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio 2024
   ```

   Si piden otro año, el script lo rechaza: dilo, no inventes cifras.

3. Lee `salidas/validacion.txt`. Si el script termina con código 1 o alguna verificación esencial dice `FALLA`,
   **detente** y reporta cuál falló. Nunca ajustes resultados para que coincidan con la referencia.

4. Responde con las cifras de `salidas/indicadores.csv`, que ya están ponderadas:
   - `pobreza_pct`: personas × `facpob07` (la principal, 27.53 % nacional).
   - `pobreza_pct_sumaria`: hogares × `factor07 × mieperho`, la forma en que publica el INEI (27.58 %). Úsala si piden
     la cifra oficial o al comparar con referencias del INEI; existe solo para nacional, área y departamento.

   Para otros cortes usa `salidas/personas_2024.parquet` y pondera siempre con `facpob07`. Nunca un promedio simple.

5. Cita así: «INEI, ENAHO 2024 (módulos 34 y 02), cálculo propio con limpiar.py». Son asociaciones descriptivas: no
   afirmes causas.

6. Antes de usar una variable que no está en la base, o si dudas de un código, lee `reference.md`.
