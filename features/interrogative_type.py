"""
license info
"""


from enum import Enum, unique


@unique
class InterrogativeType(Enum):
    """
    An enumeration representing the different types of interrogatives or
    questions that realizer can realise.
    """

    # The type of interrogative relating to the manner in which an event
    # 	 * happened. For example, <em>John kissed Mary</em> becomes
    # 	 * <em>How did John kiss Mary?</em>
    HOW = 1

    # A how question related to a predicative sentence,
    # such as <i>John is fine</i>, which becomes <i>How is John?</i>
    HOW_PREDICATE = 2

    # This type of interrogative is a question pertaining to the object of a
    # 	 * phrase. For example, <em>John bought a horse</em> becomes <em>what did
    # 	 * John buy?</em> while <em>John gave Mary a flower</em> becomes
    # 	 * <em>What did John give Mary?</em>
    WHAT_OBJECT = 3

    # This type of interrogative is a question pertaining to the subject of a
    # 	 * phrase. For example, <em>A hurricane destroyed the house</em> becomes
    # 	 * <em>what destroyed the house?</em>
    WHAT_SUBJECT = 4

    # This type of interrogative concerns the object of a verb that is to do
    # 	 * with location. For example, <em>John went to the beach</em> becomes
    # 	 * <em>Where did John go?</em>
    WHERE = 5

    # This type of interrogative is a question pertaining to the indirect
    # 	 * object of a phrase when the indirect object is a person. For example,
    # 	 * <em>John gave Mary a flower</em> becomes
    # 	 * <em>Who did John give a flower to?</em>
    WHO_INDIRECT_OBJECT = 6

    # This type of interrogative is a question pertaining to the object of a
    # 	 * phrase when the object is a person. For example,
    # 	 * <em>John kissed Mary</em> becomes <em>who did John kiss?</em>
    WHO_OBJECT = 7

    # This type of interrogative is a question pertaining to the subject of a
    # 	 * phrase when the subject is a person. For example,
    # 	 * <em>John kissed Mary</em> becomes <em>Who kissed Mary?</em> while
    # 	 * <em>John gave Mary a flower</em> becomes <em>Who gave Mary a flower?</em>
    WHO_SUBJECT = 8

    # The type of interrogative relating to the reason for an event happening.
    # 	 * For example, <em>John kissed Mary</em> becomes <em>Why did John kiss Mary?</em>
    WHY = 9

    # This represents a simple yes/no questions. So taking the example phrases
    # 	 * of <em>John is a professor</em> and <em>John kissed Mary</em> we can
    # 	 * construct the questions <em>Is John a professor?</em> and
    # 	 * <em>Did John kiss Mary?</em>
    YES_NO = 10

    # This represents a "how many" questions. For example of
    # 	 * <em>dogs chased John/em> becomes <em>How many dogs chased John</em>
    HOW_MANY = 11

    def is_object(self, is_object_type):
        """
        A method to determine if the {@code InterrogativeType} is a question
        concerning an element with the discourse function of an object.
        :param is_object_type: InterrogativeType
        :return: bool
        """
        return is_object_type in (self.WHAT_OBJECT, self.WHO_OBJECT)

    def is_indirect_object(self, is_indirect_object_type):
        """
        A method to determine if the {@code InterrogativeType} is a question
        concerning an element with the discourse function of an indirect object.
        :param is_indirect_object_type:
        :return:
        """
        return self.WHO_INDIRECT_OBJECT == is_indirect_object_type
