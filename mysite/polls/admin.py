
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin,ImportExportActionModelAdmin
from import_export.fields import Field
# from .models import Question

# admin.site.register(Question)
# from django.contrib import admin

from .models import Choice, Question
from django.db import models
from .models import Yazhu
from .models import Muju1,Muju_date1


class PostResource(resources.ModelResource):
    
    # Muju = models.ForeignKey(Muju1, on_delete=models.CASCADE,verbose_name='模具维修工单')
    # full_title = Field()
    class Meta:
        model = Muju1
        # fields =('muju_wo','muju_date','muju_empe','muju_source_code','muju_source_code_name','muju_plan_date','muju_seq','muju_Reason')
        # fields=('Muju')
    # def dehydrate_full_title(self, Muju_date1):
        # return '%s by %s' % (Muju_date1.Muju)
        # list_display=['muju_wo','muju_date','muju_empe','muju_source_code','muju_source_code_name','muju_plan_date','muju_seq','muju_Reason']

class MujuResource(resources.ModelResource):
    # muju_wo = fields.Field(widget=widgets.ForeignKeyWidget(Muju1, 'muju_wo'))
    class Meta:
        model = Muju_date1
        # import_id_fields = ['Muju']
        # fields=['muju_wo','muju_date','muju_empe','muju_source_code','muju_source_code_name','muju_plan_date','muju_seq','muju_Reason']
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class MujuDateInline(admin.StackedInline):
    model = Muju_date1
    extra=0

class YazhuAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['work_date','work_prod','work_mach']}),
        ('不良', {'fields': ['rej01','rej02','rej03'], 'classes': ['collapse']}),
    ]


admin.site.register(Yazhu, YazhuAdmin)


class MujuAdmin(ImportExportModelAdmin):

    fieldsets = [
        (None,               {'fields': ['muju_wo','muju_date','muju_empe','muju_source_code','muju_source_code_name','muju_plan_date','muju_seq','muju_Reason']}),
        # ('Date information', {'fields': ['muju_date']}),
    ]
    list_display = ('muju_wo', 'muju_source_code','muju_source_code_name')
    inlines = [MujuDateInline]
# class MujuAdminIE(ImportExportModelAdmin):  
    resource_class = PostResource 

admin.site.register(Muju1, MujuAdmin)
# admin.site.register( MujuAdminIE)
class MujuDateAdmin(ImportExportModelAdmin):
     resource_class = MujuResource
    # inlines = [Muju_date111Inline]
admin.site.register(Muju_date1,MujuDateAdmin)
# class Muju_dateAdmin(admin.ModelAdmin):
#     list_display = ('Muju','muju_date1', 'muju_date2',)
# admin.site.register(Muju_date1)
# admin.site.register(Muju_date,Muju_dateAdmin)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text','question_description']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
