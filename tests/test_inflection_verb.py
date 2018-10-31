# coding: utf8
import pytest
from lang.en.morphology.inflection_verb import InflectionVerb


@pytest.fixture
def inf():
    return InflectionVerb()


def test_with_verb_be(inf):
    assert "is" == inf.regular_third_person_singular_verb("be")


def test_with_verb_ending_in_s_z_x_sh_ch(inf):
    assert "preaches" == inf.regular_third_person_singular_verb("preach")
    assert "watches" == inf.regular_third_person_singular_verb("watch")
    assert "buzzes" == inf.regular_third_person_singular_verb("buzz")
    assert "mixes" == inf.regular_third_person_singular_verb("mix")
    assert "misses" == inf.regular_third_person_singular_verb("miss")


def test_with_verb_ending_in_y(inf):
    assert "flies" == inf.regular_third_person_singular_verb("fly")
    assert "tries" == inf.regular_third_person_singular_verb("try")


def test_with_verb_others(inf):
    assert "works" == inf.regular_third_person_singular_verb("work")
    assert "requires" == inf.regular_third_person_singular_verb("require")

def test_with_no_token(inf):
    assert "" == inf.regular_third_person_singular_verb(None)