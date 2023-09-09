from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextyField()
    technology = models.CharField(max_length=20)
