from django.db import models

class Item(models.Model):
    useritemtype = models.ForeignKey("UserItemTypes", on_delete=models.CASCADE)
    price = models.FloatField()
    name = models.CharField(max_length=40)
    need = models.BooleanField()
    user = models.ForeignKey("AUser", on_delete=models.CASCADE)
    hoursneeded = models.FloatField()
    buydifficulty = models.ForeignKey("BuyDifficulty", on_delete=models.CASCADE)
    purchased = models.BooleanField()
    purchaseby = models.DateField()
    