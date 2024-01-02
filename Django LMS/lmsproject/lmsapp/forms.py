from django import forms
from .models import Book
from django.contrib.auth.models import User

class BookSelectionForm(forms.Form):
    book_choices = [(book.id, book.title) for book in Book.objects.all()]
    selected_book = forms.ChoiceField(choices=book_choices)



class BookIssueForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())

