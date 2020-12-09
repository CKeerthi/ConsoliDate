# -*- coding: utf-8 -*-

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        
    def printName(self):
        print(self.name)
        
    def printDate(self):
        print(self.date.strftime("%d-%b-%Y"))
        
    def toString(self):
        print(self.name + ": " + self.date.strftime("%d-%b-%Y"))