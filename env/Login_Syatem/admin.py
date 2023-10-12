from django.contrib import admin
from .models import Login_User

# Register your models here.
@admin.register(Login_User)
class Admin_User(admin.ModelAdmin):
    list_display=['first_name','last_name','email','password','phone_no']