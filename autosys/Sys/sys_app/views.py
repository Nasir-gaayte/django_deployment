
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
# Create your views here.



def home(request):
    return render(request,'sys_app/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f'waryaa {username} waad ku gulaysatay')
            return redirect('home')
    else: 
        form = UserCreationForm()         
    
    return render(request,'sys_app/register.html',{'form':form})

@login_required()
def profile(request):
    return render(request,'sys_app/profile.html')

