from django.contrib import admin

from .models import Event, EventSchedule,EventRegistration

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','category')
    list_filter = ['category', 'status']
    # readonly_fields = ['uploaded_by']

    # def save_model(self, request, obj=None, **kwargs):
    #     obj.uploaded_by = request.user.organizer
    #     obj.save()


class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('idnos', 'reg_events')


admin.site.register(EventSchedule)
admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)
