from django.urls import path
from . import views

urlpatterns = [
    path('', views.core_view, name='home'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('bibliotecario_dashboard/', views.bibliotecario_dashboard, name='bibliotecario_dashboard'),
    path('socio_dashboard/', views.socio_dashboard, name='socio_dashboard'),
]
