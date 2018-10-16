# coding: utf8
import pytest
from lang.en.morphology.inflection_noun import InflectionNoun


@pytest.fixture
def inf():
    return InflectionNoun()


def test_with_empty_basetoken(inf):
    assert inf.regular_plural_noun() == ""
    assert inf.greco_latin_plural_noun() == ""


def test_with_regular_noun_ending_in_consonant_y(inf):
    """-Cy**, where C is any consonant"""
    assert "flies" == inf.regular_plural_noun("fly")
    assert "authorities" == inf.regular_plural_noun("authority")
    assert "bodies" == inf.regular_plural_noun("body")
    assert "cherries" == inf.regular_plural_noun("cherry")


def test_with_regular_noun_ending_in_s_z_x_sh_ch(inf):
    """ending in either s, z, x, sh, ch"""
    assert "waltzes" == inf.regular_plural_noun("waltz")
    assert "kisses" == inf.regular_plural_noun("kiss")
    assert "boxes" == inf.regular_plural_noun("box")
    assert "ashes" == inf.regular_plural_noun("ash")
    assert "Englishes" == inf.regular_plural_noun("English")
    assert "watches" == inf.regular_plural_noun("watch")


def test_with_other_regular_noun(inf):
    assert "apples" == inf.regular_plural_noun("apple")
    assert "languages" == inf.regular_plural_noun("language")


def test_grecolatin_noun(inf):
    assert "foci" == inf.greco_latin_plural_noun("focus")
    assert "traumata" == inf.greco_latin_plural_noun("trauma")
    assert "larvae" == inf.greco_latin_plural_noun("larva")
    assert "taxa" == inf.greco_latin_plural_noun("taxon")
    assert "analyses" == inf.greco_latin_plural_noun("analysis")
    assert "cystides" == inf.greco_latin_plural_noun("cystis")
    assert "foramina" == inf.greco_latin_plural_noun("foramen")
    assert "indices" == inf.greco_latin_plural_noun("index")
    assert "matrices" == inf.greco_latin_plural_noun("matrix")
    assert "cacti" == inf.greco_latin_plural_noun("cactus")
