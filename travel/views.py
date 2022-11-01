from django.http import HttpResponse
from django.shortcuts import render


def home(requwst):
    name = 'Bob'
    return render(requwst, 'home.html', {'name': name})
