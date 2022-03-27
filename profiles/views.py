from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
#from .models import

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def profiles(request):
    return render(request, 'profiles.html', {'pro': Profile.objects.all()})
