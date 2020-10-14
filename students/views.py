from django.shortcuts import render, redirect
from .models import Student
from .form import StudentDetailForm
# Create your views here.
def home(request):
     form = StudentDetailForm( request.POST or None)
     if request.method == 'POST':
          obj = form.save(commit=False)
          obj.save()
          return redirect(f'../')
     context = {
          'form' : form
     }
     return render(request, 'home.html', context)

def info(request):
     name = request.META['QUERY_STRING'][5:]
     print('\n', request.META['QUERY_STRING'], '\n')
     context = {
          'object': Student.objects.get(Name = name)
     }
     return render(request, 'info.html', context)