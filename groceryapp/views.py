from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate , login as loginUser,logout
from groceryapp.models import GROCERY
from datetime import datetime
import datetime

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            groceries = GROCERY.objects.all()
            print(groceries)
            return render(request, 'index.html', context={'groceries':groceries})
        else:
            date = request.POST.get('date')
            print(date)
            if date is None:
                groceries = GROCERY.objects.all()
                print(groceries)
                return render(request, 'index.html', context={'groceries':groceries})
            else:
                groceries = GROCERY.objects.filter(date=date)
                print(groceries)
                return render(request, 'index.html', context={'groceries':groceries})
    else:
        return redirect('login')

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        date = request.POST.get('date')
        grocery = GROCERY(name=name, quantity=quantity, status=status, date = date)
        print(request.user)
        print(grocery)
        grocery.save()
        return redirect("home")
    else:
        return render(request,'add.html')

def update_list(request, id):
    if request.method == "GET":
        grocery = GROCERY.objects.get(pk=id)
        print(grocery.date)
        return render(request,'update.html',context={'grocery':grocery})
    else:
        grocery = GROCERY.objects.get(pk=id)
        grocery.name = request.POST.get('name')
        grocery.quantity = request.POST.get('quantity')
        grocery.status = request.POST.get('status')
        grocery.date = request.POST.get('date')
        grocery.save()
        print('update_list')
        return redirect("home")

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form' : form
        }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {
                'form' : form
            }
            return render(request, 'login.html', context=context)

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form              
        }
        return render(request, 'signup.html', context=context)
    
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form" : form              
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)

def signout(request):
    logout(request)
    return redirect('login')

def delete_list(request, id):
    print(id)
    GROCERY.objects.get(pk=id).delete()
    return redirect('home')
