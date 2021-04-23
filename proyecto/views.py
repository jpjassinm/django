#DJANGO
from django.http import HttpResponse # En cada vista se requiere un (resquest) y se importa esta lib

#UTILIDADES
from datetime import datetime



#VISTAS
def hello_word(request): # a esto se le conoce como una vista, hay que recordar que cada vista en una funcion.
    return HttpResponse('Hola mundo, esto es una vista')

def mensaje_dia(request):
    #import pdb; pdb.set_trace()
    now = datetime.now().strftime('%d-%m-%Y  %H:%M:%S')
    return HttpResponse('Este es el mensaje del dia {now}'.format(now=str(now)))

def hi (request):
    number = [request.GET['numbers=10,20,30'].split(',')]
    #import pdb; pdb.set_trace() 
    return HttpResponse(str(numbers), content_type='application/json') #?numbers=10,520,25,2

def mensaje (request):
    print('Cuidado con lo que haces', content_type='application/json')
