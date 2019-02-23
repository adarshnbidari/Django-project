#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


from .models import Question

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    output=','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def index(request):
    return HttpResponse("Hello,world.You're at the polls index.")

def detail(request,question_id):
    return HttpResponse("you're looking at the question %s.",% question_id);

def results(request,question_id):
    response="you're looink at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("you're voting on question %s." %s question_id)
