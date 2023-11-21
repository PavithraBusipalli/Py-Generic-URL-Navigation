from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def logout(request):
    return render(request,'logout.html')

