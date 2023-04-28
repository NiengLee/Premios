from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list" : latest_question_list,
        })

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {
        "quetion": question
    })
    

def results(request, question_id):
    return HttpResponse(f"estas viendo los resultados de la pregunta numero {question_id}")
