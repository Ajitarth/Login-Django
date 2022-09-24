from django.shortcuts import render, redirect
from . models import User_query
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Welcome {username}, your account is created ')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'queryScraper/register.html',{'form':form})




@login_required()
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        query = request.POST.get("query","")
        dateTime = request.POST.get("name","")

        query = User_query(name=name,query=query,dateTime=dateTime)
        query.save()
    return render(request,'queryScraper/accept.html')

