from django.urls import path
from django.contrib.auth import views as auth_views
from . forms import CustomAuthenticationForm

from . import views as user_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html',authentication_form = CustomAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'index.html'), name='logout'),
    path('org_register/', user_views.organizerRegister, name="org-register"),

    # path('profile/', user_views.profileUpdate, name="profileUpdate"),

]