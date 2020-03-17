from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
import datetime

from users.models import *
from notices.models import *
from events.models import Event, EventSchedule, EventRegistration

from users.forms import CustomAuthenticationForm


def home(request):
    schedule = getSchedule()
    notices = Notice.objects.all().order_by('-date_created')[:5]
    reg_events_data = reg_events_titles = profile_data = []
    user = request.user
    if user.is_authenticated:
        reg_events_data, reg_events_titles = getRegEventsIds(user)
        profile_data = Organizer.objects.get(idno=request.user.username) if user.is_staff else Student.objects.get(idno=request.user.username)
    
    all_events = Event.objects.all()
    tech_events = Event.objects.filter(category="technical")
    non_tech_events = Event.objects.filter(category="non-technical")
    

    context = {
        'notices':notices,
        'schedule':schedule,
        'all_events':all_events,
        'tech_events':tech_events,
        'non_tech_events':non_tech_events,
        'reg_events_data':reg_events_data,
        'reg_events_titles':reg_events_titles,
        'profile_data':profile_data,
        }

    return render(request, 'index.html', context)


def getRegEventsIds(user):
    try:
        reg_events_data = EventRegistration.objects.filter(idnos__contains=user.username)
        raw_reg_events_titles = list(EventRegistration.objects.filter(idnos__contains=user.username).values_list('reg_events', flat=True))
        reg_events_titles = []
        for event in raw_reg_events_titles:
            if ',' in event:
                lst = event.split(',')
                for eve in lst:
                    reg_events_titles.append(eve.strip())
                continue
            reg_events_titles.append(event.strip())
        return reg_events_data, reg_events_titles
    except:
        return [],[]

def getSchedule():
    schedule = {}
    today = datetime.datetime.now().date()
    tommorrow = datetime.datetime.now().date()+datetime.timedelta(days=1)
    nextday = datetime.datetime.now().date()+datetime.timedelta(days=2)

    schedule[today] = sorted(EventSchedule.objects.filter(datePlanned=today), key=lambda attrib: attrib.start_time)
    schedule[tommorrow] = sorted(EventSchedule.objects.filter(datePlanned=tommorrow), key=lambda attrib: attrib.start_time)
    schedule[nextday] = sorted(EventSchedule.objects.filter(datePlanned=nextday), key=lambda attrib: attrib.start_time)

    return schedule