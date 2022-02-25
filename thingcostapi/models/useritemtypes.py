from django.db import models

class UserItemTypes(models.Model):
    description = models.CharField(max_length=25)
    user = models.ForeignKey("AUser", on_delete=models.CASCADE)