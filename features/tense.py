"""
license info
"""


from enum import Enum, unique


@unique
class Tense(Enum):
    """
    An enumeration representing the different types of temporal sense that can be
    applied to a verb. The tense is recorded in the {@code Feature.TENSE} feature
    and applies to verbs and their associated phrases.

    """

    # The action described by the verb will happen in the future. For example,
    # <em>John will kiss Mary</em>, <em>the dog will eat a bone</em>.
    FUTURE = 1

    # The action described by the verb happened in the past. For example,
    # <em>John kissed Mary</em>, <em>the dog ate a bone</em>.
    PAST = 2

    # The action described by the verb is happening in the present time. For
    # example, <em>John kisses Mary</em>, <em>the dog eats a bone</em>.
    PRESENT = 3
