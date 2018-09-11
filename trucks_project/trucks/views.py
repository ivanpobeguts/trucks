# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db.models import IntegerField, Case, Value, When, F, Func

from .models import Truck


def index(request):
    trucks_list = Truck.objects.all().annotate(
        percentage=Case(
            When(max_weight__lt=F('current_weight'),
                 then=Func(100 * (F('max_weight') - F('current_weight')) / F('max_weight'), function='ABS')),
            default=Value(0),
            output_field=IntegerField(),
        ),
    )

    context = {'trucks_list': trucks_list}
    return render(request, 'truck/index.html', context)
