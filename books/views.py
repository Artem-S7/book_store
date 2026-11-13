from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Category
from django.urls import reverse, reverse_lazy

# def home(request):
#     return render(request, 'books/home.html')


# from django.http import HttpResponse
# def home(request):
#     return HttpResponse('Книжковий магазин')

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)
    context = {'category': category, 'books': books}
    return render(request, 'books/category_detail.html', context)

def category_all(request):
    categories = Category.objects.prefetch_related('book_set')
    context = {'categories': categories}
    return render(request, 'books/category_all.html', context)

class BookListView(ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'books'
    paginate_by = 3
    def get_queryset(self):
        book_list = Book.objects.all()
        book_category = self.request.GET.get('category')
        book_search = self.request.GET.get('search')
        if book_search:
            book_list = book_list.filter(title__icontains=book_search)
        if book_category:
            book_list = book_list.filter(category__slug=book_category)
        return book_list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_add.html'
    fields = ['title', 'author', 'price', 'description', 'stock', 'category']
    def get_success_url(self):
        return reverse('books:book_detail', kwargs={'pk': self.object.pk})

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ['title', 'author', 'price', 'description', 'stock', 'category']
    def get_success_url(self):
        return reverse('books:book_detail', kwargs={'pk': self.object.pk})
            
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books:home')

# Create your views here.

