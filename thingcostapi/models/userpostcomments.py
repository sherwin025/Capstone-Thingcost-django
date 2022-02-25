from django.db import models

class UserPostComments(models.Model):
    comment = models.CharField(max_length=250)
    userpostsid = models.ForeignKey("UserPost", on_delete=models.CASCADE)
    user = models.ForeignKey("AUser", on_delete=models.CASCADE)