import pytest
from ps02 import power_and_log


def test_invalid_input():
    with pytest.raises(ValueError):
        power_and_log("abc", 2)

    with pytest.raises(ValueError):
        power_and_log(3, "xyz")

    with pytest.raises(ValueError):
        power_and_log(-1, 2)
