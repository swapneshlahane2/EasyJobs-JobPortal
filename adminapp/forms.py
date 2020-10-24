from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True,)
    email = forms.EmailField(max_length=30, help_text="Required a valid email address")
    # password1=forms.CharField(max_length=30 ,help_text="Required a valid email address")

    class Meta:
        model = User
        fields=['name',"username", "password1","password2" ,'email']
