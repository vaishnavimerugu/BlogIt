from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password=forms.CharField(label='Password',widget=forms.PasswordInput())
    firstName=forms.CharField(label='First Name',max_length=30)
    lastName=forms.CharField(label='Last Name',max_length=30)
    email=forms.EmailField(label='Email',max_length=40)

class LoginForm(forms.Form):
    username=forms.CharField(label='Username',max_length=30)
    password=forms.CharField(label='Password',widget=forms.PasswordInput())