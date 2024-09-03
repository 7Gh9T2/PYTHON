from django.shortcuts import render

def agregar_localidad(request):
    return render(request, 'form.html')  
