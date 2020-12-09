from modules.Data import Data
from functions.rawDataFunctions import getText, textAlgorithm, getTitle


class RawData(Data):
   def __init__(self, title, textData, path):
       super().__init__(title, path)
       self.textData = textData
       self.path = path
      
   def converToText(self):
       self.textData = getText(self.path)
       
   def mineDueDates(self):
       self.Events = textAlgorithm(self.textData)
       
   def getTitlefromData(self):
       self.title = getTitle(self.textData)