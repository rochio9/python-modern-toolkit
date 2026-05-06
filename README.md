# Python Modern Toolkit

Exploración del stack Python 2026: type system moderno, async, performance, data engineering con Polars y DuckDB, packaging con uv, observabilidad estructurada y deploy de APIs.

Combina ejercicios algorítmicos breves con notas técnicas de investigación y mini-proyectos integradores.

## Estructura

- `src/exercises/` — Ejercicios algorítmicos (LeetCode / HackerRank / StrataScratch).
- `src/projects/` — Mini-proyectos semanales integradores.
- `src/benchmarks/` — Comparativas de performance (Pandas/Polars/DuckDB, sync/async).
- `tests/` — Tests con pytest + hypothesis.
- `notes/` — Notas técnicas de investigación, una por tema.
- `data/` — Datasets para EDAs (no versionados).

## Setup

\`\`\`bash
uv sync --all-extras
\`\`\`

## Ejecutar

\`\`\`bash
uv run pytest                          # todos los tests
uv run pytest tests/exercises -v       # solo ejercicios
uv run pytest --cov=src                # con coverage
uv run ruff check .                    # lint
uv run ruff format .                   # formateo
\`\`\`

## Convenciones

- Python 3.12+, type hints estrictos (PEP 604 / 612 / 695).
- Un módulo por ejercicio: `src/exercises/day_NN_slug.py`.
- Un test por módulo: `tests/exercises/test_day_NN_slug.py`.
- Cada solución incluye docstring con URL, complejidad y decisiones técnicas.
- Conventional Commits con scope: `feat(exercises): ...`, `docs(notes): ...`, `feat(projects): ...`.

## Progreso

- [ ] **Semana 1** — Python moderno: types, errors, idioms.
- [ ] **Semana 2** — Performance, profiling, async.
- [ ] **Semana 3** — Data stack moderno: Pandas → Polars → DuckDB.
- [ ] **Semana 4** — Observabilidad, packaging, deploy.

## Notas técnicas

| # | Tema | Link |
|---|------|------|
| _Pendiente_ | | |

## Mini-proyectos

| Semana | Proyecto | Estado |
|--------|----------|--------|
| 1 | Refactor de ejercicios en paquete instalable | ⚪ Pendiente |
| 2 | Async web scraper con Pydantic | ⚪ Pendiente |
| 3 | EDA con Polars + DuckDB en marimo | ⚪ Pendiente |
| 4 | API FastAPI dockerizada deployada | ⚪ Pendiente |