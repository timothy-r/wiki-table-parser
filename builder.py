# python class to build data from commands

class Builder():

    def __init__(self):
        """ reset internal data on construct """
        self.newData()

    # reset state 
    def newData(self):
        self.keys = []
        self.row = {}
        self.data = []
    
    def addKey(self, name):
        """ add a new key value """
        self.keys.append(name)

    def newRow(self):
        """ start adding items to a new set of data """
        if (len(self.row) > 0):
            self.data.append(self.row.copy())
        self.row = {}

    def addItem(self, value):
        """ add a new cell value for the current key """
        if (len(self.keys) > len(self.row)):
            key = self.keys[len(self.row)] 
            self.row[key] = value
        else:
            # throw exception
            raise Exception('too few keys')

    def getData(self):
        """ return the produced data """
        if (len(self.row) > 0):
            self.data.append(self.row.copy())
        return self.data


