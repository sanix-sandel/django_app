from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return HttpResponse('home Page')

def submenu(request, id):
    return HttpResponse(f'submenu {id}')    
