# Generated by Django 3.2.8 on 2021-11-03 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20211103_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ex_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
