# Generated by Django 2.0.1 on 2018-01-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20180115_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muju',
            name='muju_date1',
            field=models.DateField(blank=True, default=' ', null=True, verbose_name='拆模计划日期'),
        ),
    ]
