from django.http import HttpResponse

# Create your views here.
def hello(request): #Se define una función para retornar un mensaje al cliente request es un parametro que sirve para recibir información del cliente
    return HttpResponse("<h1>Hola mundo</h1>")
def about(request):
    return HttpResponse("Texto")