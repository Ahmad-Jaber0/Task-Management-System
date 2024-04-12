from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email','role']



admin.site.register(User,UserAdmin)

