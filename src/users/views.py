from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from .forms import *

def organizerRegister(request):
    if request.user.is_authenticated:
        redirect('home');

    if request.method == 'POST':
        form = OrgRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'{username} Account has been created!')
            return redirect('login')
        else:
            messages.error(request, f'Entered details are Invalid!')
            return redirect('org_register')

    form = OrgRegisterForm()
    return render(request, 'users/org_register.html', { 'form':form})

@login_required
def newUserRegistration(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    from .newStudentsReg import studentRegData
    user_data = studentRegData.getNewStudentData() 

    for idno, pswd in user_data.items():
        print(f'Creating user account for {idno}',end=": ")
        if not User.objects.filter(username=idno).exists():
            user=User.objects.create_user(username=idno,password=pswd)
            user.save()
            print('Success')
        else:
            print('Error')
    return redirect('home')

@login_required
def profileUpdate(request):
    user = request.user

    if request.method == 'POST':
        form = OrganizerUpdateForm(request.POST, instance=request.user.organizer) if user.is_staff else StudentUpdateForm(request.POST,instance=request.user.student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile has been updated!')
            return redirect('home')
        else:
            messages.error(request, f'Update request was not acceptable')
            redirect('profile_update')
    else:
        form = OrganizerUpdateForm(instance=request.user.organizer) if user.is_staff else StudentUpdateForm(instance=request.user.student)

    return render(request, 'users/profile_update.html', { "form":form })

class LoginAfterPasswordChangeView(PasswordChangeView):
    @property
    def success_url(self):
        return reverse_lazy('logout')

