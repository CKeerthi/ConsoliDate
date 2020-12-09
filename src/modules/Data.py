class Data:
    
    def __init__(self, title, Events):
        self.title = title
        self.Events = Events
    
    def getTitle(self):
        return self.title
    
    def setTitle(self, title):
        self.title = title