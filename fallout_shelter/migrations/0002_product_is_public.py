# Generated by Django 4.2.6 on 2023-10-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fallout_shelter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='Опубликовать'),
        ),
    ]
