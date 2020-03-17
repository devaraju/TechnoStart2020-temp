from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

event_types = [('technical','TECHNICAL'), ('non-technical','NON-TECHNICAL')]
class Event(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    status = models.CharField(max_length=50, blank=True)
    cover = models.ImageField(upload_to='event_covers/', default='event_covers/default.jpg')
    category = models.CharField(max_length=20, choices=event_types)
    rules = models.TextField()
    no_of_participants = models.IntegerField()
    organizers = models.TextField()
    winners = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}'

class EventRegistration(models.Model):
    idnos = models.TextField()
    reg_events = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

class EventSchedule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    round_no = models.IntegerField()
    slot_no = models.IntegerField()
    datePlanned = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (("event", "round_no"),)

    @property
    def isCompleted(self):
        if datetime.now().date() == self.datePlanned:
            return self.end_time < datetime.now().time()
        return False

    @property
    def isLive(self):
        if datetime.now().date() == self.datePlanned:
            return (self.start_time < datetime.now().time()) & (datetime.now().time() < self.end_time) 
        return False

    def __str__(self):
        return f'{self.event.title}:Round-{self.round_no}:Slot-{self.slot_no}'