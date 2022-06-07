from django.shortcuts import render
from .forms import *
from .models import *
from hashlib import md5
import datetime

# Create your views here.
def costumerSignUp(request):
    template = "signupCostumer.html"
    ctx = {
        "form": SignUpFormCostumer(),
    }

    if request.method == "POST":
        form = SignUpFormCostumer(request.POST)

        if form.is_valid():
            costumer = Costumer()

            username = form.cleaned_data.get('signup_username')
            if User.objects.filter(username=username).exists():
                ctx["message"] = "Attenzione, username già presente!<br>"
            else:
                first_name = form.cleaned_data.get('signup_first_name')
                last_name = form.cleaned_data.get('signup_last_name')
                email = form.cleaned_data.get('signup_email')
                password = form.cleaned_data.get('signup_password')

                costumer.username = username
                costumer.first_name = first_name
                costumer.last_name = last_name
                costumer.email = email
                costumer.password = md5(password.encode()).hexdigest()
                costumer.last_login = datetime.datetime.today()

                costumer.save()

    return render(request, template_name=template, context=ctx)
