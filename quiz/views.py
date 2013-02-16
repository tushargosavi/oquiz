# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context,RequestContext
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from django.contrib.auth import logout
from quiz.models import Question, Answer

def main_page(request):
    return render(request, 'quiz/main_page.html',
           { 'user' : request.user })

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404("Requested user not found %s." % username)

    questions = Question.objects.all()
    
    template = get_template("quiz/user_page.html")
    variables = Context({
            'username' : username,
            'questions' : questions,
            })

    output = template.render(variables)
    return HttpResponse(output)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")
