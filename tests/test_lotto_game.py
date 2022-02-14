from lotto_game import __version__
from lotto_game import lotto


def test_version():
    assert __version__ == "0.1.0"


def test_try_match():
    random_choice = {1, 2, 3}
    my_input_sorted = {1, 2, 3}
    assert lotto.try_match(random_choice, my_input_sorted) == False
