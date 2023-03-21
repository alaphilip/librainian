# Import relevant modules
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# View to display a list of all books and search books by title
def book_list(request):
    books = Book.objects.all()
    query = request.GET.get('q')
# Filter books by title if there is a search query
    if query:
        books = books.filter(title__icontains=query)
# Render the book list template with the list of books
    return render(request, 'bookstore/book_list.html', {'books': books})

# View to add a new book   
def add_book(request):
# If the request method is POST, process the form data
    if request.method == "POST":
        form = BookForm(request.POST)
# If the form data is valid, save the data to the database and redirect to the book list page
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
# If the request method is GET, show the form
        form = BookForm()
    return render(request, 'bookstore/book_form.html', {'form': form})

# View to create a new book
# This is the same as the add_book view, but uses a different template
# Having two endpoints allows expansion of the program in the future
# create_book will be used for adding additional book information
# add_book will be used for bulk adding books
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookstore/book_form.html', {'form': form})

# View to update an existing book
def update_book(request, pk):
# Get the book with the given pk
    book = get_object_or_404(Book, pk=pk)
# If the request method is POST, process the form data
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
# If the form data is valid, save the data to the database and redirect to the book list page
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
# If the request method is GET, show the form with the current book data
        form = BookForm(instance=book)
    return render(request, 'bookstore/book_form.html', {'form': form})

# View to delete an existing book
def delete_book(request, pk):
# Get the book with the given pk
    book = get_object_or_404(Book, pk=pk)
# Delete the book
    book.delete()
# Redirect to the book list page
    return redirect('book_list')

# View to search books by title
def search_books(request):
# Get the search query
    query = request.GET.get('q', '')
# Filter books by title if there is a search query
    books = Book.objects.filter(title__icontains=query)
# Render the book list template with the list of books
    return render(request, 'bookstore/book_list.html', {'books': books})