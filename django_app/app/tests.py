from django.test import TestCase
from .models import Menu, SubMenu

class CustomMenuTest(TestCase):
    def test_create_menu(self):
        menu=Menu.objects.create(
            title='title 1'
        )
        self.assertEqual(menu.title, 'title 1')

    def test_create_submenu(self):
        menu=Menu.objects.create(title='title 1')
        submenu=SubMenu.objects.create(
            menu=menu, 
            title='submenu 1'
        ) 
        self.assertEqual(submenu.title, 'submenu 1')
        self.assertEqual(submenu.menu.title, 'title 1')   



