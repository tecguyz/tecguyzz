# Generated by Django 3.1.4 on 2021-04-05 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecguyz', '0010_auto_20210405_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='deals',
            name='link',
            field=models.CharField(blank='True', max_length=2345),
        ),
    ]
