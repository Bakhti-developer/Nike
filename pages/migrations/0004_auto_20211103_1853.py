# Generated by Django 3.2.8 on 2021-11-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20211103_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ex_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
