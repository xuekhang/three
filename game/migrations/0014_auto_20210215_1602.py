# Generated by Django 3.1.3 on 2021-02-15 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_round_letter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='letter',
            field=models.CharField(max_length=3),
        ),
    ]
