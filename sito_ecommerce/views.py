from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    template = "homepage.html"
    ctx = {}

    return render(request, template_name=template, context=ctx)

def welcomePage(request):
    template = "tmpLogged.html"
    ctx = {}

    return render(request, template_name=template, context=ctx)
