from django.urls import path, include
from . import views as views

urlpatterns=[
    path('', views.homePage, name='home'),
    path('<int:id>', views.submenu, name='submenu')
]

