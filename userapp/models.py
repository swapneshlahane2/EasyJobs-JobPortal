from django.db import models

# Create your models here.

class Usertable(models.Model):
    name = models.CharField(max_length =50)
    username = models.CharField(max_length =50)
    password = models.CharField(max_length =50)
    confirm_password = models.CharField(max_length =50)
    email = models.EmailField()
    address = models.CharField(max_length =50)
    contact = models.CharField(max_length =50)
    resume = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name
