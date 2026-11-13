from .models import Book
from django.forms import ModelForm
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','price', 'description', 'stock', 'category']
