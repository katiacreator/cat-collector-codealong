from django.shortcuts import render
from .models import Cat

# Add the following import
# from django.http import HttpResponse-NOT USING IT AFTER UPDATING HOME FUNCTION IN PT 2


# Define the home view
def home(request):
  return render(request, 'home.html')
  
# Define the about view
def about(request):
   return render(request, 'about.html')


# Define the all cats view
def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })