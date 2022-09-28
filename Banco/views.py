from django.shortcuts import render

# Create your views here.

def mostrarHogar(request):
    return render(request, 'Banco/index.html')

def mostrarGaleria(request):
    return render(request, 'Banco/galeria.html')

def mostrarRegistro(request):
    return render(request, 'Banco/registro.html')

def mostrarAbout(request):
    return render(request, 'Banco/about.html')

def mostrarConsultas(request):
    return render(request, 'Banco/consultas.html')

