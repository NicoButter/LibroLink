from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Ajusta esto según la URL de tu dashboard
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect(reverse('login'))
