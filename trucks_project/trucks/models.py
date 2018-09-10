from django.db import models


class Truck(models.Model):
    number = models.CharField(max_length=20)
    truck_model = models.CharField(max_length=20)
    max_weight = models.IntegerField(default=0)
    current_weight = models.IntegerField(default=0)

