# This file contains the URL patterns for the bookstore app
# Import relevant modules
from django.urls import path
from . import views
from .views import book_list, add_book, update_book, delete_book, search_books, create_book

# Define a list of URL patterns for the bookstore app
urlpatterns = [
    path('', book_list, name='book_list'),
    path('add/', add_book, name='add_book'),
    path('update/<int:pk>/', update_book, name='update_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),
    path('search/', search_books, name='search_books'),
    path('create/', create_book, name='create_book'),
]