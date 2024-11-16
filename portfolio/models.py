from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length = 150)
    text = models.CharField(max_length = 150)
    imagelink = models.CharField(max_length = 250, null=True)
    date = models.CharField(max_length = 150)
    skills = models.CharField(max_length = 150)
    link = models.CharField(max_length = 250)

class Backend(models.Model):
    title = models.CharField(max_length = 150)
    iconlink = models.CharField(max_length = 250, null=True)

class Frontend(models.Model):
    title = models.CharField(max_length = 150)
    iconlink = models.CharField(max_length = 250, null=True)

class Tools(models.Model):
    title = models.CharField(max_length = 150)
    iconlink = models.CharField(max_length = 250, null=True)

class Files(models.Model):
    cvlink = models.CharField(max_length = 250, null=True)
    filename = models.CharField(max_length = 150, null=True)