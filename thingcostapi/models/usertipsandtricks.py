from django.db import models

class UserTipsAndTricks(models.Model):
    description = models.CharField(max_length=200)
    user = models.ForeignKey("AUser", on_delete=models.CASCADE)