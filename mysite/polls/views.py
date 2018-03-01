# from django.shortcuts import render,get_object_or_404

# # Create your views here.
# from django.http import HttpResponse
# from .models import Question


from django.shortcuts import get_object_or_404, render
# Create your views here.
from . models import Muju1,Muju_date1,Mujuv2

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# def index(request):
#     return HttpResponse("<h1>中文</h1> Hello, world. You're at the polls index.")




# def index(request):
#     latest_muju_list = Muju1.objects.order_by('muju_date')[:1000]
#     context = {'latest_muju_list': latest_muju_list}
#     return render(request, 'polls/index.html', context)


def index(request):
    # Muju_list = Muju1.objects.order_by('muju_wo')[:1000]
    Muju_list=Mujuv2.objects.all()
    paginator = Paginator(Muju_list, 10)
    page = request.GET.get('page',1)
    class meta:
        ordering=['muju_wo','muju_date']
    # context = {'latest_muju_list': latest_muju_list}
    try:
        print(page)
        Muju_list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        Muju_list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        Muju_list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
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
