# Generated by Django 4.2.3 on 2023-08-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0003_alter_advertisement_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Обновлено'),
        ),
    ]
