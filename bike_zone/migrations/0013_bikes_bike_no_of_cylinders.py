# Generated by Django 3.2 on 2021-07-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_zone', '0012_bikes_bike_stroke'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='bike_no_of_cylinders',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
