from django.db import models
from django.contrib.auth.models import AbstractUser


class Advertisment(models.Model):
    title = models.CharField(max_length=70,blank=False,default='')
    doctor = models.CharField(max_length=100,blank=False)
    phone = models.CharField(max_length=15,blank=False)
    email = models.CharField(max_length=70,blank=False)
    freetime = models.CharField(max_length=70,blank=False,default='')


class User(AbstractUser):

    def __str__(self):
        return self.username


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Vet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
