from django.db import models

# Create your models here.

class form(models.Model):
    name=models.CharField(max_length=40)
    topic=models.CharField(max_length=200)
    audience=models.CharField(max_length=40)
    keyword=models.CharField(max_length=100)

    def __str__(self):
        return self.name