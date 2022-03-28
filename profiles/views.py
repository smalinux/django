from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
#from .models import

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

# SMA: Every funcion == 1 page
def profiles(request):
    ## Get all from db
    #return render(request, 'profiles.html', {'pro': Profile.objects.all()})
    # Set spacific element
    return render(request, 'profiles.html', {'pro':Profile.objects.get(name='Sohaib')})
