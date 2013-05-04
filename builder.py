# python class to build data from commands

class Builder():

    def __init__(self):
        """ reset internal data on construct """
        self.newData()

    # reset state 
    def newData(self):
        self.headers = []
        self.row = []
        self.data = []
        self.data.append(self.headers)
    
    def addHeader(self, name):
        """ add a new header value """
        self.headers.append(name)

    def newRow(self):
        self.data.append(self.row)
        self.row = []

    # should add the value to a key from headers
    # row should be an assoc array / hash
    def addItem(self, value):
        """ add a new cell value """
        self.row.append(value)

    def getData(self):
        """ return the produced data """
        return self.data


