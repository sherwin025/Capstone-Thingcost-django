from django.db import models

class UserMoneyResources(models.Model):
    url = models.TextField()
    description = models.CharField(max_length=100)
    user = models.ForeignKey("AUser", on_delete=models.CASCADE)
    