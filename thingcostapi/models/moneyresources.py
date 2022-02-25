from django.db import models

class MoneyResources(models.Model):
    url = models.TextField()
    description = models.CharField(max_length=100)
    