"""
license info
"""


import abc


class InternalFeature:
    """
    This class defines a list of features internally used within the realizer system.
    """

    __metaclass__ = abc.ABCMeta

    # This feature determines if the element is an acronym.
    ACRONYM = "acronym"

    # This feature is used to reference the base word element as created by the lexicon
    BASE_WORD = "base_word"

    # This feature determines the status of a sentence
    CLAUSE_STATUS = "clause_status"

    # This feature refers to the list of complements for the phrase
    COMPLEMENTS = "complements"

    # This feature refers to the list of components in a <code>ListElement</code>.
    COMPONENTS = "components"

    # This feature is the list of coordinated phrases in a <code>CoordinatedPhraseElement</code>
    COORDINATES = "coordinates"

    # This feature defines the role each element plays in the structure of the
    # text. For example, the phrase <em>John played football</em> has
    # <em>John</em> as the subject, <em>play</em> as the base verb and
    # <em>football</em> as the complement.
    DISCOURSE_FUNCTION = "discourse_function"
    NON_MORPH = "non_morph"

    # This feature tracks any front modifiers in sentences. Front modifiers are
    # placed after the cue phrase but before the subject.
    FRONT_MODIFIERS = "front_modifiers"

    # This feature points to the head element in a phrase. The head element is
    # deemed to be the subject in a noun phrase, the verb in a verb phrase, the
    # adjective in an adjective phrase, the adverb in an adverb phrase or the
    # preposition in a preposition phrase. The <code>PhraseElement</code> has a
    # convenience method for getting and setting the head feature
    HEAD = "head"

    # This flag is used to determine if the modal should be included in the
    # verb phrase.
    IGNORE_MODAL = "ignore_modal"

    # This flag determines if the sentence is interrogative or not
    INTERROGATIVE = "interrogative"

    # This feature represents the list of post-modifier elements.
    # Post-modifiers are added to the end of phrases and coordinated phrases
    POST_MODIFIERS = "postmodifiers"

    # This feature represents the list of premodifier elements. Premodifiers
    # are added to phrases before the head of the phrase, and to coordinated
    # phrases before the coordinates.
    PRE_MODIFIERS = "premodifiers"

    # This flag is used to define whether a noun phrase has had its specifier
    # raised. It is used in conjunction with the <code>RAISE_SECIFIER</code>
    # feature.
    RAISED = "raised"

    # This flag determines if auxiliary verbs should be realised in coordinated
    # verb phrases.
    REALISE_AUXILIARY = "realise_auxiliary"

    # This feature contains the specifier for a noun phrase. For example
    # <em>the</em> and <em>my</em>.
    SPECIFIER = "specifier"

    # This feature represents the list of subjects in a clause
    SUBJECTS = "subjects"

    # This feature represents the verb phrase in a clause
    VERB_PHRASE = "verb_phrase"
