from modules.Data import Data
from ics import Calendar, Event

class ICS(Data):
   def __init__(self, title, Events):
       super().__init__(title, Events)
       
   def writeICS(self):
       calendar = Calendar()
       for event in self.Events:
            e = Event()
            e.name = self.title +" - " +event.name
            e.begin = event.date
            e.make_all_day()
            calendar.events.add(e)
            calendar.events
       with open(self.title, 'w') as f:
            f.write(str(calendar))
       f.close()
       