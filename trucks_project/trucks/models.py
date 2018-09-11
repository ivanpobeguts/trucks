from django.db import models


class TruckModel(models.Model):
    name = models.CharField(max_length=20, verbose_name='truck_model')


class Truck(models.Model):
    number = models.CharField(max_length=20, verbose_name='number')
    truck_model = models.ForeignKey(TruckModel, on_delete=models.CASCADE)
    max_weight = models.IntegerField(default=0, verbose_name='max_weight')
    current_weight = models.IntegerField(default=0, verbose_name='current_weight')

