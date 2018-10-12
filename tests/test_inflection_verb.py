# coding: utf8
import pytest
from lang.en.morphology.inflection_verb import InflectionVerb

@pytest.fixture
def inf():
  return InflectionVerb()


def test_with_verb_be(inf):
  assert "is" == inf.regularThirdPersonSingularVerb("be")
  

def test_with_verb_ending_in_s_z_x_sh_ch(inf):
  assert "preaches" == inf.regularThirdPersonSingularVerb("preach")
  assert "watches" == inf.regularThirdPersonSingularVerb("watch")
  assert "buzzes" == inf.regularThirdPersonSingularVerb("buzz")
  assert "mixes" == inf.regularThirdPersonSingularVerb("mix")
  assert "misses" == inf.regularThirdPersonSingularVerb("miss")


def test_with_verb_ending_in_y(inf):
  assert "flies" == inf.regularThirdPersonSingularVerb("fly")
  assert "tries" == inf.regularThirdPersonSingularVerb("try")


def test_with_verb_others(inf):
  assert "works" == inf.regularThirdPersonSingularVerb("work")
  assert "requires" == inf.regularThirdPersonSingularVerb("require")