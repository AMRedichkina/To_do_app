from django import forms
from .models import TodoListItem


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoListItem
        fields = ['content', 'completed']
