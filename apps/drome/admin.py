from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.unregister(User)
# class CustomUserAdmin(UserAdmin):
# 	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','date_joined', 'last_login')
# admin.site.register(User, CustomUserAdmin) 

admin.site.register(Profile)
admin.site.register(Car)
admin.site.register(Seat)