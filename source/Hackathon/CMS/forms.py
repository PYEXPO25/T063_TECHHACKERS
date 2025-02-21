from django import forms
from .models import User, Complaint
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Form for login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

# Form for sign-up
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

# Form for submitting complaints
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint_text']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    pass
