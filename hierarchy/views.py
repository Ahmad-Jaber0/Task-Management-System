from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponse,HttpResponseForbidden,JsonResponse
from django.contrib.auth import authenticate,login,logout,get_user_model
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

        
def home(request):
    return render(request, 'home.html')

def check_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'is_taken': True})
        else:
            return JsonResponse({'is_taken': False})

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
                return redirect("developer")
            else:
                return JsonResponse({'success': False, 'message': 'Invalid Role'}, status=400)

        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password'}, status=400)

    else:
        return render(request, 'login.html')



def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        FN = request.POST.get('first name')
        LN = request.POST.get('Last name')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        role = 'Manager'

        
        if User.objects.filter(username=uname).exists():
            error_message = "Username already exists. Please choose a different username."
            return render(request, 'signup.html', {'error_message': error_message})
        else:
            my_user = User.objects.create_user(username=uname, email=email, first_name=FN, last_name=LN, password=pass1, role=role)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LogoutPage(request):
    print("Logging out user...")
    logout(request)
    print("User logged out successfully.")
    return redirect('home')


@login_required
def Manager(request):
    if request.user.role == 'Manager':
        return render(request, 'Manager.html')
    else:
        return HttpResponseForbidden("You don't have permission to access this page.")

def Leader(request):
    return HttpResponse("Welcome, Team Leader!")

def developer(request):
    return HttpResponse("Welcome, Developer!")


