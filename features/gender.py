"""
license info
"""


from enum import Enum, unique


@unique
class Gender(Enum):
    """
    An enumeration representing the gender of the subject of a noun phrase, or
    the object or subject of a verb phrase. It is most commonly used with
    personal pronouns. The gender is recorded in the {@code Feature.GENDER}
    feature and applies to nouns and pronouns.
    """

    # A word or phrase pertaining to a male topic. For example, <em>he</em>,
    # <em>him</em>, <em>his</em>
    MASCULINE = 1

    # A word or phrase pertaining to a female topic. For example, <em>she</em>,
    # <em>her</em>, <em>hers</em>
    FEMININE = 2

    # A word or phrase pertaining to a neutral or gender-less topic. For
    # example, <em>it</em>, <em>its</em>
    NEUTER = 3