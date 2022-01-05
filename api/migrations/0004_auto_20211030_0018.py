# Generated by Django 3.1.7 on 2021-10-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211029_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='humidity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='sunrise',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='sunset',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='temp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='tempmax',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='tempmin',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='timezone',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='visibility',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='windspeed',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
