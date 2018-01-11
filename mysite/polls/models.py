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
