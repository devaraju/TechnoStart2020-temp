from django.urls import path

from .views import *

urlpatterns = [
	path('<int:id>', noticeDetail, name="noticeDetail"),
    path('', allNotices, name="allNotices"),

]
