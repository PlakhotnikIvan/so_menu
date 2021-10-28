from django.shortcuts import render
from django.http import HttpResponse


def so_menu(request):
    return render(request, 'main/so_menu.html')
