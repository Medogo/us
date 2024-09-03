from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.CharField(max_length=50)
    messages = models.TextField(blank=True)
    def __str__(self):
        return  f'{self.name} {self.email} {self.content}'


class Contact(models.Model):
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.address} {self.telephone} {self.location}'
