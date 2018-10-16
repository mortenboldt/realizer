# coding: utf8
import re


class InflectionVerb(object):
    """ Rules for doing inflection on verbs"""

    @staticmethod
    def regular_third_person_singular_verb(base_token=None):
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

        :param string base_token: the base third-person singular to pluralize
        :return string pluralized verb:
        """

        if base_token is None:
            return ""

        if base_token == "be":
            return "is"
        elif re.search(".*([szx]|(ch)|(sh))$", base_token):
            return base_token + "es"
        elif base_token.endswith("y"):
            return base_token[:-1] + "ies"
        else:
            return base_token + "s"
