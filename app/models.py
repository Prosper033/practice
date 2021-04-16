from django.db import models
import datetime


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=50, null=False)
    active = models.BooleanField(default=True, null=False)
    last_login = models.DateField(default=datetime.datetime.now())
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    role = models.ManyToManyField('Role')
    permission = models.ManyToManyField('Permission')


class Role(models.Model):
    role_name = models.CharField(max_length=50, null=False)
    role_description = models.CharField(max_length=50, null=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    permission = models.ManyToManyField('Permission')


class Permission(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=50, null=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
