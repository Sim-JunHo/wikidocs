from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


def index(req):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(req, 'pybo/question_list.html', context)


def detail(req, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(req, 'pybo/question_detail.html', context)
