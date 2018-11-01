from enum import Enum, unique


@unique
class LexicalCategory(Enum):

    # A default value =  indicating an unspecified category.
    ANY = 1

    # The element represents a symbol.
    SYMBOL = 2

    # A noun element.
    NOUN = 3

    # An adjective element.
    ADJECTIVE = 4

    # An adverb element.
    ADVERB = 5

    # A verb element.
    VERB = 6

    # A determiner element often referred to as a specifier.
    DETERMINER = 7

    # A pronoun element.
    PRONOUN = 8

    # A conjunction element.
    CONJUNCTION = 9

    # A preposition element.
    PREPOSITION = 10

    # A complementiser element.
    COMPLEMENTISER = 11

    # A modal element.
    MODAL = 12

    # An auxiliary verb element.
    AUXILIARY = 13
