from django.db import models

# Create your models here.
# from django.db import models


class Yazhu(models.Model):
    work_date = models.DateField('date published')
    work_prod = models.CharField(max_length=50, default='.')
    work_mach = models.CharField(max_length=50, default='.')
    rej01=models.IntegerField(default=0)
    rej02=models.IntegerField(default=0)
    rej03=models.IntegerField(default=0)
    def __str__(self):
        return self.work_mach

# class Reject(models.Model):
#     yazhu = models.ForeignKey(Yazhu, on_delete=models.CASCADE)
#     reject_name = models.CharField(max_length=200)
#     reject_qty = models.IntegerField(default=0)
#     def __str__(self):
#         return self.reject_name

# from django.db import models

# Create your models here.
class Muju1(models.Model):
    muju_wo = models.CharField('模具维修工单',max_length=50, default='.')
    muju_date = models.DateField('AMRT300日期')
    muju_empe = models.CharField('维修人员',max_length=50, default='.')
    muju_source_code = models.CharField('资源编号',max_length=50, default='.')
    muju_source_code_name = models.CharField('资源名称',max_length=50, default='.')
    muju_plan_date = models.DateField('模具预计完成日',null=True, blank=True)
    muju_seq = models.CharField('项次',max_length=10, default='.')
    muju_Reason = models.CharField('报修原因',max_length=1000, default='.')

    class meta:
        verbose_name = '主要信息'
        verbose_name_plural = '主要信息'
    
    def __str__(self):
        return self.muju_wo

class Muju_date1(models.Model):
    Muju = models.ForeignKey(Muju1, on_delete=models.CASCADE)
    muju_date1 = models.DateField('拆模计划日期', null=True,blank=True)
    muju_date2 = models.DateField('拆模实际日期',null=True, blank=True)
    muju_date3 = models.DateField('易损与材料制作计划',null=True, blank=True)
    muju_date4 = models.DateField('易损与材料制作实际',null=True, blank=True)
    muju_date5 = models.DateField('线割计划日期',null=True, blank=True)
    muju_date6 = models.DateField('线割实际日期',null=True, blank=True)
    muju_date7 = models.DateField('烧焊计划日期',null=True, blank=True)
    muju_date8 = models.DateField('烧焊实际日期',null=True, blank=True)
    muju_date9 = models.DateField('CNC计划日期',null=True, blank=True)
    muju_date10 = models.DateField('CNC实际日期',null=True, blank=True)
    muju_date11 = models.DateField('放电计划日期',null=True, blank=True)
    muju_date12 = models.DateField('放电实际日期',null=True, blank=True)
    muju_date13 = models.DateField('抛光计划日期',null=True, blank=True)
    muju_date14 = models.DateField('抛光实际日期',null=True, blank=True)
    muju_date15 = models.DateField('组立计划日期',null=True, blank=True)
    muju_date16 = models.DateField('组立实际日期',null=True, blank=True)
    muju_date17 = models.DateField('其他计划日期',null=True, blank=True)
    muju_date18 = models.DateField('其他实际日期',null=True, blank=True)
    muju_date19 = models.CharField('备注',max_length=1000, default='.')
    muju_date20 = models.CharField('维修瓶颈工序',max_length=50, default='.')
    muju_date21 = models.DateField('实际完成日期',null=True, blank=True)
    def __str__(self):
        return str(self.Muju)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_description = models.CharField(max_length=500, default='.')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
