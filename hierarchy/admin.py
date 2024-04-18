from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email','role','supervisor','id']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_description','assigned_to','status','Manager_approved','Leader_approved']

admin.site.register(User,UserAdmin)
admin.site.register(Task,TaskAdmin)


