from urllib.request import CacheFTPHandler
from django.db import models

class ItemRaking(models.Model):
    ranking = models.IntegerField()
    item = models.ForeignKey("Item", on_delete=models.CASCADE, )