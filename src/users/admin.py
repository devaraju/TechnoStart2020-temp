from django.contrib import admin

from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ('idno','name','batch','section')
    list_filter = ['batch', 'section']

admin.site.register(Student, StudentAdmin)
admin.site.register(Organizer)
