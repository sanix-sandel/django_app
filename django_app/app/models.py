from django.db import models
from django.urls import reverse


# Create your models here.
class Menu(models.Model):
    title=models.CharField(max_length=25, default='no title')

    def __str__(self):
        return f"{self.title}"

class SubMenu(models.Model):
    title=models.CharField(max_length=25, default='submenu with no title')
    menu=models.ForeignKey(Menu, related_name='submenu', on_delete=models.CASCADE)
    visited=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('submenu', args[self.id])