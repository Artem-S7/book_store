from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('categories/all/', views.category_all, name = 'category_all'),
    path('categories/<slug:slug>/', views.category_detail, name = 'category_detail'),
    path('books/add/', views.BookCreateView.as_view(), name='book_add'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    ]