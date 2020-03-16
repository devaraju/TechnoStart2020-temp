from django.db import models
from django.contrib.auth.forms import User

SECTION_CHOICES = [('sec1','SEC-1'),('sec2','SEC-2'),('sec3','SEC-3'),('sec4','SEC-4')]

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    idno = models.CharField(max_length=7)
    name = models.CharField(max_length=50)
    batch = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'{self.idno}:{self.name}'

class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    idno = models.CharField(max_length=7)
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10, choices=SECTION_CHOICES)
    events = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.idno}:{self.name} ({self.section}) - {self.mobile}'
