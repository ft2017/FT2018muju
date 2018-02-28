# Generated by Django 2.0.1 on 2018-02-09 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20180115_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muju1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muju_wo', models.CharField(default='.', max_length=50, verbose_name='模具维修工单')),
                ('muju_date', models.DateField(verbose_name='AMRT300日期')),
                ('muju_empe', models.CharField(default='.', max_length=50, verbose_name='维修人员')),
                ('muju_source_code', models.CharField(default='.', max_length=50, verbose_name='资源编号')),
                ('muju_source_code_name', models.CharField(default='.', max_length=50, verbose_name='资源名称')),
                ('muju_plan_date', models.DateField(blank=True, null=True, verbose_name='模具预计完成日')),
                ('muju_seq', models.CharField(default='.', max_length=10, verbose_name='项次')),
                ('muju_Reason', models.CharField(default='.', max_length=1000, verbose_name='报修原因')),
            ],
        ),
        migrations.CreateModel(
            name='Muju_date1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muju_date1', models.DateField(blank=True, default=' ', null=True, verbose_name='拆模计划日期')),
                ('muju_date2', models.DateField(blank=True, null=True, verbose_name='拆模实际日期')),
                ('muju_date3', models.DateField(blank=True, null=True, verbose_name='易损与材料制作计划')),
                ('muju_date4', models.DateField(blank=True, null=True, verbose_name='易损与材料制作实际')),
                ('muju_date5', models.DateField(blank=True, null=True, verbose_name='线割计划日期')),
                ('muju_date6', models.DateField(blank=True, null=True, verbose_name='线割实际日期')),
                ('muju_date7', models.DateField(blank=True, null=True, verbose_name='烧焊计划日期')),
                ('muju_date8', models.DateField(blank=True, null=True, verbose_name='烧焊实际日期')),
                ('muju_date9', models.DateField(blank=True, null=True, verbose_name='CNC计划日期')),
                ('muju_date10', models.DateField(blank=True, null=True, verbose_name='CNC实际日期')),
                ('muju_date11', models.DateField(blank=True, null=True, verbose_name='放电计划日期')),
                ('muju_date12', models.DateField(blank=True, null=True, verbose_name='放电实际日期')),
                ('muju_date13', models.DateField(blank=True, null=True, verbose_name='抛光计划日期')),
                ('muju_date14', models.DateField(blank=True, null=True, verbose_name='抛光实际日期')),
                ('muju_date15', models.DateField(blank=True, null=True, verbose_name='组立计划日期')),
                ('muju_date16', models.DateField(blank=True, null=True, verbose_name='组立实际日期')),
                ('muju_date17', models.DateField(blank=True, null=True, verbose_name='其他计划日期')),
                ('muju_date18', models.DateField(blank=True, null=True, verbose_name='其他实际日期')),
                ('muju_date19', models.DateField(blank=True, null=True, verbose_name='备注')),
                ('muju_date20', models.DateField(blank=True, null=True, verbose_name='维修瓶颈工序')),
                ('muju_date21', models.DateField(blank=True, null=True, verbose_name='实际完成日期')),
                ('Muju', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Muju1')),
            ],
        ),
        migrations.DeleteModel(
            name='Muju',
        ),
    ]