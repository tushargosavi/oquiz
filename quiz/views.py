# Create your views here.
import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context,RequestContext
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from quiz.models import Question, Answer, Tag
from quiz.forms import RegistrationForm
from quiz.forms import QuestionSaveForm

def main_page(request):
    return render(request, 'quiz/main_page.html',
           { 'user' : request.user })

@login_required
def user_page(request, username):
    user = get_object_or_404(User, username=username)
    questions = Question.objects.all()
    template = get_template("quiz/user_page.html")
    variables = RequestContext(request, {
            'username' : username,
            'questions' : questions,
            'show_tags' : True,
            })

    output = template.render(variables)
    return HttpResponse(output)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")

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
        form = RegistrationForm()

    return render(request, "registration/register.html",
                  { 'form' : form })

@login_required
def question_save_page(request):
    if request.method == 'POST':
        form = QuestionSaveForm(request.POST)
        if form.is_valid():
            question = Question.objects.create(
                text = form.cleaned_data['text'],
                opt1 = form.cleaned_data['opt1'],
                opt2 = form.cleaned_data['opt2'],
                opt3 = form.cleaned_data['opt3'],
                opt4 = form.cleaned_data['opt4'],
                correctOpt=form.cleaned_data['ans'],
                user = request.user,
                numLikes = 0,
                numUnLikes = 0,
                added = datetime.datetime.now())
            tag_names = form.cleaned_data['tags'].split()
            for tag in tag_names:
                tag, dummy = Tag.objects.get_or_create(name=tag)
                question.tag_set.add(tag)
            question.save()
            return HttpResponseRedirect("/")
    else:
        form = QuestionSaveForm()

    return render(request, "quiz/question_save.html",
                  { 'form' : form })


# Tag page
def tag_page(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    questions = tag.questions.order_by('-id')
    return render(request, "quiz/tag_page.html",
                  { 'questions' : questions,
                    'show_tags' : False,
                    'show_user' : True,
                    'tag_name'  : tag_name })

def tag_cloude_page(request):
    MAX_WEIGHT = 5
    tags = Tag.objects.order_by('name')

    # Calculate tag, min and max counts.
    min_count = max_count = tags[0].questions.count()
    for tag in tags:
        tag.count = tag.questions.count()
        if tag.count < min_count:
            min_count = tag.count
        if max_count < tag.count:
            max_count = tag.count

    # Calculate count range. Avoid dividing by zero.
    diff = float(max_count - min_count)
    if diff == 0.0:
        diff = 1.0

    # Calculate tag weights.
    for tag in tags:
        tag.weight = int(
            MAX_WEIGHT * (tag.count - min_count) / diff
            )

    return render(request, 'quiz/tag_cloud_page.html', {
            'tags' : tags })
                    
