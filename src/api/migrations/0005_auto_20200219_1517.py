# Generated by Django 3.0.3 on 2020-02-19 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200219_1250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='device',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
    ]