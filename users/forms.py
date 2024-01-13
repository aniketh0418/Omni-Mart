# forms.py
from django import forms
from shop.models import Product, Category
from django.forms import ModelForm, inlineformset_factory, formset_factory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'slug', 'name', 'image', 'description', 'price', 'available']
        widgets = {
            'name':forms.Textarea(attrs={'place holder': 'Name of the Product', 'style': 'font-size: 16px; font-weight: 500; width: 70%; height: 25px; padding:6px;'}),
            'description':forms.Textarea(attrs={'placeholder': 'Description ', 'style': 'font-size: 16px; font-weight: 500; width: 70%; height: 25px;padding:6px;'}),
            'price':forms.Textarea(attrs={'placeholder': 'Price', 'style': 'font-size: 16px; font-weight: 500; width: 30%; height: 25px;padding:3px;'}),
            
        }
    
Productformset = formset_factory(form=ProductForm, extra=1)

class LoginForm(AuthenticationForm):
    # You can customize the form if needed
    class Meta:
        model = User  # Assuming you have a User model
        fields = ['username', 'password']
        widgets = {
            'name':forms.Textarea(attrs={'place holder': 'Name of the Product', 'style': 'font-size: 16px; font-weight: 500; width: 70%; height: 25px; padding:6px;'}),
            'password':forms.Textarea(attrs={'placeholder': 'Description ', 'style': 'font-size: 16px; font-weight: 500; width: 70%; height: 25px;padding:6px;'}),
            
            
        }
Userformset = formset_factory(form=LoginForm, extra=1)


class ProductUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Product Name', 'style': 'font-size: 16px; font-weight: 500;  color: black; margin-bottom:12px; border-radius:4px;padding:4px;'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter Product Description', 'style': 'font-size: 16px; font-weight: 500;  color: black; margin-bottom:12px; border-radius:4px;padding:4px; width:90%;'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Product Price', 'style': 'font-size: 16px; font-weight: 500;  color: black; margin-bottom:12px; border-radius:4px;padding:4px;'}))
    available = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style': 'margin-bottom:12px;'}), required=False)
    vendor = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'style': 'font-size: 16px; font-weight: 500;  color: black; margin-bottom:12px; border-radius:4px;padding:4px;'}))

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available', 'vendor']