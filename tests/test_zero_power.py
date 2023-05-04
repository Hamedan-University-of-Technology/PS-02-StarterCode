from ps02 import power_and_log


def test_zero_power():
    assert power_and_log(2, 0) == (1, float('-inf'))
    assert power_and_log(0, 5) == (0, float('-inf'))
