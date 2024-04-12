from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    MANAGER = 'manager'
    TEAM_LEADER = 'team_leader'
    DEVELOPER = 'developer'
    ROLE_CHOICES = [
        (MANAGER, 'Manager'),
        (TEAM_LEADER, 'Team Leader'),
        (DEVELOPER, 'Developer'),
    ]
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='supervised_users')



class Task(models.Model):
    task_description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)    