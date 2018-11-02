"""
license info
"""

import abc
from framework.lexical_category import LexicalCategory
from framework.phrase_category import PhraseCategory


class LexicalFeature:
    """
    This class defines a list of constant values used by realizer lexicons
    """

    __metaclass__ = abc.ABCMeta

    # This feature is used to map an acronym element to the full forms of the
    # acronym.
    ACRONYM_OF = "acronym_of"

    # This feature is used to map a word to its acronyms
    ACRONYMS = "acronyms"

    # This feature is used to specify, for a given word, what its default
    # inflectional variant is, if more than one is possible.
    DEFAULT_INFL = "default_infl"

    # This feature is used to specify the spelling variants of a word.
    SPELL_VARS = "spell_vars"

    # This feature is used to specify the default spelling variant of a word,
    # if it has more than one.
    DEFAULT_SPELL = "default_spell"

    # This feature is used to define the base form for phrases and words
    BASE_FORM = "base_form"

    # This feature is used for determining the position of adjectives. Setting
    # this value to true means that the adjective can occupy the
    # <em>classifying</em> position.
    CLASSIFYING = "classifying"

    # This feature is used for determining the position of adjectives. Setting
    # this value to true means that the adjective can occupy the
    # <em>colour</em> position.
    COLOUR = "colour"

    # This feature gives the comparative form for adjectives and adverbs. For
    # example, <em>dizzier</em> is the comparative form of <em>dizzy</em>,
    # <em>fatter</em> is the comparative form of <em>fat</em> and
    # <em>earlier</em> is the comparative form of <em>early</em>.
    COMPARATIVE = "comparative"

    # This feature determines if a verb is ditransitive, meaning that it can
    # have a subject, direct object and indirect object. For example in the
    # phrase <em>he gave Mary ten pounds</em>, the verb <em>give</em> has three
    # components: the subject is the person doing the giving (<em>he</em>), the
    # direct object is the object being passed (<em>ten pounds</em>) and the
    # indirect object is the recipient (<em>Mary</em>).
    DITRANSITIVE = "ditransitive"

    # This feature determines whether a noun is masculine, feminine or neuter
    # in nature.
    GENDER = "gender"

    # This flag determines if an adverb is an intensifier, such as
    # <em>very</em>.
    INTENSIFIER = "intensifier"

    # This flag highlights a verb that can only take a subject and no objects.
    INTRANSITIVE = "intransitive"

    # This feature gives the past tense form of a verb. For example, the past
    # tense of <em>eat</em> is <em>ate</em>, the past tense of <em>walk</em> is
    # <em>walked</em>.
    PAST = "past"

    # This feature gives the past participle tense form of a verb. For many
    # verbs the past participle is exactly the same as the past tense, for
    # example, the verbs <em>talk</em>, <em>walk</em> and <em>say</em> have
    # past tense and past participles of <em>talked</em>, <em>walked</em> and
    # <em>said</em>. Contrast this with the verbs <em>do</em>, <em>eat</em> and
    # <em>sing</em>. The past tense of these verbs is <em>did</em>,
    # <em>ate</em> and <em>sang</em> respectively. while the respective past
    # participles are <em>done</em>, <em>eaten</em> and <em>sung</em>
    PAST_PARTICIPLE = "pastParticiple"

    # This feature gives the plural form of a noun. For example, the plural of
    # <em>dog</em> is <em>dogs</em> and the plural of <em>sheep</em> is
    # <em>sheep</em>
    PLURAL = "plural"

    #  This flag is set on adjectives that can also be used as a predicate. For
    # example <em>happy</em>.
    PREDICATIVE = "predicative"

    # This feature gives the present participle form of a verb. For example,
    # the present participle form of <em>eat</em> is <em>eating</em> and the
    # present participle form of <em>walk</em> is <em>walking</em>.
    PRESENT_PARTICIPLE = "presentParticiple"

    # This feature gives the present third person singular form of a verb. For
    # example, the present participle form of <em>eat</em> is <em>eats</em> as
    # in <em>the dog eats</em>. Another example is <em>ran</em> being the
    # present third person singular form of <em>run</em> as in
    # <em>John ran home</em>.
    PRESENT3S = "present3s"

    # This flag is used to determine whether a noun is a proper noun, such as a
    # person's name.
    PROPER = "proper"

    # This feature is used for determining the position of adjectives. Setting
    # this value to true means that the adjective can occupy the
    # <em>qualitative</em> position.
    QUALITATIVE = "qualitative"

    # This flag is set if a pronoun is written in the reflexive form. For
    # example, <em>myself</em>, <em>yourself</em>, <em>ourselves</em>.
    REFLEXIVE = "reflexive"

    # This feature is used to define whether an adverb can be used as a clause
    # modifier, which are normally applied at the beginning of clauses. For
    # example, <em>unfortunately</em>.
    SENTENCE_MODIFIER = "sentence_modifier"

    # This feature gives the superlative form for adjectives and adverbs. For
    # example, <em>fattest</em> is the superlative form of <em>fat</em> and
    # <em>earliest</em> is the superlative form of <em>early</em>.
    SUPERLATIVE = "superlative"

    # This flag highlights a verb that can only take a subject and an object.
    TRANSITIVE = "transitive"

    # This feature is used to define whether an adverb can be used as a verb
    # modifier, which are normally added in a phrase before the verb itself.
    # For example, <em>quickly</em>.
    VERB_MODIFIER = "verb_modifier"

    # This feature determines if the pronoun is an expletive or not. Expletive
    # pronouns are usually <em>it</em> or <em>there</em> in sentences such as:<br>
    # <em><b>It</b> is raining now.</em><br>
    # <em><b>There</b> are ten desks in the room.</em>
    EXPLETIVE_SUBJECT = "expletive_subject"

    @staticmethod
    def get_inflectional_features(cat):
        """
        Return those features related to a word's inflection, depending on its
        category, that is, the constants for
        <code>PAST, PAST_PARTICIPLE, PLURAl, PRESENT_PARTICIPLE, PRESENT3S, COMPARATIVE</code>
        or <code>SUPERLATIVE</code>.
        :param cat: ElementCategory
        :return: List of possible features for the ElementCategory
        """

        possible_features = []

        if cat in (PhraseCategory.NOUN_PHRASE, LexicalCategory.NOUN):
            possible_features.append(LexicalFeature.PLURAL)
        elif cat in (PhraseCategory.VERB_PHRASE, LexicalCategory.VERB):
            possible_features.append([LexicalFeature.PAST,
                                      LexicalFeature.PAST_PARTICIPLE,
                                      LexicalFeature.PRESENT_PARTICIPLE,
                                      LexicalFeature.PRESENT3S])
        elif cat in (PhraseCategory.ADJECTIVE_PHRASE, LexicalCategory.ADJECTIVE):
            possible_features.append([LexicalFeature.COMPARATIVE, LexicalFeature.SUPERLATIVE])

        return possible_features
