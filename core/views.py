from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def core_view(request):
    context = {
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Aquí puedes agregar más contexto según sea necesario
    }
    return render(request, 'core/home.html', context)
