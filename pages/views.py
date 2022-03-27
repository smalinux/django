from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('index page')
    return render(request, 'pages/index.html')

def about(request):
    return HttpResponse('about pages')
