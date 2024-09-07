from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class MessagesList(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ('-id',)

        verbose_name = _("Message List")
        verbose_name_plural = _("Messages List")

    def __str__(self):
        return str(self.id)

class Contact(models.Model):
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.address} {self.telephone} {self.location}'

# models.py

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
