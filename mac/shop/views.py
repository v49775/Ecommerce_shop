from django.shortcuts import render
from django.http import HttpResponse
from .models import my_product
from math import ceil

# Create your views here.
def index(request):
    # products = my_product.objects.all()
    # print(products)
    # n = len(products)
    # nslides = n//4 + ceil((n/4)-(n//4))
    # param = {'product':products,'no_of_sildes':nslides,'range':range(1,nslides)}
    # allprods = [[products,range(1,len(products)),nslides],
    #             [products,range(1,len(products)),nslides]]

    allprods = []
    catprods = my_product.objects.values('category','id')
    cats = { item['category'] for item in catprods}
    for cat in cats:
        prod = my_product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nslides),nslides])


    param = {'allprods':allprods}
    return render(request,'shop/index.html',param)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("we are at Contact")

def search(request):
    return HttpResponse("we are at Search")

def tracker(request):
    return HttpResponse("we are at Tracker")

def productView(request):
    return HttpResponse("we are at Product View")

def checkout(request):
    return HttpResponse("we are at Checkout")
