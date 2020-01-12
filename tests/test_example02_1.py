import pytest

from curso.example02 import get_animal


@pytest.mark.parametrize("animal, resolution", (
        ("", 0),
        ("test", 0),
        ("test", 1000000)
))
def test_get_animal_invalid_params(animal, resolution):
    with pytest.raises(Exception):
        get_animal(animal, resolution)
