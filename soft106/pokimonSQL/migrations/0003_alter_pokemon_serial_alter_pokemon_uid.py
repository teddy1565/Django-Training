# Generated by Django 4.0 on 2022-01-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokimonSQL', '0002_alter_pokemon_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='serial',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
