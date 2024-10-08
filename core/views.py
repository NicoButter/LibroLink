from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from datetime import datetime

@login_required
def core_view(request):
    context = {
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return render(request, 'core/home.html', context)

# BLOQUE PARA BIBLIOTECARIO

@login_required
def bibliotecario_dashboard(request):
    if not request.user.is_bibliotecario:
        raise PermissionDenied
    return render(request, 'core/bibliotecario_dashboard.html')

@login_required
def gestionar_libros(request):
    # Implementar la lógica de gestión de libros o redirigir a la app correspondiente
    return redirect('book_list')

@login_required
def gestionar_socios(request):
    # Aquí iría la lógica para la gestión de socios
    return render(request, 'core/gestionar_socios.html')

@login_required
def gestionar_prestamos(request):
    # Aquí iría la lógica para la gestión de préstamos
    return render(request, 'core/gestionar_prestamos.html')

# BLOQUE PARA SOCIO

@login_required
def socio_dashboard(request):
    if not request.user.is_socio:
        raise PermissionDenied
    return render(request, 'core/socio_dashboard.html')

# BLOQUE PARA EL ADMIN

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        raise PermissionDenied
    return render(request, 'core/admin_dashboard.html')
