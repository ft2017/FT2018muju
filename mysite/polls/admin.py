
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# from .models import Question

# admin.site.register(Question)
# from django.contrib import admin

from .models import Choice, Question

from .models import Yazhu
from .models import Muju1,Muju_date1


class PostResource(resources.ModelResource):
    class Meta:
        model = Muju1

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class MujuDateInline(admin.TabularInline):
    model = Muju_date1
    extra = 1
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
    
# class MujuAdminIE(ImportExportModelAdmin):  
    resource_class = PostResource 
    # inlines = [Muju_date111Inline]
admin.site.register(Muju1, MujuAdmin)
# admin.site.register( MujuAdminIE)

# class Muju_dateAdmin(admin.ModelAdmin):
#     list_display = ('Muju','muju_date1', 'muju_date2',)
admin.site.register(Muju_date1)
# admin.site.register(Muju_date,Muju_dateAdmin)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text','question_description']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
