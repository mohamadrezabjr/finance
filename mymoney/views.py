from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .forms import *
import string,random

def main(request):
    template= loader.get_template('main.html')
    return render(request,'main.html')

def random_str ():
    return ''.join(random.choices(string.ascii_letters,k=25))
@csrf_exempt
# Create your views here.
def get_info(request):

    template = loader.get_template('forms.html')
    return HttpResponse (template.render())

@csrf_exempt
def register(request):

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            this_user = User.objects.filter(username = request.POST['username']).get()
            this_token =random_str()
            Token.objects.create(user = this_user, token = this_token)

            template= loader.get_template('showtoken.html')
            context = {'token' : this_token}

            return HttpResponse(template.render(context, request))
    context = {'form':form}

    return render(request, 'register.html', context=context)

def login(request):

    return HttpResponse("<h1>Welcome</h1>")


def test(request):

    template= loader.get_template('test.html')
    return HttpResponse(template.render())

@csrf_exempt
def submit_expense(request):

    this_token = request.POST['token']
    this_user =  User.objects.filter(token__token = this_token).get()

    expense.objects.create(user = this_user , text = request.POST['text'] , amount = request.POST['amount'] ,
                           date = datetime.now() )
    return HttpResponse('expense submitted')

def submit_income(request):

    this_token = request.POST['token']
    this_user =  User.objects.filter(token__token = this_token).get()

    income.objects.create(user = this_user , text = request.POST['text'] , amount = request.POST['amount'] ,
                           date = datetime.now() )
    return HttpResponse('expense submitted')