# Generated by Django 5.0.2 on 2024-04-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Название города'),
        ),
        migrations.AlterField(
            model_name='city',
            name='date',
            field=models.DateField(verbose_name='Дата посещения'),
        ),
    ]