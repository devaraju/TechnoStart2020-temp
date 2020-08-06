from django.shortcuts import render, redirect

from .models import Notice
from users.models import Student, Organizer
from events.models import Event, EventRegistration


def allNotices(request):
    profile_data = []
    if request.user.is_authenticated:
        profile_data = Organizer.objects.get(idno=request.user.username) if request.user.is_staff else Student.objects.get(idno=request.user.username)
    reg_events_data, reg_events_titles= getRegEventsIds(request.user)

    notices = Notice.objects.all().order_by('-date_created')
    
    # paginator = Paginator(notices, 2)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {
        'notices':notices,
        'profile_data':profile_data,
        'reg_events_data':reg_events_data,
        'reg_events_titles':reg_events_titles
    }

    return render(request,'notices.html', context)

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