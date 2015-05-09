from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Perfil

# Register your models here.
class personalf(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfil'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (personalf, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)