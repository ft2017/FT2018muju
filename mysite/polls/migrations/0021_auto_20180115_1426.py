# Generated by Django 2.0.1 on 2018-01-15 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20180115_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muju',
            name='muju_Reason',
            field=models.CharField(default='.', max_length=1000, verbose_name='报修原因'),
        ),
    ]
