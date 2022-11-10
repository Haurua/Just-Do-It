from django import forms
from .models import JustDoItTasks


class JustDoItForm(forms.ModelForm):
    class Meta:
        model = JustDoItTasks
        fields = [
            "title",
            "description",
            "completed"
        ]

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-title',
                                            'placeholder': 'Enter Task *'}),
            "description": forms.Textarea(attrs={'class': 'form-description',
                                                 'placeholder': 'Enter Task Details'}),
            "completed": forms.CheckboxInput(attrs={'class': 'form-completed'})
        }
