from django import forms
from .models import Student
class StudentDetailForm(forms.ModelForm):
     class Meta: 
          model = Student
          fields = ['Name','Roll', 'Uni', 'GPA']

