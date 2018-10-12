# coding: utf8
import re

class InflectionNoun(object):
  """ Rules for doing inflection on nouns"""


  def regularPluralNoun(self, baseToken=None):
    """
    Builds a plural for regular nouns. The rules are performed in this order:

    For nouns ending **-Cy**, where C is any consonant, the ending
    becomes **-ies**. For example, **fly** becomes **flies**.*

    *For nouns ending **-ch**, **-s**, **-sh**, **-x**
    or **-z** the ending becomes **-es**. For example, **box**
    becomes **boxes**.*

    *All other nouns have **-s** appended the other end. For example,
    **dog** becomes **dogs**.*
    
    :param string baseToken: the base regular singular noun to pluralize
    :return string pluralized noun:
    """

    if baseToken is None:
      return ""

    if re.search(".*[^eiou]y\\Z", baseToken):
      return baseToken[:-1] + "ies"
    elif re.search(".*([szx]|(ch)|(sh))$", baseToken):
      return baseToken + "es"
    else:
      return baseToken + "s"




  def GrecoLatinPluralNoun(self, baseToken=None):
    """
    Builds a plural for Greco-Latin regular nouns. The rules are performed in
    this order:
    
    For nouns ending **-us** the ending becomes **-i**. For
    example, **focus** becomes **foci**.*
    
    For nouns ending **-ma** the ending becomes **-mata**. For
    example, **trauma** becomes **traumata**.*
    
    For nouns ending **-a** the ending becomes **-ae**. For
    example, **larva** becomes **larvae**.*
    
    For nouns ending **-um** or **-on** the ending becomes
    **-a**. For example, **taxon** becomes **taxa**.*
    
    For nouns ending **-sis** the ending becomes **-ses**. For
    example, **analysis** becomes **analyses**.*
    
    For nouns ending **-is** the ending becomes **-ides**. For
    example, **cystis** becomes **cystides**.*
    
    For nouns ending **-men** the ending becomes **-mina**. For
    example, **foramen** becomes **foramina**.*
    
    For nouns ending **-ex** the ending becomes **-ices**. For
    example, **index** becomes **indices**.*
    
    For nouns ending **-x** the ending becomes **-ces**. For
    example, **matrix** becomes **matrices**.*

    :param string baseToken: the base GrecoLatin singular noun to pluralize
    :return string pluralized noun:
    """
    
    if baseToken is None:
      return ""
    
    if baseToken.endswith("us"):
      return baseToken[:-2] + "i"
    elif baseToken.endswith("ma"):
      return baseToken + "ta"
    elif baseToken.endswith("a"):
      return baseToken[:-1] + "ae"
    elif baseToken.endswith(("on", "um")):
      return baseToken[:-2] + "a"
    elif baseToken.endswith("sis"):
      return baseToken[:-3] + "ses"
    elif baseToken.endswith("is"):
      return baseToken[:-2] + "ides"
    elif baseToken.endswith("men"):
      return baseToken[:-3] + "mina"
    elif baseToken.endswith("ex"):
      return baseToken[:-2] + "ices"
    elif baseToken.endswith("x"):
      return baseToken[:-1] + "ces"