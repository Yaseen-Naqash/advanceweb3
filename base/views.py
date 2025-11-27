from django.shortcuts import render, redirect
from .models import Product, ProductFeatures, Person
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    sizes = request.GET.getlist('size')
    feature_ids = request.GET.getlist('feature')


    products_list = Product.objects.filter( Q(title__icontains = q) | Q(details__icontains=q))

    if sizes:
        products_list = products_list.filter(size__in=sizes)

    # ####### or feature filters logic
    if feature_ids:
        print(feature_ids)
        x = ProductFeatures.objects.filter(id__in=feature_ids)
        products_list = products_list.filter(productFeatures__in=x)

    # ####### and feature filters logic
    # if feature_ids:
    #     for feature_id in feature_ids:
    #         products_list = products_list.filter(productFeatures=feature_id)   
    
    paginator = Paginator(products_list, 16)
    page = request.GET.get('page') if request.GET.get('page') else 1

    products = paginator.get_page(page)

    features =  ProductFeatures.objects.all()


    context = {
        'products':products,
        'features':features,
    }

    return render (request, 'index.html', context)



@login_required
def detail(request,pk):

    product = Product.objects.get(id=pk)
    feature_ids = product.productFeatures.values_list('id', flat=True)

    similar_product = Product.objects.filter(productFeatures__in=feature_ids).exclude(id=product.id)[:4]

    context = {
        'product':product,
        'similar_products': similar_product,
    }

    return render(request, 'detail.html', context)







def login_page(request):


    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user is not None :
            login(request, user)
            messages.success(request, 'you are logged in')
            return redirect('home_url')
        else:
            messages.error(request, 'username or password is incorrect!')
            return redirect('login_url')






    return render(request, 'login.html')

def sign_up(request):

    

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm-password')

        if password1 != password2:
            messages.error(request,'password does not match!')
            return redirect('signup_url')  


        user = Person.objects.create(
            username = username,
            email = email,
            password=password1
        )
        # user.set_password(password1)
        user.save()

    return render(request, 'signup.html')


def logout_command(request):
    logout(request)
    return redirect('login_url')


def examsignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        print(username)
        print(email)

        print(pass1)

        print(pass2)
        

        if pass1 != pass2:
            return JsonResponse('error password does not match')

        user = Person.objects.create(
            username = username,
            email = email,
            password = pass1
        )
        user.set_password(pass1)
        user.save()

    return render(request, 'midexam.html')


def examlogin(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        print(username)
        print(pass1)

        user = authenticate(username=username, password = pass1)
        if user is not None:
            login(request, user)
        else:
            return JsonResponse('username or password incorrect')

        
    return render(request, 'midexam.html')


def testblock(request):
    return render(request, 'test_base_block.html')