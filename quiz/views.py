# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def main_page(request):
    template = get_template("quiz/main_page.html")
    variable = Context({
            'head_title' : "Online Quiz",
            'page_title' : "Welcome to Online Quiz",
            'page_body' : "Where you can prepare of competative exams"
            })
    output = template.render(variable)
    return HttpResponse(output)

