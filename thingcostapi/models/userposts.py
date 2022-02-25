from django.db import models

class UserPost(models.Model):
    post = models.CharField(max_length=25)
    user = models.ForeignKey("AUser", on_delete=models.CASCADE)