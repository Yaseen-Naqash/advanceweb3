from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def home_page(request):

    products_list = Product.objects.all()

    paginator = Paginator(products_list, 16)

    page = request.GET.get('page') if request.GET.get('page') else 1



    products = paginator.get_page(page)
    context = {
        'products':products,
    }

    return render (request, 'index.html', context)




def detail(request,pk):
    print(pk)

    product = Product.objects.get(id=pk)

    context = {
        'product':product,
    }

    return render(request, 'detail.html', context)

def login_page(request):
    return render(request, 'login.html')