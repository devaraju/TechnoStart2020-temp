from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Event, EventRegistration
from users.models import Student, Organizer

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
    messages.success(request, f'{user.username} Event registration successful.')

    return redirect('allEvents')

@login_required
def eventRegisterMany(request, users_cnt, eventId):
    usernames = []
    error = f'Great Effort buddy!'
    user = request.user
    if request.user.username ==  request.POST.get('user_1',''):
        error = None
        for cnt in range(2,users_cnt+1):
            try:
                uname = request.POST.get('user_'+str(cnt),'')
                if uname != '':
                    usr = User.objects.get(username=uname)
                    usernames.append(uname)
            except:
                error = f'{uname} not listed in our DB.'
                messages.error(request, error)
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
        messages.success(request, f'{user.username} Event registration successful.')
    else:
        messages.error(request, f'{user.username} Invalid details.')

    return redirect('allEvents')


def allEvents(request):
    profile_data = []
    if request.user.is_authenticated:
        profile_data = Organizer.objects.get(idno=request.user.username) if request.user.is_staff else Student.objects.get(idno=request.user.username)

    if request.method == 'POST':
        title = request.POST.get('title','')
        context1 = {'all_events':list(Event.objects.filter(title__icontains=title)), 'isSearchActive':True,}
    else:
        context1 = {'all_events': Event.objects.all()}

    reg_events_data, reg_events_titles= getRegEventsIds(request.user)
    context = {'reg_events_data':reg_events_data, 'reg_events_titles':reg_events_titles, 'profile_data':profile_data}
    context.update(context1)
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