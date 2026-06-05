from fractions import Fraction

from hypothesis import given, strategies


rationals = strategies.builds(
    Fraction,
    strategies.integers(min_value=-(2**128), max_value=2**128),
    strategies.integers(min_value=1, max_value=2**64),
)
nonzero_rationals = strategies.builds(
    Fraction,
    strategies.integers(min_value=-(2**128), max_value=2**128).filter(bool),
    strategies.integers(min_value=1, max_value=2**64),
)


def direct_division(value, y):
    return value / y


def reciprocal_multiply(value, inv):
    return value * inv


@given(
    value=strategies.floats(allow_nan=False, allow_infinity=False),
    y=strategies.one_of(
        strategies.floats(max_value=0.0, allow_nan=False, allow_infinity=False, exclude_max=True),
        strategies.floats(min_value=0.0, allow_nan=False, allow_infinity=False, exclude_min=True),
    ),
)
def test_division_equivalence(value: float, y: float) -> None:
    inv = 1.0 / y
    assert reciprocal_multiply(value, inv) == direct_division(value, y)


@given(
    value=rationals,
    y=nonzero_rationals,
)
def test_fraction_division_equivalence(value: Fraction, y: Fraction) -> None:
    inv = Fraction(1, 1) / y
    assert reciprocal_multiply(value, inv) == direct_division(value, y)
