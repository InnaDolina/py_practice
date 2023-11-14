import pytest

from stuff.accum import Accumulator


@pytest.fixture
def accum(scope='function'):
    yield Accumulator()
    print('Done with the test!')


@pytest.fixture
def accum2():
    return Accumulator()
