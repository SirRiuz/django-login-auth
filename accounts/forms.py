
# Django imports

from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=250)
    password = forms.CharField(max_length=250)



class RegisterForm(forms.Form):

    name = forms.CharField(max_length=250)
    description = forms.CharField(max_length=250)
    email = forms.EmailField()
    password = forms.CharField(max_length=50)

    imageProfile = forms.ImageField()
    userPage = forms.URLField()




