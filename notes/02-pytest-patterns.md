# Patterns esenciales de pytest

> Nota técnica · 2026-05-06 · Aplicable a `tests/exercises/`

## TL;DR

Cinco mecanismos de pytest que cubren ~90% del testing profesional en Python:

1. **Fixtures** — preparación de datos/estado reutilizable.
2. **`parametrize` con ids** — múltiples casos con nombres legibles.
3. **`conftest.py`** — fixtures compartidas sin imports explícitos.
4. **Markers** — etiquetar tests para skip/xfail/categorización.
5. **Fixtures built-in** — `tmp_path`, `monkeypatch`, `capsys`.
   
## 1. Fixtures

Función que prepara datos o contextos para tests:
- crea datos
- abre conexiones
- Prepara objetos

Reemplaza `setUp`/`tearDown` con funciones decoradas que se inyectan por nombre.

\`\`\`python
import pytest

@pytest.fixture
def numero() -> int:
    return 7

def test_suma(numero: int) -> bool:
    assert numero + 3 == 10
\`\`\`

Del ejerciocio del día 01:

\`\`\`python
import pytest

@pytest.fixture
def sample_data() -> list[int]:
    return [2, 7, 11, 15]

def test_two_sum_with_fixture(sample_data: list[int]) -> None:
    assert two_sum(sample_data, 9) == (0, 1)
\`\`\`

**Scopes** (por defecto `function`, recreada en cada test):

| Scope | Recreación |
|-------|-----------|
| `function` | Por test (default) |
| `class` | Por clase |
| `module` | Por archivo |
| `session` | Una vez por sesión completa |

**Yield-fixtures** para setup + teardown:

\`\`\`python
@pytest.fixture
def temp_db():
    db = create_db()         # setup
    yield db                 # test corre aquí
    db.close()               # teardown garantizado
\`\`\`

## 2. `parametrize` avanzado

\`\`\`python
@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        pytest.param([2, 7], 9, (0, 1), id="basic"),
        pytest.param([3, 3], 6, (0, 1), id="duplicates"),
        pytest.param([], 0, None, id="empty", marks=pytest.mark.xfail),
    ],
)
def test_cases(nums, target, expected): ...
\`\`\`

Beneficios: ids legibles en output (`test_cases[basic]` vs `test_cases[0]`), marks por caso individual, casos esperados a fallar sin romper la suite.

## 3. `conftest.py`

Archivo especial cargado automáticamente. Las fixtures ahí definidas son globales al directorio.

\`\`\`python
# tests/conftest.py
import pytest

@pytest.fixture
def small_array() -> list[int]:
    return [1, 2, 3, 4, 5]
\`\`\`

`small_array` ahora está disponible en cualquier test bajo `tests/` sin importarlo.

## 4. Markers

Built-in:

\`\`\`python
@pytest.mark.skip(reason="Not implemented yet")
def test_future(): ...

@pytest.mark.skipif(sys.platform == "win32", reason="POSIX only")
def test_unix_specific(): ...

@pytest.mark.xfail(reason="Bug #123, expected fail until fixed")
def test_known_bug(): ...
\`\`\`

Custom markers (declarar en `pyproject.toml`):

\`\`\`toml
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: requires external services",
]
\`\`\`

Uso:

\`\`\`python
@pytest.mark.slow
def test_heavy_computation(): ...
\`\`\`

Ejecución selectiva: `pytest -m slow` o `pytest -m "not slow"`.

## 5. Fixtures built-in útiles

### `tmp_path` — directorio temporal por test

\`\`\`python
def test_writes_file(tmp_path: Path) -> None:
    file = tmp_path / "output.txt"
    file.write_text("hello")
    assert file.read_text() == "hello"
\`\`\`

Limpieza automática al terminar.

### `monkeypatch` — modificaciones reversibles

\`\`\`python
def test_with_env_var(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("API_KEY", "fake")
    assert os.environ["API_KEY"] == "fake"
# La env var se restaura al terminar el test
\`\`\`

### `capsys` — capturar stdout/stderr

\`\`\`python
def test_print(capsys) -> None:
    print("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
\`\`\`

## Aplicación en este repo

Decisiones tomadas en `tests/exercises/`:

- **Sin fixtures aún**: los ejercicios algorítmicos no comparten setup, agregan complejidad sin beneficio.
- **`parametrize` con ids descriptivos**: aplicado en `test_day_01_two_sum.py` para legibilidad del output.
- **Sin markers custom todavía**: los tests son rápidos. Cuando agregue benchmarks, usaré `@pytest.mark.slow`.
- **`conftest.py` futuro**: planeo agregar fixtures comunes cuando los mini-proyectos compartan datos sintéticos.

## Comando útil descubierto

Listar todos los tests sin ejecutarlos:

\`\`\`bash
uv run pytest --collect-only -q
\`\`\`

Útil para revisar nombres y verificar que `parametrize` está generando los casos esperados.

## Referencias

- [Documentación oficial pytest](https://docs.pytest.org/)
- [Bruno Oliveira — *pytest Quick Start Guide*](https://www.packtpub.com/product/pytest-quick-start-guide/9781789347562)
- [Brian Okken — *Python Testing with pytest*](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/) — la referencia más completa