# Generated by Django 3.2 on 2021-07-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_zone', '0004_bikes_bike_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='bike_location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]