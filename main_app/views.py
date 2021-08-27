from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
  
# Define the about view
def about(request):
   return render(request, 'about.html')

# Define the all cats view
def cats_index(request):
   return render(request, 'cats.html')