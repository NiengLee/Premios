from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.all()
    return HttpResponse('pagina princiapl de premios')

def detail(request, question_id):
    return HttpResponse(f"estas viendo la pregunta numero {question_id}")

def results(request, question_id):
    return HttpResponse(f"estas viendo los resultados de la pregunta numero {question_id}")
