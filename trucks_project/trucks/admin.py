# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Truck, TruckModel

admin.site.register(Truck)
admin.site.register(TruckModel)
