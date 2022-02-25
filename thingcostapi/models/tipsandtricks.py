from django.db import models

class TipsAndTricks(models.Model):
    description = models.CharField(max_length=200)