from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
#from .models import

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

# SMA: Every funcion == 1 page
def profiles(request):
    ctx = {
            # Set spacific element by ID
            'pro': Profile.objects.get(id=2),
            # Set spacific element by name
            'soo': Profile.objects.get(name='Sohaib'),
            ## Get all from db
            'all': Profile.objects.all(),
            # filter
            'f': Profile.objects.all().filter(),
            # order_by
            'o': Profile.objects.all().order_by('price'),
            # get only the count of elements in the database
            'count': Profile.objects.all().count(),
            # exclude
            'exclude': Profile.objects.all().exclude(name='Sohaib'),
            # exact filter
            'exact': Profile.objects.all().filter(name__exact='Sohaib'),
    }
    return render(request, 'profiles.html', ctx)
