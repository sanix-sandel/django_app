from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def homePage(request):
    menus=Menu.objects.all()
    context={'menus':menus}
    return render(request, './base.html', context)

def submenu(request, id):
    return HttpResponse(f'submenu {id}')    
