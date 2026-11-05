import pytest
from train_fare import base_fare, concession, tatkal_charge

#Example test cases:
def test_sleeper_fare():
    assert base_fare("SL", 500) == 500

def test_adult_no_concession():
    assert concession(30, "M", False) == 0

def test_invalid_train_class():
    with pytest.raises(ValueError):
        base_fare("XX", 500)

def test_invalid_distance():
    with pytest.raises(ValueError):
        base_fare("SL", -100)

def test_minimum_fare():
    assert base_fare("SL", 10) == 50

def test_tatkal_no_concession():
    assert concession(65, "F", True) == 0

def test_child_under_five():
    assert concession(4, "M", False) == 100

def test_child_concession():
    assert concession(12, "F", False) == 50

def test_senior_female_concession():
    assert concession(65, "F", False) == 50

def test_senior_male_concession():
    assert concession(65, "M", False) == 40

def test_sleeper_tatkal_minimum():
    assert tatkal_charge("SL", 500) == 100

def test_ac_tatkal_maximum():
    assert tatkal_charge("3A", 2000) == 400

def test_tatkal_charge_between_limits():
    assert tatkal_charge("SL", 2000) == 200
