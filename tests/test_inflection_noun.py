# coding: utf8
import pytest
from lang.en.morphology.inflection_noun import InflectionNoun

@pytest.fixture
def inf():
  return InflectionNoun()


def test_with_empty_basetoken(inf):
  assert inf.regularPluralNoun() == ""
  assert inf.GrecoLatinPluralNoun() == ""


def test_with_regular_noun_ending_in_consonant_Y(inf):
  """-Cy**, where C is any consonant"""
  assert "flies" == inf.regularPluralNoun("fly")
  assert "authorities" == inf.regularPluralNoun("authority")
  assert "bodies" == inf.regularPluralNoun("body")
  assert "cherries" == inf.regularPluralNoun("cherry")


def test_with_regular_noun_ending_in_s_z_x_sh_ch(inf):
  """ending in either s, z, x, sh, ch"""
  assert "waltzes" == inf.regularPluralNoun("waltz")
  assert "kisses" == inf.regularPluralNoun("kiss")
  assert "boxes" == inf.regularPluralNoun("box")
  assert "ashes" == inf.regularPluralNoun("ash")
  assert "Englishes" == inf.regularPluralNoun("English")
  assert "watches" == inf.regularPluralNoun("watch")


def test_with_other_regular_noun(inf):
  assert "apples" == inf.regularPluralNoun("apple")
  assert "languages" == inf.regularPluralNoun("language")


def test_grecolatin_noun(inf):
  assert "foci" == inf.GrecoLatinPluralNoun("focus")
  assert "traumata" == inf.GrecoLatinPluralNoun("trauma")
  assert "larvae" == inf.GrecoLatinPluralNoun("larva")
  assert "taxa" == inf.GrecoLatinPluralNoun("taxon")
  assert "analyses" == inf.GrecoLatinPluralNoun("analysis")
  assert "cystides" == inf.GrecoLatinPluralNoun("cystis")
  assert "foramina" == inf.GrecoLatinPluralNoun("foramen")
  assert "indices" == inf.GrecoLatinPluralNoun("index")
  assert "matrices" == inf.GrecoLatinPluralNoun("matrix")
  assert "cacti" == inf.GrecoLatinPluralNoun("cactus")
  
