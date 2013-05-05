# python class to build data from commands

class Builder():

    def __init__(self):
        """ reset internal data on construct """
        self.newData()

    # reset state 
    def newData(self):
        self.headers = []
        self.row = {}
        self.data = []
    
    def addHeader(self, name):
        """ add a new header value """
        self.headers.append(name)

    def newRow(self):
        if (len(self.row) > 0):
            self.data.append(self.row.copy())
        self.row = {}

    def addItem(self, value):
        """ add a new cell value for the current key """
        if (len(self.headers) > len(self.row)):
            key = self.headers[len(self.row)] 
            self.row[key] = value
        else:
            # throw exception
            raise Exception('too few headers')

    def getData(self):
        """ return the produced data """
        if (len(self.row) > 0):
            self.data.append(self.row.copy())
        return self.data


