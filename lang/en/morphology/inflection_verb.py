# coding: utf8
"""
Rules for doing inflection on verbs

"""


import re


class InflectionVerb:
    """Rules for doing inflection on verbs"""

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

        output_string = ""

        if base_token is not None:
            if base_token == "be":
                output_string = "is"
            elif re.search(r".*([szx]|(ch)|(sh))$", base_token):
                output_string = base_token + "es"
            elif base_token.endswith("y"):
                output_string = base_token[:-1] + "ies"
            else:
                output_string = base_token + "s"

        return output_string
