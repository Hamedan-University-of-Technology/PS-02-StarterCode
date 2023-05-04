import math
import pytest
from ps02 import power_and_log

def test_power_and_log():
    assert power_and_log(2, 3) == (8, 1)
    assert power_and_log(10, 2) == (100, 3.321928094887362)
    assert power_and_log(5, 0) == (1, float('-inf'))

def test_invalid_input():
    with pytest.raises(ValueError):
        power_and_log("abc", 2)
    with pytest.raises(ValueError):
        power_and_log(3, "xyz")
    with pytest.raises(ValueError):
        power_and_log(-1, 2)

def test_zero_power():
    assert power_and_log(2, 0) == (1, float('-inf'))
    assert power_and_log(0, 5) == (0, float('-inf'))

