# Generated by Django 4.0 on 2022-01-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineQuerySystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='inputText',
            field=models.TextField(blank=True),
        ),
    ]
