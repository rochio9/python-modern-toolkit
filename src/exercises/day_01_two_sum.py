"""
Day 01 — Two Sum.

Plataforma: LeetCode #1 (Easy)
URL: https://leetcode.com/problems/two-sum/

Enunciado:
    Dado un array de enteros `nums` y un entero `target`, devolver los
    índices de los dos números cuya suma sea igual a `target`.
    Existe exactamente una solución y no se puede usar el mismo
    elemento dos veces.

Complejidad:
O(n)

Decisiones técnicas:
- Se prefiere solución de orden O(n) sobre O(n^2) para evitar iterar sobre el array más de una vez.
"""

from collections.abc import Sequence


def two_sum(nums: Sequence[int], target: int) -> tuple[int, int]:
    """Return indices `(i, j)` such that `nums[i] + nums[j] == target`.

    Args:
        nums: Sequence of integers (length >= 2).
        target: Target sum.

    Returns:
        Tuple `(i, j)` with `i < j` such that `nums[i] + nums[j] == target`.

    Raises:
        ValueError: If no valid pair exists.
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        if (complement_idx := seen.get(target - num)) is not None:
            return complement_idx, i
        seen[num] = i
    raise ValueError(f"No pair sums to {target} in given sequence.")
