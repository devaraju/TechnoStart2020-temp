from django.urls import path

from .views import *

urlpatterns = [
    path('', allEvents,name="allEvents"),

    path('<int:eventId>/register/', eventRegister,name="eventRegister"),
    path('<int:eventId>/<int:users_cnt>registermany/', eventRegisterMany,name="eventRegisterMany"),
]

