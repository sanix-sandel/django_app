from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

def homePage(request):
    menus=Menu.objects.all()
    context={'menus':menus}
    return render(request, './home.html', context)

def submenu(request, id):
    submenu=get_object_or_404(SubMenu, id=id)
    context={'submenu':submenu}
    return render(request, './submenu.html', context)  
