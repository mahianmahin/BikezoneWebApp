# Generated by Django 3.2 on 2021-07-31 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_zone', '0018_auto_20210725_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='bike_brand',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bikes',
            name='bike_model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bikes',
            name='bike_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bikes',
            name='bike_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
