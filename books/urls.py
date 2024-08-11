from django.urls import path
from . import views

app_name = 'books' 

urlpatterns = [
    path('gestionar/', views.gestionar_libros, name='gestionar_libros'),
    path('add/', views.add_book, name='add_book'),
    path('list/', views.book_list, name='book_list'),
]
