# Import relevant modules
from django import forms
from .models import Book

# Define a custom BookForm class, that extends forms.ModelForm
class BookForm(forms.ModelForm):
# Add the condition field to the form, using the choices from the Book model
    condition = forms.ChoiceField(choices=Book.CONDITION_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
# Specify which fields should be displayed on the form
    class Meta:
        model = Book
        fields = ['title', 'author', 'qty', 'spine_colour', 'condition']
# Specify the widgets to use for the spine_colour field, customising its appearance
        widgets = {'spine_colour': forms.TextInput(attrs={'class': 'form-control'})}
