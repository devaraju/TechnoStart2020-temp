from django.urls import path
from django.contrib.auth import views as auth_views
from . forms import CustomAuthenticationForm

from . import views as user_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html',authentication_form = CustomAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'index.html'), name='logout'),

    path('password-change/', user_views.LoginAfterPasswordChangeView.as_view(template_name="users/pswd_change.html"), name='password_change'),
    # path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/pswd_change_done.html'), name='password_change_done'),
    
    path('profile-update/', user_views.profileUpdate, name="profile_update"),
    
    path('org-register/', user_views.organizerRegister, name="org_register"),

    path('new-students/', user_views.newUserRegistration, name='new_students'),
]