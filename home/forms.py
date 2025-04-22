from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone No.")
    age = forms.IntegerField(label="Age")
    
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    
    departuredate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    returndate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    DESTINATIONS = [
        ('kashmir', 'Kashmir'),
        ('istanbul', 'Istanbul'),
        ('paris', 'Paris'),
        ('bali', 'Bali'),
        ('dubai', 'Dubai'),
        ('geneva', 'Geneva'),
        ('port_blair', 'Port Blair'),
        ('rome', 'Rome'),
    ]
    td = forms.MultipleChoiceField(choices=DESTINATIONS, widget=forms.CheckboxSelectMultiple, label="Travel Destination")
    
    PACKAGE_CHOICES = [('bronze', 'Bronze'), ('silver', 'Silver'), ('gold', 'Gold'), ('platinum', 'Platinum')]
    locations = forms.ChoiceField(choices=PACKAGE_CHOICES, widget=forms.RadioSelect, label="Package")
    
    tnc = forms.BooleanField(label="I accept the Terms & Conditions")
 

 