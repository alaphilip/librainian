from django import forms
from django.db import models

# Create your models here.

class Book(models.Model):
# Define the fields for the book model
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    qty = models.IntegerField()
    spine_colour = models.CharField(max_length=100)
# Define the condition choices for the book model
    CONDITION_CHOICES = [    ('Poor', 'Poor - annotations, dirt, or other wear'),    ('Average', 'Average - significant scuffing'),    ('Good', 'Good - minimal scuffing'),    ('Very Good', 'Very Good - very minor signs of shelf wear, nothing more'),    ('Like New', 'Like New - no visible signs of wear'),]
    spine_colour = models.CharField(max_length=100, blank=True)
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=20, default='Good')

# Define the string representation of a Book object
    def __str__(self):
        return self.title

class BookForm(forms.ModelForm):
# Define the meta data for the BookForm model
    class Meta:
        model = Book
        fields = ['title', 'author', 'qty', 'spine_colour', 'condition']
