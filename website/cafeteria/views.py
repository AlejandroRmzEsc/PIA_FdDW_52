from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request,'index.html')

def unete(request):
    return render(request, 'unete.html')