from django.contrib import admin

from .models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','category')
    list_filter = ['category', 'status']

class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('idnos', 'reg_events')

admin.site.register(EventSchedule)
admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)
