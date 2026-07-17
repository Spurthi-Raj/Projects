from dataclasses import dataclass
from utils import now,parse_time

@dataclass
class Alarm:
    time:str
    active:bool = True
    def due(self):
        return self.active and now()>=parse_time(self.time)


class AlarmManager:
    def __init__(self):
        self.alarms = []
    def add(self,t):
        self.alarms.append(Alarm(t))
    def remove(self,i):
        self.alarms.pop(i)
