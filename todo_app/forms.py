from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=10,
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Title',
                                                          'class': 'form-control',
                                                          })
                            )
    description = forms.CharField(max_length=50,
                                  required=False,
                                  widget=forms.TextInput(attrs={'placeholder': 'Description',
                                                                'class': 'form-control',
                                                                })
                                  )
    due_date = forms.DateField(required=True,
                               widget=forms.DateInput(attrs={'class': 'form-control'}))
    status = forms.BooleanField(required=False)

    class Meta:
        model = Tasks
        fields = ['title', 'description', 'due_date', 'status']
