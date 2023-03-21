# Import the admin and Book modules
from django.contrib import admin
from .models import Book

# Define a custom BookAdmin class
class BookAdmin(admin.ModelAdmin):
# Specify which fields that should be displayed on the admin edit page for a Book object
    fields = ('id', 'title', 'author', 'qty', 'spine_colour', 'condition')
# Specify that the id field should be read-only
    readonly_fields = ('id',)

# Register the Book model with the admin site, using the custom admin class
admin.site.register(Book, BookAdmin)