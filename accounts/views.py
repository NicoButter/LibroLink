from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CustomAuthenticationForm
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect_user(user)
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def redirect_user(user):
    if user.is_admin:
        return redirect('admin_dashboard')  # La vista de admin -> estar en `core`
    elif user.is_bibliotecario:
        return redirect('bibliotecario_dashboard')
    elif user.is_socio:
        return redirect('socio_dashboard')
    else:
        return redirect('login')
    
