from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.auth import urls as auth_urls

from .views import *

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home, name="home"),
    path('ts/', home, name="home"),
    path('ts/notice/', include('notices.urls')),
    path('ts/user/', include('users.urls')),
    path('ts/event/', include('events.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)