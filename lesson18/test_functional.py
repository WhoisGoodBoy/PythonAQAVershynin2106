from lesson18.code_for_testing import Human
import pytest


a = "color,expected"
@pytest.mark.xfail(reason='failed due to known bug @83483289')
def test_change_hair_color():
    human = Human('Alnert', 80, 'pink')
    human.change_color('black')
    assert human.color == 'blacak'

@pytest.mark.skip('this test would be skipped')
def test_age_growth(human):
    human.grow()
    assert human.age == 26


@pytest.mark.smoke
@pytest.mark.regression
def test_age_growth2(human):
    human.grow()
    assert human.age == 26


@pytest.mark.parametrize(
    a, [('black','black'),('white','white')],ids=['change to black', 'change to white']
)
def test_change_hair_color2(human, color, expected):
    human.change_color(color)
    assert human.color == expected

def test_check_raise_for_exception(human):
    with pytest.raises(Exception):
        human.change_color('ginger')