"""
license info
"""


from enum import Enum, unique


@unique
class Person(Enum):
    """
    This is an enumeration used to represent the point of view of the narrative.
    It covers first person, second person and third person. The person is
    recorded in the {@code Feature.PERSON} feature and applies to clauses,
    coordinated phrases, noun phrases and verb phrases.
    """

    # The enumeration to show that the narration is written in the first
    # person. First person narrative uses the personal pronouns of <em>I</em>
    # and <em>we</em>.
    FIRST = 1

    # The enumeration to show that the narration is written in the second
    # person. Second person narrative uses the personal pronoun of <em>you</em>.
    SECOND = 2

    # The enumeration to show that the narration is written in the third
    # person. Third person narrative uses the personal pronouns of <em>he</em>,
    # <em>her</em> and <em>they</em>.
    THIRD = 3
