# coding: utf8
import pytest
from lang.en.morphology.determiner_helper import DeterminerHelper


@pytest.fixture
def helper():
    return DeterminerHelper()


def test_requires_an(helper):
    t = True
    f = False

    assert t == helper.requires_an("elephant")
    assert t == helper.requires_an("ear")
    assert t == helper.requires_an("elf")
    assert t == helper.requires_an("endorphone")

    assert f == helper.requires_an("car")
    assert f == helper.requires_an("cow")

    # Does not hand phonetics
    # @TODO
    assert f == helper.requires_an("hour")

    # But does have exceptions for some numerals
    assert f == helper.requires_an("one")
    assert f == helper.requires_an("100")
