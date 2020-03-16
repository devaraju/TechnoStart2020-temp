from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages

from .forms import *

def organizerRegister(request):
    if request.user.is_authenticated:
        redirect('home');

    if request.method == 'POST':
        form = OrgRegisterForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = OrgRegisterForm()
        return render(request, 'users/org_register.html', { 'form':form})


# @login_required
# def profileUpdate(request):
#     user = request.user

#     if request.method == 'POST':
#         form = OrganizerUpdateForm(request.POST, instance=request.user.organizer) if user.is_staff else StudentUpdateForm(request.POST,instance=request.user.student)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Profile has been updated!')
#             return redirect('home')
#     else:
#         form = OrganizerUpdateForm(instance=request.user.organizer) if user.is_staff else StudentUpdateForm(instance=request.user.student)

#     return render(request, 'users/profile.html', { "form":form })
