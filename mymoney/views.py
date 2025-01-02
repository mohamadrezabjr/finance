from django.contrib.auth import logout
from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .forms import *
from django.contrib import messages

def main(request):
    return render(request,'main.html')

def register(request):

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'showtoken.html')
    context = {'form':form}

    return render(request, 'register.html', context=context)


def test(request):

    template= loader.get_template('test.html')
    return HttpResponse(template.render())

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('/')


def management(request):
    # this_token = request.POST['token']
    if request.user.is_authenticated:
        if request.method == 'POST':

            this_user = request.user
            try:
                income.objects.create(user=this_user, text=request.POST['text_income'], amount=request.POST['amount_income'],
                date=datetime.now())
            except:
                expense.objects.create(user=this_user, text=request.POST['text_expense'], amount=request.POST['amount_expense'],
                                   date=datetime.now())
        this_user = request.user

        this_expense = expense.objects.filter(user = this_user).order_by('-date')
        this_income =income.objects.filter(user=this_user).order_by('-date')
        context = {'expenses' :this_expense , 'incomes': this_income}

        return render(request, 'manage.html', context =context)
    else :
        return redirect('login')


