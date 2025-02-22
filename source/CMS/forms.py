from django import forms
from .models import User, Complaints, PersonalInfo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
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

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    pass

class PersonalInfoForm(forms.ModelForm):
    phone = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{10}$', message="Enter a valid 10-digit phone number")]
    )

    class Meta:
        model = PersonalInfo
        fields = ['full_name', 'phone', 'email', 'gender', 'address']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ['category', 'description', 'location', 'attachment']

