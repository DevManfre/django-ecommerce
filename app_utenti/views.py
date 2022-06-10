from re import A
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from hashlib import md5
import datetime
from django.contrib.auth import authenticate, login

# Create your views here.
template = "signup_login.html"

def signupPage(request):
    ctx = {
        "action" : "signup",
        "tabTitle" : "eGym - Registrazione",
        "title" : "Nuovo Utente",
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
                ecommerceuser.set_password(md5(password.encode()).hexdigest())
                ecommerceuser.last_login = datetime.datetime.today()

                ecommerceuser.save()

                #TODO: Aggiungere popup di conferma
                return redirect('homepage')

    return render(request, template_name=template, context=ctx)

def loginPage(request):
    ctx = {
        "action" : "login",
        "tabTitle" : "eGym - Login",
        "title" : "Accesso",
        "form": LogInForm(),
        "messages": list()
    }

    if request.method == "POST":
        form = LogInForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("login_username")
            password = md5(form.cleaned_data.get("signup_password").encode()).hexdigest()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('welcomePage')
            
    return render(request, template_name=template, context=ctx)