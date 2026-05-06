"""Tests for day 01 — Two Sum."""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from src.exercises.day_01_two_sum import two_sum


class TestTwoSumExamples:
    """Casos puntuales y edge cases."""

    def test_basic_case(self) -> None:
        assert two_sum([2, 7, 11, 15], 9) == (0, 1)

    def test_duplicates(self) -> None:
        assert two_sum([3, 3], 6) == (0, 1)

    def test_negatives(self) -> None:
        assert two_sum([-3, 4, 3, 90], 0) == (0, 2)

    def test_no_solution_raises(self) -> None:
        with pytest.raises(ValueError, match="No pair sums to"):
            two_sum([1, 2, 3], 100)

    def test_accepts_tuple_input(self) -> None:
        """Verifica que Sequence acepta tuplas, no solo listas."""
        assert two_sum((2, 7, 11, 15), 9) == (0, 1)

    @pytest.mark.parametrize(
        ("nums", "target", "expected"),
        [
            ([2, 7, 11, 15], 9, (0, 1)),
            ([3, 2, 4], 6, (1, 2)),
            ([3, 3], 6, (0, 1)),
            ([-1, -2, -3, -4, -5], -8, (2, 4)),
        ],
    )
    def test_parametrized(
        self,
        nums: list[int],
        target: int,
        expected: tuple[int, int],
    ) -> None:
        assert two_sum(nums, target) == expected


class TestTwoSumProperties:
    """Property-based tests con Hypothesis."""

    @given(
        nums=st.lists(
            st.integers(min_value=-1000, max_value=1000),
            min_size=2,
            max_size=100,
        ),
        target=st.integers(min_value=-2000, max_value=2000),
    )
    def test_solution_satisfies_target_or_raises(self, nums: list[int], target: int) -> None:
        """Si hay solución, debe sumar al target con índices distintos.

        Si no hay solución, debe lanzar ValueError y verificamos
        exhaustivamente que efectivamente no exista ningún par.
        """
        try:
            i, j = two_sum(nums, target)
        except ValueError:
            for a in range(len(nums)):
                for b in range(a + 1, len(nums)):
                    assert nums[a] + nums[b] != target, (
                        f"Solver dijo 'sin solución' pero "
                        f"nums[{a}]+nums[{b}] = {nums[a] + nums[b]} = target"
                    )
            return

        assert i < j, "El primer índice debe ser menor al segundo"
        assert i != j, "Los índices deben ser distintos"
        assert nums[i] + nums[j] == target

    @given(
        prefix=st.lists(st.integers(min_value=0, max_value=100), min_size=0, max_size=50),
        a=st.integers(min_value=-1000, max_value=1000),
        b=st.integers(min_value=-1000, max_value=1000),
        suffix=st.lists(st.integers(min_value=0, max_value=100), min_size=0, max_size=50),
    )
    def test_finds_first_valid_pair(
        self,
        prefix: list[int],
        a: int,
        b: int,
        suffix: list[int],
    ) -> None:
        """Construye un caso con solución conocida y verifica que se halla."""
        nums = [*prefix, a, *suffix, b]
        target = a + b
        i, j = two_sum(nums, target)
        assert nums[i] + nums[j] == target
