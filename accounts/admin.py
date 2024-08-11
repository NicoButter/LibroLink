from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm

class CustomUserAdmin(DefaultUserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    fieldsets = DefaultUserAdmin.fieldsets + (
        (None, {'fields': ('dni', 'is_admin', 'is_bibliotecario', 'is_socio')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'dni', 'password1', 'password2', 'is_admin', 'is_bibliotecario', 'is_socio'),
        }),
    )

    list_display = ('username', 'email', 'dni', 'is_admin', 'is_bibliotecario', 'is_socio')
    search_fields = ('username', 'email', 'dni')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
