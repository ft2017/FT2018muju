# Generated by Django 2.0.1 on 2018-03-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180301_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mujuv2',
            name='muju_status',
            field=models.BooleanField(default='False', verbose_name='完成否'),
        ),
    ]