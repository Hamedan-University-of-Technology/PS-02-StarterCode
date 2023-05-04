from math import log
from ps02 import power_and_log


def test_power_and_log():
    assert power_and_log(2, 3) == (8, log(2, 2))
    assert power_and_log(10, 2) == (100, log(10, 2))
