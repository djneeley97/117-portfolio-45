from django.db import models

# Create your models here.
# EVERYTIME you modify anything in models,
# remember to run migrations

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='projects_images/')
    repository = models.URLField()
    technologies = models.ManyToManyField(Technology)

