from django.db import models

class ItemType(models.Model):
    label = models.CharField(max_length=20)