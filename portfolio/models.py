from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length = 150)
    text = models.CharField(max_length = 150)
    image = models.ImageField(upload_to="projects", null=True)
    date = models.CharField(max_length = 150)
    skills = models.CharField(max_length = 150)
    link = models.CharField(max_length = 250)

class Backend(models.Model):
    title = models.CharField(max_length = 150)
    icon = models.FileField(upload_to="skills")

class Frontend(models.Model):
    title = models.CharField(max_length = 150)
    icon = models.FileField(upload_to="skills")

class Tools(models.Model):
    title = models.CharField(max_length = 150)
    icon = models.FileField(upload_to="skills")

class Files(models.Model):
    cv = models.FileField(upload_to="files")
    filename = models.CharField(max_length = 150, null=True)