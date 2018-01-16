# from django.shortcuts import render,get_object_or_404

# # Create your views here.
# from django.http import HttpResponse
# from .models import Question


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question
from .models import Muju


# def index(request):
#     return HttpResponse("<h1>中文</h1> Hello, world. You're at the polls index.")





def index(request):
    latest_muju_list = Muju.objects.order_by('muju_date')[:12]

    context = {'latest_muju_list': latest_muju_list}
    return render(request, 'polls/index.html', context)




def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def index_old(request,muju_wo):
    muju = get_object_or_404(muju, pk=muju_id)
    return render(request, 'polls/index_old.html', {'muju': muju})    

def indexDev(request):
    ft_dev_list = Muju.objects.order_by('muju_date')[:12]
    context = {'ft_dev_list': ft_dev_list}
    return render(request, 'polls/indexDev.html', context)
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choice.votes += 1
        selected_choice.votes += 1

        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
