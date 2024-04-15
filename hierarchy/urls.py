from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login, name='login'), 
    path('signup/', views.SignupPage, name='signup'),
    path('logout_page/', LogoutView.as_view(), name='logout_page'), 
    path('Manager/', views.Manager, name='Manager'), 
    path('Leader/', views.Leader, name='Leader'), 
    path('developer/', views.developer, name='developer'), 
    path('check-username/', views.check_username, name='check_username'),

] 
