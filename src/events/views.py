from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *
from users.models import *

@login_required
def eventRegister(request, eventId):
    user = request.user

    try:
        eventName = Event.objects.get(id=eventId).title
        reg = EventRegistration.objects.get(idnos=user.username)
        reg.reg_events += ','+eventName
        reg.save()
    except:
        reg = EventRegistration.objects.create(idnos=user.username, reg_events=eventName)
    return redirect('home')

@login_required
def eventRegisterMany(request, users_cnt, eventId):
    usernames = []
    error = f'Great Effort buddy!'

    if request.user.username ==  request.POST.get('user_1',''):
        error = None
        for cnt in range(2,users_cnt+1):
            try:
                uname = request.POST.get('user_'+str(cnt),'')
                if uname is not '':
                    usr = User.objects.get(username=uname)
                    usernames.append(uname)
            except:
                error = f'------>User-{uname} not listed in our DB.'
                break


    if error is None and len(usernames)!=0:
        # usernames = sorted(usernames)
        usernames = ','.join(usernames)
        try:
            eventName = Event.objects.get(id=eventId).title
            reg = EventRegistration.objects.get(idnos=usernames)
            reg.reg_events += ','+eventName
            # reg.save()
        except:
            reg = EventRegistration.objects.create(idnos=usernames, reg_events=eventName)
            # reg.save()
    return redirect('home')


def allEvents(request):
    all_events = Event.objects.all()

    reg_events_data, reg_events_titles= getRegEventsIds(request.user)
    context = {
        'reg_events_data':reg_events_data,
        'reg_events_titles':reg_events_titles,
        'all_events':all_events,
    }

    return render(request,'events/events.html', context)

def getRegEventsIds(user):
    try:
        reg_events_data = EventRegistration.objects.filter(idnos__contains=user.username)
        raw_reg_events_titles= list(EventRegistration.objects.filter(idnos__contains=user.username).values_list('reg_events', flat=True))
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