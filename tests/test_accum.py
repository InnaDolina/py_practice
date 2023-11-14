import pytest


@pytest.mark.accumulator
def test_accumulator_init(accum):
    assert  accum.count == 0


@pytest.mark.accumulator
def test_accumulator_add_one(accum):
    accum.__add__(1)
    assert  accum.count == 1


@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    accum.__add__(3)
    assert  accum.count == 3


@pytest.mark.accumulator
def test_accumulator_add_twice(accum, accum2):
    accum.__add__(1)
    accum.__add__(1)
    assert  accum.count == 2


@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter"):
        accum.count = 10

