from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view, custom_logout, alta_socio, edicion_socio, eliminar_socio, gestionar_socios

app_name = 'accounts'

urlpatterns = [
    path("", views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', custom_logout, name = 'logout'),
    path('alta_socio/', alta_socio, name='alta_socio'),
    path('gestionar_socios/', gestionar_socios, name='gestionar_socios'),
    path('edicion_socio/<int:user_id>/', edicion_socio, name='edicion_socio'),
    path('eliminar_socio/<int:user_id>/', eliminar_socio, name='eliminar_socio'),
]
