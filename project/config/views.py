from django.http import HttpResponse

def saludo(request):
	return HttpResponse("Hola Django - Coder")
def saludo_vista(request):
	return HttpResponse("<h1>Segunda vista</h1>")
def nombre(request, nombre: str, apellido: str):
	nombre= nombre.capitalize()
	apellido=apellido.capitalize()
	return HttpResponse(f"{apellido},{nombre}")
