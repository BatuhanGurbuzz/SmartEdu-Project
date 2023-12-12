from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    firstName = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'First Name'
    }))

    lastName = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Last Name'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Your Email'
    }))
    
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Your Phone'
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Give us more details..'
    }))

    class Meta:
        model = Contact
        fields = ['firstName', 'lastName', 'email', 'phone', 'message']
