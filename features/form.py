"""
license info
"""


from enum import Enum, unique


@unique
class Form(Enum):
    """
    An enumeration representing the different forms a verb and its associated
    phrase can take. The form is recorded under the {@code Feature.FORM} feature
    and applies to verbs and verb phrases.
    """

    # The bare infinitive is the base form of the verb.
    BARE_INFINITIVE = 1

    # In English, the gerund form refers to the usage of a verb as a noun. For
    # example, <em>I like <b>swimming</b></em>. In more general terms, gerunds
    # are usually formed from the base word with <em>-ing</em> added to the
    # end.
    GERUND = 2

    # The imperative form of a verb is the one used when the grammatical
    # mood is one of expressing a command or giving a direct request. For example,
    # <em><b>Close</b> the door.</em>
    IMPERATIVE = 3

    # The infinitive form represents the base form of the verb, with our
    # without the particle <em>to</em>. For example, <em>do</em> and
    # <em>to do</em> are both infinitive forms of <em>do</em>
    INFINITIVE = 4

    # Normal form represents the base verb. For example, <em>kiss</em>,
    # <em>walk</em>, <em>bark</em>, <em>eat</em>
    NORMAL = 5

    # Most verbs will have only a single form for the past tense. However, some
    # verbs will have two forms, one for the simple past tense and one for the
    # past participle (also knowns as passive participle or perfect
    # participle). The part participle represents the second of these two
    # forms. For example, the verb <em>eat</em> has the simple past form of
    # <em>ate</em> and also the past participle form of <em>eaten</em>. Another
    # example, is <em>write</em>, <em>wrote</em> and <em>written</em>.
    PAST_PARTICIPLE = 6

    # The present participle is identical in form to the gerund and is normally
    # used in the active voice. However, the gerund is meant to highlight a
    # verb being used as a noun. The present participle remains as a verb. For
    # example, <em>Jim was <b>sleeping</b></em>
    PRESENT_PARTICIPLE = 7
