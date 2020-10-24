from django.db import models
from userapp.models import Usertable
from django.contrib.auth.models import User  # this is inbuilt user


class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

    def get_absolute_url(self):
        return '#'

#=========================================================================================================#
class ITJobs(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desgination = models.CharField(max_length=100)
    experience = models.FloatField()
    package = models.FloatField()
    vaccancy = models.IntegerField()
    date_from = models.DateField()
    date_to = models.DateField()
    location = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    user = models.ManyToManyField(Usertable)
    hrtable = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return f'/readitjob/{self.hrtable.id}/'

#=========================================================================================================#
class MechJobs(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desgination = models.CharField(max_length=100)
    experience = models.FloatField()
    package = models.FloatField()
    vaccancy = models.IntegerField()
    date_from = models.DateField()
    date_to = models.DateField()
    location = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    user = models.ManyToManyField(Usertable)
    hrtable = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return f'/readmechjob/{self.hrtable.id}/'

#=========================================================================================================#
class CivilJobs(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desgination = models.CharField(max_length=100)
    experience = models.FloatField()
    package = models.FloatField()
    vaccancy = models.IntegerField()
    date_from = models.DateField()
    date_to = models.DateField()
    location = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    user = models.ManyToManyField(Usertable)
    hrtable = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return f'/readciviljob/{self.hrtable.id}/'
