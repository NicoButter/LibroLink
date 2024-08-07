from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from datetime import datetime

@login_required
def core_view(request):
    context = {
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return render(request, 'core/home.html', context)

@login_required
def bibliotecario_dashboard(request):
    if not request.user.is_bibliotecario:
        raise PermissionDenied
    return render(request, 'core/bibliotecario_dashboard.html')

@login_required
def socio_dashboard(request):
    if not request.user.is_socio:
        raise PermissionDenied
    return render(request, 'core/socio_dashboard.html')

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        raise PermissionDenied
    return render(request, 'core/admin_dashboard.html')
