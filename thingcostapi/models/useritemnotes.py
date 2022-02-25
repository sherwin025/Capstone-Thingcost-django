from django.db import models

class UserItemNotes(models.Model):
    description = models.CharField(max_length=250)
    item = models.ForeignKey("Item", on_delete=models.CASCADE, )