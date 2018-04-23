from django import forms

from .models import Mujuv2

class Muju2Form(forms.ModelForm):

    class Meta:
        model = Mujuv2
        fields = ('muju_plan_date', 'muju_date1','muju_date2','muju_date3','muju_date4','muju_date5','muju_date6','muju_date7','muju_date8','muju_date9','muju_date10','muju_date11','muju_date12','muju_date13','muju_date14','muju_date15','muju_date16','muju_date17','muju_date18','muju_date19','muju_date20','muju_date21','muju_status',)