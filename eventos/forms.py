from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    user_type = forms.CharField(disabled=True, initial='Gerente')
    #user_type.disabled(True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'user_type', 'password1', 'password2']