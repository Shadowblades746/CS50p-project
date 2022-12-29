# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from project import good_morning
from project import good_afternoon
from project import good_evening


def test_good_morning():
    assert good_morning("good") == "good morning"


def test_good_afternoon():
    assert good_afternoon("good") == "good afternoon"


def test_good_evening():
    assert good_evening("good") == "good evening"
