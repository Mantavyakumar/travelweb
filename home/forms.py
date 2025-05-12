from django import forms
from .models import Contact,Registration

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }


# forms.py
 

# forms.py
from django import forms

# class RegistrationForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email-Id'}))
#     phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone No.', 'id': 'phonenum'}))
#     age = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'Age'}))
    
#     GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
#     gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    
#     departure_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'placeholder': 'Departure Date', 'type': 'datetime-local'}))
#     return_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'placeholder': 'Return Date', 'type': 'datetime-local'}))
    
#     destination_choices = [
#         ('Kashmir', 'Kashmir'), ('Istanbul', 'Istanbul'), ('Paris', 'Paris'),
#         ('Bali', 'Bali'), ('Dubai', 'Dubai'), ('Geneva', 'Geneva'),
#         ('Port Blair', 'Port Blair'), ('Rome', 'Rome')
#     ]
#     destination = forms.MultipleChoiceField(choices=destination_choices, widget=forms.CheckboxSelectMultiple())
    
#     PACKAGE_CHOICES = [('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')]
#     package = forms.ChoiceField(choices=PACKAGE_CHOICES, widget=forms.RadioSelect())
    
#     tnc = forms.BooleanField(required=True, label="I accept the Terms & Conditions.")


# forms.py
from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'departure_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'return_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }