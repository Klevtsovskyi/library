from django import forms

from .models import BookInstance


class BookInstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['due_back', 'status', 'imprint', 'borrower']
