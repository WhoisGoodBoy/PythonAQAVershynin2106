import pytest


def test_sum():
    assert 2 + 2 == 4


def test_multiply():
    assert 2 * 2 == 4


@pytest.mark.skip
def test_skip():
    pass
