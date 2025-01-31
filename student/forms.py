from django import forms
from django.contrib.auth.forms import UserCreationForm
from instructor.models import User

class StudentCreateForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","email"]

    def __init__(self, *args, **kwargs):
        super(StudentCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class StudentLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()