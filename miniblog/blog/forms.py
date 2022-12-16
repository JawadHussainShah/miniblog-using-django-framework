import imp
from re import I
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post

class SignupForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Confirm Passowrd')
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']
        labels = {'email':'Email'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            '':forms.TextInput(attrs={'class':'form-control'})
        }
    
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs=
    {'autofocus':'true','class':'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))     

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc']
        labels = {'desc':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        'desc':forms.Textarea(attrs={'class':'form-control'})}