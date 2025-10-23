from django.shortcuts import render
from .models import Product
# Create your views here.

def home_page(request):

    products = Product.objects.all()

    context = {
        'products':products,
    }

    return render (request, 'index.html', context)




def single(request):

    return render(request, 'single.html')