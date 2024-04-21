from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponse,HttpResponseForbidden,JsonResponse
from django.contrib.auth import authenticate,login,logout,get_user_model
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
import json

        
def home(request):
    return render(request, 'home.html')

def Sortable(request):

    return render (request,"sortable.html")

def task_data(request):
    tasks = Task.objects.all()
    data = []
    for task in tasks:
        data.append({
            'id': task.id,
            'name': task.name,
            'task_description': task.task_description,
            'assigned_to': task.assigned_to.username,
            'status': task.status,
            'approved': task.approved
        })

    return JsonResponse(data, safe=False)

def user_data(request):
    users = User.objects.all()
    data = []
    for user in users:
        user_dict = {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'role': user.role,
            'supervisor': user.supervisor.username if user.supervisor else None  
        }
        
        data.append(user_dict)
    return JsonResponse(data, safe=False)

def check_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'is_taken': True})
        else:
            return JsonResponse({'is_taken': False})
        
def update_Task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task_id = data.get('task_id')
        status = data.get('status')
        
        try:
            task = Task.objects.get(pk=task_id)
            if status == 'apply':
                    task.approved = True
                    task.save()
            elif status == 'reject':
                task.delete()
            return JsonResponse({'message': 'Task updated successfully'}, status=200)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def update_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task_id = data.get('task_id')
        status = data.get('status')
        
        try:
            task = Task.objects.get(pk=task_id)
            task.status = status
            task.save()
            return JsonResponse({'message': 'Status updated successfully'}, status=200)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)        


def login(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=userName, password=password)
        
        if user is not None:
            auth.login(request, user)
            print(user.role)
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

@login_required
def LogoutPage(request):
    logout(request)
    return redirect('home')


@login_required
def Manager(request):
    if request.user.role == 'Manager':
        queryset = Task.objects.filter(assigned_to=request.user)
        return render(request,'Manager.html',{'tasks':queryset})

    else:
        return render(request,'permission.html')
    
@login_required
def View_members(request):
    if request.user.role == 'Manager':
        queryset = User.objects.filter(supervisor=request.user)

        return render(request, 'View_members.html',{'Leaders':queryset,'pk':request.user.id})
    else:
        return render(request,'permission.html')

@login_required    
def Add_Team_Leader(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        FN = request.POST.get('firstname')
        LN = request.POST.get('lastname')
        pass1 = request.POST.get('password')
        role = 'Team Leader'

        supervisor_username = request.user

        if User.objects.filter(username=uname).exists() or User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Username or email already exists'}, status=400)
        else:
            my_user = User.objects.create_user(username=uname, email=email, first_name=FN, last_name=LN, password=pass1, role=role, supervisor=supervisor_username)
            return redirect('Manager') 
    else:
        return render(request, 'add_leader.html')


@login_required 
def Add_Developer(request,pk):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        FN = request.POST.get('firstname')
        LN = request.POST.get('lastname')
        pass1 = request.POST.get('password')
        role = 'Developer'
        x=User.objects.get(pk=pk)
        supervisor_username = x

        if User.objects.filter(username=uname).exists():
            pass
        else:
            my_user = User.objects.create_user(username=uname, email=email, first_name=FN, last_name=LN, password=pass1, role=role, supervisor=supervisor_username)
            return redirect('Manager')

    else:
        return render(request, 'add_developer.html')    

@login_required
def Show_Developer(request,pk):
    x=User.objects.get(pk=pk)
    queryset = User.objects.filter(supervisor=x)
    return render(request,'show_developer.html',{'developers':queryset,'pk':pk,'role':request.user.role}) 

@login_required
def add_task(request,pk):
    if request.method=='POST':
        name=request.POST.get('Name')
        description=request.POST.get('task_description')
        assigned_to = User.objects.get(pk=pk)
        print(assigned_to)
        status='In Progress'
        my_user = Task.objects.create(name=name, task_description=description, assigned_to=assigned_to, status=status,approved=True)
        if request.user.role =='Manager':
            return redirect('Manager')
        return redirect('Leader')
        
        
    return render(request,'add_task.html')      

@login_required
def show_task(request,pk):
    x=User.objects.get(pk=pk)
    queryset = Task.objects.filter(assigned_to=x)
    return render(request,'show_task.html',{'tasks':queryset,'pk':pk}) 

@login_required
def Create_task(request):

    if request.method=='POST':
        name=request.POST.get('Name')
        description=request.POST.get('task_description')
        assigned_to = request.user
        status='In Progress' 
        if request.user.role=='Manager':
            my_user = Task.objects.create(name=name, task_description=description, assigned_to=assigned_to, status=status,approved=True)
            return redirect('Manager')
                
        my_user = Task.objects.create(name=name, task_description=description, assigned_to=assigned_to, status=status)        
        if request.user.role == 'Team Leader':
            return redirect('Leader')
        
        return redirect('developer')
        
        
    return render(request,'add_task.html') 

@login_required
def Watch_Task(request):

    my_user = request.user
    if my_user.role == 'Team Leader':
        team_members = User.objects.filter(supervisor=my_user)
        tasks = Task.objects.filter(assigned_to__in=team_members)
    else:
        tasks = Task.objects.all()

    return render(request, 'watch_task.html', {'tasks': tasks,'role': my_user.role})



@login_required
def Leader(request):
    if request.user.role=='Team Leader':
        queryset = Task.objects.filter(assigned_to=request.user)
        return render(request,'Leader.html',{'tasks':queryset,'pk':request.user.id,'role':request.user.role}) 
    else:
        return render(request,'permission.html')
    
@login_required
def developer(request):
    if request.user.role=='Developer':
        queryset = Task.objects.filter(assigned_to=request.user)
        return render(request,'Leader.html',{'tasks':queryset,'pk':request.user.id}) 
    else:
        return render(request,'permission.html')

