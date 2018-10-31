# coding: utf8
import pytest
from lang.en.morphology.determiner_helper import DeterminerHelper


@pytest.fixture
def helper():
    return DeterminerHelper()


def test_requires_an(helper):
    assert helper.requires_an("elephant")
    assert helper.requires_an("ear")
    assert helper.requires_an("elf")
    assert helper.requires_an("endorphone")

    assert not helper.requires_an("car")
    assert not helper.requires_an("cow")
    assert not helper.requires_an("fish")
    assert not helper.requires_an("historic")


def test_requires_an_numeric(helper):
    assert not helper.requires_an("one")
    assert not helper.requires_an("100")
    assert not helper.requires_an("110")
    assert not helper.requires_an("180")

    assert not helper.requires_an("110000")
    assert not helper.requires_an("180000")
    assert not helper.requires_an("181,000")
    assert not helper.requires_an("185,000.25")

    assert helper.requires_an("8")
    assert helper.requires_an("8.50")
    assert helper.requires_an("80")
    assert helper.requires_an("11")
    assert helper.requires_an("11000")
    assert helper.requires_an("80000")
    assert helper.requires_an("80,000")
    assert helper.requires_an("80,000.90")


# def test_requires_an_with_phonetics(helper):
#   assert helper.requires_an("hour")
#   assert helper.requires_an("honorable")
#   assert helper.requires_an("honor")
#   assert helper.requires_an("honest")
#   assert helper.requires_an("heir")


def test_check_ends_with_indefinite_articles1(helper):
    input_text = "I see a"
    np = "elephant"
    assert "I see an" == helper.check_ends_with_indefinite_article(input_text, np)


def test_check_ends_with_indefinite_articles2(helper):
    input_text = "I see a"
    np = "cow"
    assert "I see a" == helper.check_ends_with_indefinite_article(input_text, np)


def test_check_ends_with_indefinite_articles3(helper):
    input_text = "I see an"
    np = "cow"
    assert "I see a" == helper.check_ends_with_indefinite_article(input_text, np)
