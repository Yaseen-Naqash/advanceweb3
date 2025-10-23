from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def home_page(request):

    products_list = Product.objects.all()
    x = Paginator(products_list, 16)

    page = request.GET.get('page') if request.GET.get('page') else 1

    products = x.get_page(page)
    context = {
        'products':products,
    }

    return render (request, 'index.html', context)




def single(request):

    return render(request, 'single.html')

def login_page(request):
    return render(request, 'login.html')