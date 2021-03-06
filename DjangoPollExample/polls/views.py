from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You are currently viewing question: %s." % question_id)


def results(request, question_id):
    response = "You are currently viewing the results of question: %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are currently voting on question: %s" % question_id)
