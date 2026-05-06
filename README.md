# Python Modern Toolkit

Exploración del stack Python 2026: types, async, performance, data engineering moderno, packaging y deploy.
Combina ejercicios algorítmicos, notas técnicas de investigación y mini-proyectos integradores.

## Estructura

- `src/week_01_basics/` — Strings, listas, diccionarios (hash maps).
- `src/week_02_arrays/` — Two pointers, sliding window, arrays.
- `src/week_03_search_recursion/` — Búsqueda binaria, recursión, árboles, linked lists.
- `src/week_04_dp_pandas/` — DP, Pandas, NumPy.
- `tests/` — Tests con pytest, espejo de la estructura de `src/`.
- `notes/` — Apuntes técnicos.

## Setup

\`\`\`bash
uv sync --all-extras
\`\`\`

## Ejecutar tests

\`\`\`bash
pytest                          # todos
pytest tests/week_01_basics     # una semana
pytest tests/week_01_basics/test_day_01_two_sum.py -v   # un ejercicio
pytest --cov=src                # con coverage
\`\`\`

## Lint

\`\`\`bash
ruff check .
ruff format .
\`\`\`

## Convenciones

- Un módulo por ejercicio: `src/week_NN/day_NN_slug.py`
- Un test por módulo: `tests/week_NN/test_day_NN_slug.py`
- Cada solución tiene docstring con: URL, dificultad, complejidad temporal/espacial, decisiones clave.
- Type hints en todas las funciones públicas.

## Progreso

- [ ] Semana 1 — Strings,listas,diccionarios
- [ ] Semana 2 — Two pointers, sliding window, arrays (Medium)
- [ ] Semana 3 — Recursión, búsqueda, ordenamiento (Medium)
- [ ] Semana 4 - DP, Pandas/NumPy, casos DS (Hard / aplicado)