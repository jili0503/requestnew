# Generated by Django 2.0.2 on 2019-07-31 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0005_auto_20190729_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='params',
            field=models.CharField(max_length=1000),
        ),
    ]
