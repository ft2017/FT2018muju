from django.db import models

# Create your models here.
from django.db import models


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

class Muju(models.Model):
    muju_wo = models.CharField(max_length=50, default='.')
    muju_date = models.DateField('date published')
    muju_empe = models.CharField(max_length=50, default='.')
    muju_source_code = models.CharField(max_length=50, default='.')
    muju_source_code_name = models.CharField(max_length=50, default='.')
    muju_plan_date = models.CharField(max_length=100, default='.')
    muju_seq = models.CharField(max_length=10, default='.')
    muju_Reason = models.CharField(max_length=1000, default='.')
    muju_date1 = models.CharField(max_length=1000, default='.')
    muju_date2 = models.CharField(max_length=1000, default='.')
    muju_date3 = models.CharField(max_length=1000, default='.')
    muju_date4 = models.CharField(max_length=1000, default='.')
    muju_date5 = models.CharField(max_length=1000, default='.')
    muju_date6 = models.CharField(max_length=1000, default='.')
    muju_date7 = models.CharField(max_length=1000, default='.')
    muju_date8 = models.CharField(max_length=1000, default='.')
    muju_date9 = models.CharField(max_length=1000, default='.')
    muju_date10 = models.CharField(max_length=1000, default='.')
    muju_date11 = models.CharField(max_length=1000, default='.')
    muju_date12 = models.CharField(max_length=1000, default='.')
    muju_date13 = models.CharField(max_length=1000, default='.')
    muju_date14 = models.CharField(max_length=1000, default='.')
    muju_date15 = models.CharField(max_length=1000, default='.')
    muju_date16 = models.CharField(max_length=1000, default='.')
    muju_date17 = models.CharField(max_length=1000, default='.')
    muju_date18 = models.CharField(max_length=1000, default='.')
    muju_date19 = models.CharField(max_length=1000, default='.')
    muju_date20 = models.CharField(max_length=1000, default='.')
    muju_date21 = models.CharField(max_length=1000, default='.')
    def __str__(self):
        return self.muju_wo




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
