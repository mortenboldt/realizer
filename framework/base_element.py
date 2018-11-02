"""
Base class for all element types.
NLGElement.java
"""

import abc
from features.number_agreement import NumberAgreement
from features.feature import Feature
from framework.element_category import ElementCategory


class BaseElement:
    """
    Base class for all element types
    """

    __metaclass__ = abc.ABCMeta

    # The category of this element
    # Type: ElementCategory
    _category = None

    # The features of this element
    # Type: Dict[str, object]
    _features = {}

    # The parent of this element
    # Type: BaseElement
    _parent = None

    # The realization of this element
    # Type: str
    _realisation = None

    # The factory that created this element
    # Type: Factory
    _factory = None

    @property
    def category(self):
        """
        Fetches the category of the element
        :return: ElementCategory: The category of the element
        """
        return self._category

    @category.setter
    def category(self, category: ElementCategory):
        """
        Sets the category of the element
        :param category: ElementCategory: The element of the category
        """
        self._category = category

    @property
    def features(self):
        """
        Fetches all the features of the element
        :return: Dict: A dict containing all the features of the element
        """
        return self._features

    def set_feature(self, feature_name, feature_value):
        """
        Adds a feature to the feature map. If the feature already exists then it
        is given the new value. If the value provided is None,
        the feature is removed from the map.
        """
        if feature_name is not None:
            if feature_value is None:
                self.remove_feature(feature_name)

            self._features[feature_name] = feature_value

    def remove_feature(self, feature_name):
        """
        Removes a feature from the element feature map
        :param feature_name: String: The name of the element to remove from the element
        :return: void
        """
        del self._features[feature_name]

    def clear_all_features(self):
        """
        Clears the feature map of the element
        :return: void
        """
        self._features.clear()

    def has_feature(self, feature_name):
        """
        Checks if the element feature map contains the given feature
        :param feature_name: String: The name of the feature to check for
        :return: bool
        """
        return feature_name in self._features

    def feature_names(self):
        """
        Retrieves the set of features currently contained in the feature map
        :return: A list of all the feature names in the feature map of this element
        """
        return self._features.keys()

    @property
    def parent(self):
        """
        Fetches the parent of the element
        :return: The parent of the element
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets a parent for the element
        :param parent: The parent of the element
        :return: void
        """
        self._parent = parent

    @abc.abstractmethod
    def children(self):
        """
        Retrieves the children for this element.
        This method need s to be overridden for each specific type of element.
        Each type of element will have its own way of determining the child elements.
        :return: List of child objects
        """
        return []

    @property
    def realisation(self):
        """
        Fetches the realissation of the element.
        Leading and trailing whitespace is removed before it is returned
        :return: String: The realisation of the element
        """
        realisation = ""
        if self._realisation:
            realisation = self._realisation.strip()

            if realisation == "":
                self._realisation = None

        return realisation

    @realisation.setter
    def realisation(self, realised):
        """
        Sets the realisation of the element to a string
        :param realised: String: The realisation of the element
        :return: void
        """
        self._realisation = realised

    def is_a(self, check_category):
        """
        Checks if the supplied ElementCategory matches the category of this element
        :param check_category: ElementCategory
        :return: bool
        """
        is_a = False

        if self.category:
            # TODO: Verify that this equality works
            is_a = self.category.__eq__(check_category)
        elif check_category is None:
            is_a = True

        return is_a

    def print_tree(self, indent):
        """
        Prints a tree of the element
        Needs verification
        :param indent: String:
        :return: String
        """
        this_indent = (" |-" if indent is None else indent + " |-")
        child_indent = (" |-" if indent is None else indent + " |-")
        out = "Element: \n"

        children = self.children()
        if children:
            for child in children:
                out += "{}{}".format(this_indent, child.print_tree(child_indent))

        print(out, end="")

    def set_plural(self, is_plural):
        """
        Sets the number agreement on this element. This method is added for
        convenience and not all element types will make use of the number
        agreement feature.
        :param is_plural: bool
        :return: void
        """
        if is_plural:
            self.set_feature(Feature.NUMBER, NumberAgreement.PLURAL)
        else:
            self.set_feature(Feature.NUMBER, NumberAgreement.SINGULAR)

    def is_plural(self):
        """
        Determines if this element is to be treated as a plural. This is a
        convenience method and not all element types make use of number agreement.
        :return: bool
        """
        return NumberAgreement.PLURAL == self.features[Feature.NUMBER]

    @property
    def factory(self):
        """
        return the factory that build this element
        :return: Factory
        """
        return self._factory

    @factory.setter
    def factory(self, factory):
        self._factory = factory

    # TODO: Implement a tostring method
    # TOdO: Implement an equality check method: Equals
