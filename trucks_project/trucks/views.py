# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db.models import IntegerField, Case, Value, When, F, Func, FloatField

from .models import Truck, TruckModel


def index(request):
    truck_models_list = TruckModel.objects.all()
    if request.GET.get('filter', 'ALL') == 'ALL':
        trucks_list = Truck.objects.all().annotate(
            percentage=Case(
                When(truck_model__max_weight__lt=F('current_weight'),
                     then=Func(100 * (F('truck_model__max_weight') - F('current_weight')) / F('truck_model__max_weight'), function='ABS')),
                default=Value(0),
                output_field=IntegerField(),
            ),
        )
    else:
        trucks_list = Truck.objects.all().annotate(
            percentage=Case(
                When(truck_model__max_weight__lt=F('current_weight'),
                     then=Func(100 * (F('truck_model__max_weight') - F('current_weight')) / F('truck_model__max_weight'), function='ABS')),
                default=Value(0),
                output_field=IntegerField(),
            ),
        ).filter(truck_model__name=request.GET.get('filter'))

    context = {'trucks_list': trucks_list, 'truck_models_list': truck_models_list}
    return render(request, 'truck/index.html', context)
