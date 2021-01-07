'''from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    print("You are in homepage view")
    return HttpResponse("<h1>HomePage</h1><br><p>SKNCOE</p>")
    #return HttpResponse("<h1>Homepage<\h1>")

def index(request):
    print("IT is a index page")
    return HttpResponse("<h1>ffff</h1>")
'''
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def product_view1(request):
    print("IT is a view page")
    return HttpResponse("<h1>product1</h1>")
def product_view2(request):
    print("IT is a view page")
    return HttpResponse("<h1>product2</h1>")
def product_view3(request):
    print("IT is a view page")
    return HttpResponse("<h1>product3</h1>")
def product_view4(request):
    print("IT is a view page")
    return HttpResponse("<h1>product4</h1>")