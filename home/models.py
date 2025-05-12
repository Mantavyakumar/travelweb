from django.db import models

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name


# # Registration Model
# class Registration(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     age = models.IntegerField()

#     GENDER_CHOICES = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     ]
#     gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

#     departure_date = models.DateTimeField()
#     return_date = models.DateTimeField()

#     DESTINATION_CHOICES = [
#         ('Kashmir', 'Kashmir'),
#         ('Istanbul', 'Istanbul'),
#         ('Paris', 'Paris'),
#         ('Bali', 'Bali'),
#         ('Dubai', 'Dubai'),
#         ('Geneva', 'Geneva'),
#         ('Port Blair', 'Port Blair'),
#         ('Rome', 'Rome'),
#     ]
#     destination = models.CharField(max_length=100, choices=DESTINATION_CHOICES)

#     PACKAGE_CHOICES = [
#         ('Bronze', 'Bronze'),
#         ('Silver', 'Silver'),
#         ('Gold', 'Gold'),
#         ('Platinum', 'Platinum'),
#     ]
#     package = models.CharField(max_length=8, choices=PACKAGE_CHOICES)

#     tnc = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.name} - {self.destination} - {self.email}"


# models.py
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    departure_date = models.DateTimeField()
    return_date = models.DateTimeField()
    destination = models.CharField(max_length=100)
    package = models.CharField(max_length=100)
    tnc = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name