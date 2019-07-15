from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

'''Se crean 3 formularios para el registro de usuarios, por medio de clases que heredan de
 UserCreationForm, que nos permite extender campos UserRegisterForm que contiene por defecto
 username y password por eso no hace falta definir esos campos aqui. 
 Con UserCreationForm podemos extender ese modulo para agregar campos personalizados'''

#Formulario para registrar un agente
class AgenteRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    user_type = forms.CharField(disabled=True, initial='Agente')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'user_type', 'password1', 'password2']

#Formulario para registrar un gerente
class GerenteRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    user_type = forms.CharField(disabled=True, initial='Gerente')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'user_type', 'password1', 'password2']

#Formulario para registrar un administrador
class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    user_type = forms.CharField(disabled=True, initial='Administrador')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'user_type', 'password1', 'password2']