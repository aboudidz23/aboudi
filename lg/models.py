from django.db import models

# Create your models here.
class secret(models.Model):
    user=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
