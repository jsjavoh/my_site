from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-name',
                'placeholder': 'Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-email',
                'placeholder': 'Email',
            }),
            'message': forms.Textarea(attrs={  # Textarea ga o'zgartirildi
                'class': 'form-message',
                'placeholder': 'Message',
                'rows': 4,  # Ixtiyoriy: matn maydonining balandligini belgilash
            }),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance