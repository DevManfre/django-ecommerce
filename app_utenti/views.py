from django.shortcuts import render
from .forms import *
from .models import *
from hashlib import md5
import datetime

# Create your views here.
def signup(request):
    template = "signup.html"
    ctx = {
        "form": SignUpForm(),
        "messages": list()
    }

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            ecommerceuser = EcommerceUser()

            username = form.cleaned_data.get('signup_username')
            email = form.cleaned_data.get('signup_email')
            
            if User.objects.filter(username=username).exists():
                ctx["messages"].append("Attenzione, username già esistente!")
            if User.objects.filter(email=email).exists():
                ctx["messages"].append("Attenzione, email già esistente!")
            
            if(len(ctx["messages"]) == 0):
                first_name = form.cleaned_data.get('signup_first_name')
                last_name = form.cleaned_data.get('signup_last_name')
                password = form.cleaned_data.get('signup_password')

                ecommerceuser.username = username
                ecommerceuser.first_name = first_name
                ecommerceuser.last_name = last_name
                ecommerceuser.email = email
                ecommerceuser.password = md5(password.encode()).hexdigest()
                ecommerceuser.last_login = datetime.datetime.today()

                ecommerceuser.save()

    return render(request, template_name=template, context=ctx)
