from django.shortcuts import render

def homepage(request):
    template = "homepage.html"
    ctx = {}

    return render(request, template_name=template, context=ctx)

def welcomePage(request):
    template = "welcomePage.html"
    ctx = {}

    return render(request, template_name=template, context=ctx)

def vendorWelcomePage(request):
    template = "vendorWelcomePage.html"
    ctx = {}

    return render(request, template_name=template, context=ctx)
