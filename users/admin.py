#Mostrando nosso usuário
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

