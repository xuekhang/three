# Generated by Django 3.1.3 on 2021-02-28 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20210228_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='round',
        ),
        migrations.AddField(
            model_name='question',
            name='category_in_round',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game.categoryinround'),
            preserve_default=False,
        ),
    ]
