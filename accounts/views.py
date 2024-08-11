import io
import qrcode

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.files.base import ContentFile
from django.db.models import Q 

from .forms import CustomAuthenticationForm, CustomUserCreationForm

from .models import CustomUser, Socio


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

def custom_logout(request):
    logout(request)
    return redirect(reverse('accounts:login'))

def redirect_user(user):
    if user.is_admin:
        return redirect('admin_dashboard')  # La vista de admin -> estar en `core`
    elif user.is_bibliotecario:
        return redirect('core:bibliotecario_dashboard')
    elif user.is_socio:
        return redirect('socio_dashboard')
    else:
        return redirect('login')
    
# VISTAS PARA LA GESTION DE USUARIOS

def gestionar_socios(request):
    query = request.GET.get('q')
    socios = Socio.objects.all()

    if query:
        socios = socios.filter(
            Q(user__username__icontains=query) |
            Q(user__email__icontains=query) |
            Q(carnet__numero__icontains=query)
        )

    return render(request, 'accounts/gestionar_socios.html', {'socios': socios})


@login_required
def alta_socio(request):
    User = get_user_model()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = request.user
            user.save()

            # Generar QR y carné
            qr_data = f'ID: {user.id}, Username: {user.username}'
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(qr_data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')

            # Guardar imagen del QR en un archivo
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            file_name = f'qr_{user.id}.png'
            user.qr_code.save(file_name, ContentFile(buffer.getvalue()), save=True)

            return redirect('accounts:gestionar_usuarios')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/alta_socio.html', {'form': form})

@login_required
def edicion_socio(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:gestionar_usuarios')
    else:
        form = CustomUserCreationForm(instance=user)

    return render(request, 'accounts/edicion_socio.html', {'form': form})

@login_required
def eliminar_socio(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        user.delete()
        return redirect('accounts:gestionar_usuarios')
    
    return render(request, 'accounts/eliminar_socio.html', {'user': user})
