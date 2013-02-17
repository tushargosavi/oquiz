# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context,RequestContext
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from django.contrib.auth import logout
from quiz.models import Question, Answer
from quiz.forms import RegistrationForm
from quiz.forms import QuestionSaveForm

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
    variables = RequestContext(request, {
            'username' : username,
            'questions' : questions,
            })

    output = template.render(variables)
    return HttpResponse(output)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")

def register_error(request, form):
    return render(request, "registration/register.html",
           { 'form' : form });

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = form.cleaned_data['email']
                )
            # hack, somehow create do not encrypt the password
            # while saving into database. use ser_password to
            # save encrypted password.
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return HttpResponseRedirect("/register/success")
        else:
            return register_error(request, form)
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {
                'form' : form
                })
        return render_to_response(
            'registration/register.html',
            variables)

def question_save_page(request):
    if request.method == 'POST':
        print "POST called"
    else:
        form = QuestionSaveForm()
        return render(request, "quiz/question_save.html",
               { 'form' : form })
