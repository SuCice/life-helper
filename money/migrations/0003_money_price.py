# Generated by Django 3.0.3 on 2020-02-17 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0002_moneyprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
