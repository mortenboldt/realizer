"""
Number agreement license info
"""


from enum import Enum, unique


@unique
class NumberAgreement(Enum):
    """
    An enumeration representing the different types of number agreement.
    The number agreement is recorded in the {@code Feature.NUMBER} feature
    and applies to nouns and verbs, and their associated phrases.
    """

    # This represents words that have the same form regardless of whether they
    # are singular or plural. For example, <em>sheep</em>, <em>fish</em>.
    BOTH = 1

    # This represents verbs and nouns that are written in the singular.
    # For example, <em>dog</em> as opposed to <em>dogs</em>, and <em>John <b>kisses</b> Mary</em>.
    SINGULAR = 2

    # This represents verbs and nouns that are written in the plural.
    # For example, <em>dogs</em> as opposed to <em>dog</em>,
    # and <em>John and Simon <b>kiss</b> Mary</em>
    PLURAL = 3
