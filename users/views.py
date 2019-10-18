from django.shortcuts import render, redirect
from .models import CustomUser
from data_entry.models import OwnerInfo

def login(request):
    return render(request, 'users/login.html')

def login_success(request):
        return redirect("/owner")