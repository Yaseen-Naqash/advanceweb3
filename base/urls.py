from django.urls import path
from .views import home_page, single, login_page

urlpatterns = [
    path('', home_page, name='home_url'),
    path('single/',single, name='single_url'),
    path('login/', login_page),
]   
