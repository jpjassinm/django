from django.shortcuts import render # este es la lib que se debe importar para los template
from django.http import HttpResponse
# Create your views here.


def list_posts(request):
    posts=[1,2,3]
    return HttpResponse(str(post))


def list_posts(request):
    return render(request, 'index.html')
