from django.urls import path
from .views import home_page, detail, login_page

urlpatterns = [
    path('', home_page, name='home_url'),
    path('product/<int:pk>',detail, name='detail_url'),
    
    path('login/', login_page),
]   
