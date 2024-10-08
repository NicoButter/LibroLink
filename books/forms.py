from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'ISBN',
            'title',
            'author',
            'publisher',
            'publication_date',
            'genre',
            'language',
            'summary',
            'cover_image',
        ]
