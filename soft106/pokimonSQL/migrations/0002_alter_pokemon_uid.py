# Generated by Django 4.0 on 2022-01-17 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokimonSQL', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='uid',
            field=models.IntegerField(),
        ),
    ]
