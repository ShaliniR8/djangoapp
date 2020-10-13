from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
     context = {}
     return render(request, 'home.html', context)

def info(request):
     name = request.META['QUERY_STRING'][5:]
     print('\n', request.META['QUERY_STRING'], '\n')
     context = {
          'object': Student.objects.get(Name = name)
     }
     return render(request, 'info.html', context)