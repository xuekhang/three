# Generated by Django 3.1.3 on 2021-02-14 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_config_num_of_cat_per_round'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
