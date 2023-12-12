from django.db import models

class Contact(models.Model):
    firstName = models.CharField(max_length=100, verbose_name="User First Name")
    
    lastName = models.CharField(max_length=100, verbose_name="User Last Name")
    
    email = models.EmailField(max_length=100, verbose_name="User Email Adress")
    
    phone = models.CharField(max_length=100, verbose_name="User Phone Number")

    message = models.TextField(blank=True, verbose_name="User Message")

    def __str__(self):
        return self.email

