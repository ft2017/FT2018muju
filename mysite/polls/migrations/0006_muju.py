# Generated by Django 2.0.1 on 2018-01-12 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180109_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muju',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muju_wo', models.CharField(default='.', max_length=50)),
                ('muju_date', models.DateField(verbose_name='date published')),
                ('muju_empe', models.CharField(default='.', max_length=50)),
                ('muju_source_code', models.CharField(default='.', max_length=50)),
                ('muju_source_code_name', models.CharField(default='.', max_length=50)),
                ('muju_plan_date', models.DateField(verbose_name='plane_date')),
                ('muju_seq', models.CharField(default='.', max_length=10)),
            ],
        ),
    ]
