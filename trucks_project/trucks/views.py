# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Truck


import logging

logger = logging.getLogger(__name__)


def index(request):
    trucks_list = Truck.objects.all()
    context = {'trucks_list': trucks_list}
    return render(request, 'truck/index.html', context)
