from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from authyy.models import Product


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


from django import forms


class ContactUs(forms.Form):
    from_email = forms.EmailField(required=True)

    subject = forms.CharField(required=True)

    message = forms.CharField(widget=forms.Textarea, required=True)