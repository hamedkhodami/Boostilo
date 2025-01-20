from django import forms
from .models import ContactModel

class ContactUsForms(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['fullname', 'email']
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-3 py-3 focus:outline-none rounded-full bg-[#9482ad] sm:text-sm',
                'placeholder': 'Full name...'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'mt-1 block w-full px-3 py-3 focus:outline-none rounded-full bg-[#9482ad] sm:text-sm',
                'placeholder': 'Email...'
            }),
        }
