# Generated by Django 2.0.1 on 2018-01-12 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_muju'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muju',
            name='muju_plan_date',
            field=models.DateField(default='.', verbose_name='plane_date'),
        ),
    ]
