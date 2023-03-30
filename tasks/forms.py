from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'No. medidor',
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Ejemplo: 18.5167, -70.0167',
        'rows': 5,
    }))

    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')
