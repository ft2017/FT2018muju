# Generated by Django 2.0.1 on 2018-02-11 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_auto_20180211_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muju_date1',
            name='muju_date19',
            field=models.TextField(default='.', max_length=1000, verbose_name='备注'),
        ),
    ]