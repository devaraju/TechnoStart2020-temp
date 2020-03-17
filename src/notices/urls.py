from django.urls import path

from .views import allNotices

urlpatterns = [
    path('', allNotices, name="allNotices"),
]
