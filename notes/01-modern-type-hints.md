# Type hints en Python (PEP 604, 612, 695)

> Nota técnica · 2026-05-05 · Aplicada en `src/exercises/day_01_two_sum.py`

## TL;DR

Desde Python 3.10+ los type hints se simplificaron. Tres PEPs marcan el estilo actual:

- **PEP 604** (3.10): `int | None` reemplaza `Optional[int]`; `int | str` reemplaza `Union[int, str]`.
- **PEP 612** (3.10): `ParamSpec` para genéricos sobre callables.
- **PEP 695** (3.12): `type X = ...` para alias de tipo, `class Foo[T]:` para genéricos sin `TypeVar` explícito.

## Antes vs ahora

| Antes (typing.X) | Ahora (3.10+) |
|------------------|---------------|
| `Optional[int]` | `int \| None` |
| `Union[int, str]` | `int \| str` |
| `List[int]` | `list[int]` |
| `Dict[str, int]` | `dict[str, int]` |
| `Tuple[int, int]` | `tuple[int, int]` |
| `Callable[[int], str]` | `Callable[[int], str]` (de `collections.abc`) |

## Ejemplo aplicado

\`\`\`python
# Estilo antiguo (pre-3.10)
from typing import List, Dict, Optional, Union

def process(
    items: List[Dict[str, Union[int, str]]],
    config: Optional[Dict[str, int]] = None,
) -> List[int]:
    ...

# Estilo moderno (3.10+)
def process(
    items: list[dict[str, int | str]],
    config: dict[str, int] | None = None,
) -> list[int]:
    ...
\`\`\`

## Decisión sobre `Sequence` vs `list`

En `day_01_two_sum.py` el parámetro es `Sequence[int]`, no `list[int]`.

Razón: el algoritmo solo necesita iteración indexada y `len()` — ambos contratos de `Sequence`, no exclusivos de `list`. Aceptar `Sequence` permite invocar la función con tuplas, deques u otras secuencias, sin que el type checker rechace el llamado. Aplicación del **Liskov Substitution Principle** vía typing.

Trade-off: el caller pierde garantía de que el argumento sea mutable. En este caso es deseable: la función no muta el input.

## Cuándo `typing.X` sigue siendo necesario

Sin equivalente nativo aún (Python 3.13):

- `TypeVar`, `ParamSpec`, `TypeVarTuple`
- `Protocol` (typing duck-typing estructural)
- `Self`, `Literal`, `Final`, `ClassVar`
- `Annotated`, `TypedDict`, `NotRequired`, `Required`

## Referencias

- [PEP 604 — Allow writing union types as `X | Y`](https://peps.python.org/pep-0604/)
- [PEP 612 — Parameter Specification Variables](https://peps.python.org/pep-0612/)
- [PEP 695 — Type Parameter Syntax](https://peps.python.org/pep-0695/)
- *Fluent Python* (3rd ed., Ramalho 2022), cap. 8 "Type Hints in Functions".