""" Wrapper for an attribute list """

class AttributeList:
    attributes = [];

    def __init__(self, attributes):
        self.attributes = attributes
       
    def contains(self, key, value):
        """ test if attribute with key contains a value """
        for a in self.attributes:
            if a[0] == key and -1 != a[1].find(value):
                return True

        return False


