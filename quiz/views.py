# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from quiz.models import Question, Answer

def main_page(request):
    template = get_template("quiz/main_page.html")
    variable = Context({
            'head_title' : "Online Quiz",
            'page_title' : "Welcome to Online Quiz",
            'page_body' : "Where you can prepare of competative exams"
            })
    output = template.render(variable)
    return HttpResponse(output)

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404("Requested user not found %s." % username)

    questions = Question.objects.all()
    
    template = get_template("quiz/user_page.html")
    variables = Context({
            'username' : username,
            'questions' : questions
            })

    output = template.render(variables)
    return HttpResponse(output)
