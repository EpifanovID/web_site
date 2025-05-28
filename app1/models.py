from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='app1/static/app1/images/')

class ProgramSupervisor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.ImageField(upload_to='app1/images/')

class ProgramManager(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.ImageField(upload_to='app1/images/')

class ProgramInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    supervisor = models.OneToOneField(ProgramSupervisor, on_delete=models.CASCADE)
    manager = models.OneToOneField(ProgramManager, on_delete=models.CASCADE)

class Classmate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='app1/images/')
