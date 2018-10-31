# coding: utf8
"""
This module helps find the determiner for a given word

For instance "a horse", instead of "an horse", when given the word "horse"
It also works on numbers.
"""


class DeterminerHelper:
    """
    Rules for determining whether the determiner for a word should be a or an
    """

    AN_EXCEPTIONS = ["one", "180", "110"]

    VOWELS = ['a', 'e', 'i', 'o', 'u']  # y is traditionally not counted as a vowel in English

    @classmethod
    def check_ends_with_indefinite_article(cls, input_text, noun_phrase):
        """
        Check to see if a string ends with the indefinite article "a"
        and it agrees with noun_phrase.
        """
        last_char = input_text.lower()[-1]
        output_text = input_text
        if last_char == "a" and cls.requires_an(noun_phrase):
            output_text = input_text + "n"
        elif last_char == "n" and not cls.requires_an(noun_phrase):
            output_text = input_text[:-1]

        return output_text

    @classmethod
    def requires_an(cls, term):
        """
        Is is required for the term to be prefixed by "an"?
        :param term:
        :return: bool
        """
        requires_an = False

        term_lower = term.lower()
        if term_lower[0] in cls.VOWELS and not cls._is_an_exception(term_lower):
            requires_an = True
        else:
            numeric_prefix = cls._get_numeric_prefix(term_lower)
            if numeric_prefix is not None and numeric_prefix.startswith(("8", "11", "18")):
                requires_an = cls._check_number(int(numeric_prefix))

        return requires_an

    @classmethod
    def _is_an_exception(cls, term):
        return any([term == x for x in cls.AN_EXCEPTIONS])

    @classmethod
    def _get_numeric_prefix(cls, term):
        numeric = ""

        if term is not None:
            stripped_term = term.strip()
            if stripped_term:
                for char in stripped_term:
                    if char.isdigit():
                        numeric += char
                    elif char == ",":
                        continue
                    else:
                        break

        return str(numeric) if numeric else None

    @classmethod
    def _check_number(cls, number):
        """
        Returns true if the number starts with 8, 11 or 18 and is
        either less than 100 or greater than 1000, but excluding 180,000 etc.
        """

        needs_an = False
        if number == 8 or number == 11 or number == 18 or (80 <= number < 90):
            needs_an = True
        elif number > 1000:
            needs_an = cls._check_number(round(number / 1000))

        return needs_an
