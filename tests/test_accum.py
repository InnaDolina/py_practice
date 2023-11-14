import pytest

from stuff.accum import Accumulator


def test_accumulator_init():
    accum = Accumulator()
    assert  accum.count == 0


def test_accumulator_add_one():
    accum = Accumulator()
    accum.__add__(1)
    assert  accum.count == 1


def test_accumulator_add_three():
    accum = Accumulator()
    accum.__add__(3)
    assert  accum.count == 3


def test_accumulator_add_twice():
    accum = Accumulator()
    accum.__add__(1)
    accum.__add__(1)
    assert  accum.count == 2


def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter"):
        accum.count = 10

