from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.core_view, name='home'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('bibliotecario_dashboard/', views.bibliotecario_dashboard, name='bibliotecario_dashboard'),
    path('gestionar_libros/', views.gestionar_libros, name='gestionar_libros'),
    # path('gestionar_socios/', views.gestionar_socios, name='gestionar_socios'),
    # path('gestionar_prestamos/', views.gestionar_prestamos, name='gestionar_prestamos'),
    # path('socio_dashboard/', views.socio_dashboard, name='socio_dashboard'),
]
