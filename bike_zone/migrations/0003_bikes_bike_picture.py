# Generated by Django 3.2 on 2021-07-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_zone', '0002_bikes_bike_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='bike_picture',
            field=models.ImageField(default=1, upload_to='product_bike_image'),
            preserve_default=False,
        ),
    ]