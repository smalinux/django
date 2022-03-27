from django.shortcuts import render
import os
#from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('index page')
    x = {
            'name':'ahmed',
            'last':'',
            'full':'Sohaib Mohamed Abdel fattah',
            'age': 62783467324,
        }
    return render(request, 'pages/index.html', x)

def about(request):
    return render(request, 'pages/about.html')
