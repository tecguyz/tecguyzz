# Generated by Django 3.1.4 on 2021-04-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecguyz', '0008_remove_trending_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='trending',
            name='image',
            field=models.CharField(blank='True', max_length=2343),
        ),
    ]