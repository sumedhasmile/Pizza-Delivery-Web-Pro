# Generated by Django 3.0.6 on 2020-06-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0002_customermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='phoneno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pizzamodel',
            name='price',
            field=models.IntegerField(),
        ),
    ]