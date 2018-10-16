# coding: utf8
import re


class DeterminerHelper(object):
    """
    Rules for determining whether the determiner for a word should be a or an
    """

    AN_EXCEPTIONS = ["one", "180", "110"]

    VOWELS = ['a', 'e', 'i', 'o', 'u']  # y is traditionally not counted as a vowel in English

    @classmethod
    def check_ends_with_indefinite_article(cls, input_text, np):
        """
        Check to see if a string ends with the indefinite article "a" and it agrees with np.
        """
        last_char = input_text.lower()[-1]
        if last_char == "a" and cls.requires_an(np):
            return input_text + "n"
        elif last_char == "n" and not cls.requires_an(np):
            return input_text[:-1]

        return input_text

    @classmethod
    def requires_an(cls, term):
        requires_an = False

        term_lower = term.lower()
        if term_lower[0] in cls.VOWELS and not cls._is_an_exception(term_lower):
            requires_an = True
        else:
            numeric_prefix = cls._get_numeric_prefix(term_lower)
            if numeric_prefix is not None and re.search("^(8|11|18).*$", numeric_prefix):
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
            if len(stripped_term) > 0:
                for char in stripped_term:
                    if char.isdigit():
                        numeric += char
                    elif char == ",":
                        continue
                    else:
                        break

        return str(numeric) if len(numeric) > 0 else None

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
