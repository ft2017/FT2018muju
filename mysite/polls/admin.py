
from django.contrib import admin

# from .models import Question

# admin.site.register(Question)
# from django.contrib import admin

from .models import Choice, Question
from .models import Yazhu
from .models import Muju
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class YazhuAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['work_date','work_prod','work_mach']}),
        ('不良', {'fields': ['rej01','rej02','rej03'], 'classes': ['collapse']}),
    ]


admin.site.register(Yazhu, YazhuAdmin)


class MujuAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['muju_wo','muju_date','muju_empe','muju_source_code','muju_source_code_name','muju_plan_date','muju_seq','muju_Reason','muju_date1','muju_date2','muju_date3','muju_date4','muju_date5','muju_date6','muju_date7','muju_date8','muju_date9','muju_date10','muju_date11','muju_date12','muju_date13','muju_date14','muju_date15','muju_date16','muju_date17','muju_date18','muju_date19','muju_date20','muju_date21']}),
       
    ]


admin.site.register(Muju, MujuAdmin)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text','question_description']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
