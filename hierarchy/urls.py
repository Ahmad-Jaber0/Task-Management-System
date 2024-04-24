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
    path('add_Leader',views.Add_Team_Leader,name='add_Leader'),
    path('add_developer/<int:pk>/',views.Add_Developer,name='add_developer'),
    path('Show_developer/<int:pk>/',views.Show_Developer,name='Show_developer'),
    path('add_task/<int:pk>/',views.add_task, name='add_task'),
    path('show_task/<int:pk>/',views.show_task, name='show_task'),
    path('update_status/',views.update_status, name='update_status'),
    path('update_Task/', views.update_Task, name='update_Task'),
    path('Create_task/',views.Create_task,name="Create_task"),
    path('Watch_Task/',views.Watch_Task,name='Watch_Task'),
    path('sortable/',views.Sortable,name='sortable'),
    path('task_data/', views.task_data, name='task_data'),
    path('user_data/', views.user_data, name='user_data'),
    path('View_members/',views.View_members,name='View_members'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('MyAccount/',views.MyAccount,name='MyAccount'),


] 
