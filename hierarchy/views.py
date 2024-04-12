from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout,get_user_model
from .models import *



def login(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=userName, password=password)
        
        if user is not None:
            auth.login(request, user)
            
            if user.role == 'Manager':
                return redirect("Manager")
            elif user.role == 'Team Leader':
                return redirect("Leader")
            elif user.role == 'Developer':
                return redirect("developer_view")
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        # If request method is not POST, render the login page
        return render(request, 'login.html')



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        FN=request.POST.get('first name')
        LN=request.POST.get('Last name')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        role='Manager'

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            User = get_user_model()
            my_user = User.objects.create_user(username=uname, email=email, first_name=FN, last_name=LN, password=pass1, role=role)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def Manager(request):
    return HttpResponse("Welcome, Manager!")

def Leader(request):
    return HttpResponse("Welcome, Team Leader!")

def developer(request):
    return HttpResponse("Welcome, Developer!")
