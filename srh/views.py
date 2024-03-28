from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pat(request):
    return render(request,'patcummins.html')

def klassen(request):
    return HttpResponse('<h1> Classic Kalssen...!!!!</h1>')
