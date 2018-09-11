# Generated by Django 2.1.1 on 2018-09-11 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='number')),
                ('max_weight', models.IntegerField(default=0, verbose_name='max_weight')),
                ('current_weight', models.IntegerField(default=0, verbose_name='current_weight')),
            ],
        ),
        migrations.CreateModel(
            name='TruckModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='truck_model')),
            ],
        ),
        migrations.AddField(
            model_name='truck',
            name='truck_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trucks.TruckModel'),
        ),
    ]
