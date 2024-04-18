from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login, name='login'), 
    path('signup/', views.SignupPage, name='signup'),
    path('logout/', views.LogoutPage, name='logout_page'),
    path('Manager/', views.Manager, name='Manager'), 
    path('Leader/', views.Leader, name='Leader'), 
    path('developer/', views.developer, name='developer'), 
    path('check-username/', views.check_username, name='check_username'),
    path('add_Leader',views.Add_Team_Leader,name='add_Leader'),
    path('add_developer/<int:pk>/',views.Add_Developer,name='add_developer'),
    path('Show_developer/<int:pk>/',views.Show_Developer,name='Show_developer'),
    path('add_task/<int:pk>/',views.add_task, name='add_task'),
    path('show_task/<int:pk>/',views.show_task, name='show_task'),
    path('update_status/',views.update_status, name='update_status'),
    path('update_Task/', views.update_Task, name='update_Task'),
    path('Create_task/<int:pk>',views.Create_task,name="Create_task"),
    path('Watch_Task/',views.Watch_Task,name='Watch_Task'),
] 
