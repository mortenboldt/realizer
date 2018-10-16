# coding: utf8
import re


class InflectionNoun(object):
    """ Rules for doing inflection on nouns"""

    @staticmethod
    def regular_plural_noun(base_token=None):
        """
        Builds a plural for regular nouns. The rules are performed in this order:

        For nouns ending **-Cy**, where C is any consonant, the ending
        becomes **-ies**. For example, **fly** becomes **flies**.*

        *For nouns ending **-ch**, **-s**, **-sh**, **-x**
        or **-z** the ending becomes **-es**. For example, **box**
        becomes **boxes**.*

        *All other nouns have **-s** appended the other end. For example,
        **dog** becomes **dogs**.*

        :param string base_token: the base regular singular noun to pluralize
        :return string pluralized noun:
        """

        if base_token is None:
            return ""

        if re.search(".*[^eiou]y\\Z", base_token):
            return base_token[:-1] + "ies"
        elif re.search(".*([szx]|(ch)|(sh))$", base_token):
            return base_token + "es"
        else:
            return base_token + "s"

    @staticmethod
    def greco_latin_plural_noun(base_token=None):
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

        :param string base_token: the base GrecoLatin singular noun to pluralize
        :return string pluralized noun:
        """

        if base_token is None:
            return ""

        if base_token.endswith("us"):
            return base_token[:-2] + "i"
        elif base_token.endswith("ma"):
            return base_token + "ta"
        elif base_token.endswith("a"):
            return base_token[:-1] + "ae"
        elif base_token.endswith(("on", "um")):
            return base_token[:-2] + "a"
        elif base_token.endswith("sis"):
            return base_token[:-3] + "ses"
        elif base_token.endswith("is"):
            return base_token[:-2] + "ides"
        elif base_token.endswith("men"):
            return base_token[:-3] + "mina"
        elif base_token.endswith("ex"):
            return base_token[:-2] + "ices"
        elif base_token.endswith("x"):
            return base_token[:-1] + "ces"
