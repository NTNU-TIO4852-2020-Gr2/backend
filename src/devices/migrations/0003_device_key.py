# Generated by Django 3.0.4 on 2020-03-18 23:54

import devices.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_measurement_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='key',
            field=models.CharField(default=devices.models.get_random_string_64, max_length=64, validators=[django.core.validators.MinLengthValidator(64)]),
        ),
    ]
