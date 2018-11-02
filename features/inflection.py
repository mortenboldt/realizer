"""
license info
"""


from enum import Enum, unique


@unique
class Inflection(Enum):
    """
    An enumeration representing the different types of morphology patterns used
    by the basic morphology processor included with realizer. This enumeration
    is a way of informing the morphology processor which set of rules should be
    used when inflecting the word.

    The pattern is recorded in the {@code Feature.PATTERN} feature and applies to
    adjectives, nouns and verbs.

    It should be noted that the morphology processor will use user-defined
    inflections or those found in a lexicon first before applying the supplied rules.
    """

    # The morphology processor has simple rules for pluralising Greek and Latin
    # 	 * nouns. The full list can be found in the explanation of the morphology
    # 	 * processor. An example would be turning <em>focus</em> into <em>foci</em>.
    # 	 * The Greco-Latin rules are generally more complex than the basic rules.
    GRECO_LATIN_REGULAR = 1

    # A word having an irregular pattern essentially means that none of the
    # 	 * supplied rules can be used to correctly inflect the word. The inflection
    # 	 * should be defined by the user or appear in the lexicon. <em>sheep</em> is
    # 	 * an example of an irregular noun.
    IRREGULAR = 2

    # Regular patterns represent the default rules when dealing with
    # 	 * inflections. A full list can be found in the explanation of the
    # 	 * morphology processor. An example would be adding <em>-s</em> to the end
    # 	 * of regular nouns to pluralise them.
    REGULAR = 3

    # Regular double patterns apply to verbs where the last consonant is
    # 	 * duplicated before applying the new suffix. For example, the verb
    # 	 * <em>tag</em> has a regular double pattern as its inflected forms include
    # 	 * <em>tagged</em> and <em>tagging</em>.
    REGULAR_DOUBLE = 4

    # The value for uncountable nouns, which are not inflected in their plural form.
    UN_COUNT = 5

    # The value for words which are invariant, that is, are never inflected.
    INVARIANT = 6
