from django import forms
from .models import AutoProizvodjac, AutoModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class AutoProizvodjacModelForm(forms.ModelForm):
	class Meta:
		model = AutoProizvodjac
		widgets = {
            'ime': forms.TextInput(attrs={'class':'form-control','placeholder':'Ime'}),
            'web_stranica': forms.TextInput(attrs={'class':'form-control','placeholder':'Web stranica'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email adresa'}),
            'logo': forms.TextInput(attrs={'class':'form-control','placeholder':'Logo'}),
        }
		fields = ['ime', 'web_stranica', 'email','logo']
		

class AutoModelModelForm(forms.ModelForm):
	class Meta:
		model = AutoModel
		widgets = {
            'tip': forms.TextInput(attrs={'class':'form-control','placeholder':'Model'}),
            'verzija': forms.NumberInput(attrs={'class':'form-control','placeholder':'Verzija'}),
            'godina_proizvodnje': forms.DateInput(attrs={'class':'form-control','placeholder':'Godina proizvodnje'}),
            'slika': forms.TextInput(attrs={'class':'form-control','placeholder':'Slika'}),
            'automobili': forms.Select(attrs={'class':'form-control'}),
        }

		fields = ['tip','verzija','godina_proizvodnje','automobili','slika']