# Generated by Django 4.2 on 2025-01-09 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libr', '0002_alter_reading_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, to='libr.author', verbose_name='Авторы'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 9, 16, 10, 38, 610291), verbose_name='Дата выдачи книги'),
        ),
    ]
