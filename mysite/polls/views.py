# from django.shortcuts import render,get_object_or_404

# # Create your views here.
# from django.http import HttpResponse
# from .models import Question


from django.shortcuts import get_object_or_404, render
# Create your views here.
from . models import Muju1,Muju_date1,Mujuv2,Yazhupc

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# def index(request):
#     return HttpResponse("<h1>中文</h1> Hello, world. You're at the polls index.")
from django.db.models import Q  

from django.contrib.auth import authenticate, login, logout
import urllib.request
import json

url ="http://10.10.0.106/c001zt/jsongen/"
weatherHtml = urllib.request.urlopen(url)
weatherHtml1=weatherHtml.read()
# print(weatherHtml1)
weatherJSON=json.loads(weatherHtml1)
# print(weatherJSON)
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

for i in weatherJSON:
    Mujuv2.objects.get_or_create(
                muju_wo=i['AMRT300'],muju_date=str(i['AMRT300_DATE']),muju_empe=i['AMRT300_BY_NAME'],muju_source_code=i['资源编号']
                    ,muju_source_code_name=i['资源名称'],muju_seq=i['SEQ'],muju_Reason=i['报修原因']
                    )

# def main():
#     from polls.models import Mujuv2
#     f=

 # user = authenticate(username=username, password=password)
 #    if user is not None and user.is_active:        
 #    login(request, user)        
 #    return HttpResponseRedirect(redirect_to)

# def index(request):
#     latest_muju_list = Muju1.objects.order_by('muju_date')[:1000]
#     context = {'latest_muju_list': latest_muju_list}
#     return render(request, 'polls/index.html', context)

# @login_require
def index(request):
    # for i in weatherJSON:
    #   Mujuv2.objects.get_or_create(
    #     muju_wo=i['AMRT300'],muju_date=str(i['AMRT300_DATE']),muju_empe=i['AMRT300_BY_NAME'],muju_source_code=i['资源编号']
    #                 ,muju_source_code_name=i['资源名称'],muju_seq=i['SEQ'],muju_Reason=i['报修原因']
    #                 )
    # Muju_list = Muju1.objects.order_by('muju_wo')[:1000]
    Muju_list=Mujuv2.objects.filter(muju_status='False').order_by('muju_date','muju_wo')
    #_gt shi >
    # Muju_list=Mujuv2.objects.filter(muju_seq__gt='0')
    #分页view的逻辑
    # if Muju_list.muju_status=='Ture':
    # print('xxxxxxxxxxxx')

    # paginator = Paginator(Muju_list, 10)
    # page = request.GET.get('page',1)
    # class meta:
    #     ordering=['muju_wo','muju_date']
    # # context = {'latest_muju_list': latest_muju_list}
    # try:
    #     print(page)
    #     Muju_list = paginator.page(page)#获取当前页码的记录
    # except PageNotAnInteger:
    #     Muju_list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    # except EmptyPage:
    #     Muju_list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'polls/index.html', {'Muju_list': Muju_list})
    # return render(request, 'polls/index.html', context)
#def index(request):
  #latest_question_list=Question.objects.order_by('pub_date')[:5]
  #context = {'latest_question_list': latest_question_list}
  #return render(request, 'polls/index.html', context)

#def index(request):
    #latest_muju_list = Muju.objects.order_by('muju_date')[:12]

  #  context = {'latest_muju_list': latest_muju_list}
   # return render(request, 'polls/index.html', context)


def schedula(request):
  schedula_list=Yazhupc.objects.filter(~Q(baiban1= 'nan') or ~Q(wanban1= 'nan') or ~Q(baiban2= 'nan')or ~Q(wanban2= 'nan')or ~Q(baiban3= 'nan')or ~Q(wanban3= 'nan')or ~Q(baiban4= 'nan')or ~Q(wanban4= 'nan')or~Q(baiban5= 'nan')or~Q(wanban5= 'nan')or~Q(baiban6= 'nan')or~Q(wanban6= 'nan')or~Q(baiban7= 'nan')or~Q(wanban7= 'nan')or~Q(baiban8= 'nan')or~Q(wanban8= 'nan'))
  return render(request, 'polls/schedula.html', {'schedula_list': schedula_list})



def detail(request, muju_id):
    muju = get_object_or_404(Muju1, pk=muju_id)
    return render(request, 'polls/detail.html', {'muju': muju})


def index_old(request,muju_wo):
    muju = get_object_or_404(Muju1, pk=muju_wo)
    return render(request, 'polls/index_old.html', {'muju': muju})

def indexDev(request):
    ft_dev_list = Muju1.objects.order_by('muju_date')[:12]
    context = {'ft_dev_list': ft_dev_list}
    return render(request, 'polls/indexDev.html', context)
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


#def results(request, question_id):
   # question = get_object_or_404(Question, pk=question_id)
   # return render(request, 'polls/results.html', {'question': question})


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

#def vote(request, question_id):
   # question = get_object_or_404(Question, pk=question_id)
   # try:
       # selected_choice = question.choice_set.get(pk=request.POST['choice'])
    #except (KeyError, Choice.DoesNotExist):
    #    # Redisplay the question voting form.
       # return render(request, 'polls/detail.html', {
         #   'question': question,
          #  'error_message': "You didn't select a choice.",
       # })
   # else:
        # selected_choice.votes += 1
        #selected_choice.votes += 1

        #selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
       # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
