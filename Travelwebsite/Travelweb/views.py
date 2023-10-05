from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')
def tour(request):
    return render(request,'tour.html')
def information(request):
    return render(request,'information.html')