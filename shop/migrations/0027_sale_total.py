# Generated by Django 3.0.8 on 2020-08-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20200813_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='total',
            field=models.CharField(default='', max_length=10),
        ),
    ]