from cgitb import html
from urllib import request
from django.shortcuts import render

# Create your views here.

def acount(request):
    return render(request, "Cuentas/cuenta.html")

