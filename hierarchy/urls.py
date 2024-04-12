from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'), 
    path('signup/', views.SignupPage, name='signup'),
    path('Manager/', views.Manager, name='Manager'), 
    path('Leader/', views.Leader, name='Leader'), 
    path('developer/', views.developer, name='developer'), 

] 
