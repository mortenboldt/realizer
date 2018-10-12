# coding: utf8
import re

class InflectionVerb(object):
  """ Rules for doing inflection on verbs"""


  def regularThirdPersonSingularVerb(self, baseToken=None):
    """
    Builds the third-person singular form for regular verbs. The rules are
    performed in this order:
    
    *If the verb is **be** the realised form is **is**.*
    *For verbs ending **-ch**, **-s**, **-sh**, **-x**
    or **-z** the ending becomes **-es**. For example,
    **preach** becomes **preaches**.*
    *For verbs ending **-y** the ending becomes **-ies**. For
    example, **fly** becomes **flies**.*
    *For every other verb, **-s** is added to the end of the word.*
    
    :param string baseToken: the base third-person singular to pluralize
    :return string pluralized verb:
    """

    if baseToken is None:
      return ""

    if baseToken == "be":
      return "is"
    elif re.search(".*([szx]|(ch)|(sh))$", baseToken):
      return baseToken + "es"
    elif baseToken.endswith("y"):
      return baseToken[:-1] + "ies"
    else:
      return baseToken + "s"
