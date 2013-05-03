# python class to build data from commands

class Builder():

    def __init__(self):
        self.newData()

    # reset state 
    def newData(self):
        self.headers = []
        self.row = []
        self.data = []
        self.data.append(self.headers)
    
    def addHeader(self, name):
        self.headers.append(name)

    def newRow(self):
        self.data.append(self.row)
        self.row = []

    # should add the value to a key from headers
    # row should be an assoc array / hash
    def addItem(self, value):
        self.row.append(value)

    def getData(self):
        return self.data


