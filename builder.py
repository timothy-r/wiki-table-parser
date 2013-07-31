# -*- coding: utf-8 -*-
# python class to build data from commands

class Builder():

    def __init__(self):
        """ reset internal data on construct """
        self.newData()

    # reset state 
    def newData(self):
        self.keys = []
        self.set = {}
        self.data = []
    
    def addKey(self, name):
        """ add a new key value """
        self.keys.append(name)

    def newSet(self):
        """ start adding items to a new set of data """
        if (len(self.set) > 0):
            self.data.append(self.set.copy())
        self.set = {}

    def addItem(self, value):
        """ add a new cell value for the current key """
        if (len(self.keys) > len(self.set)):
            key = self.keys[len(self.set)] 
            self.set[key] = value
        else:
            # throw exception
            raise Exception('too few keys')

    def getData(self):
        """ return the produced data """
        if (len(self.set) > 0):
            self.data.append(self.set.copy())
        return self.data

