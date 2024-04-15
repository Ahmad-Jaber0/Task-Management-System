from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email','role']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_description','assigned_to','status']

admin.site.register(User,UserAdmin)
admin.site.register(Task,TaskAdmin)


