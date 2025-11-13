from django.urls import path
from .views import home_page, detail, login_page,logout_command, sign_up

urlpatterns = [
    path('', home_page, name='home_url'),
    path('product/<int:pk>',detail, name='detail_url'),
    

    path('sign-up/',sign_up, name='signup_url'),
    path('login/',login_page, name='login_url'),
    path('logout/', logout_command, name='logout_url'),

]   
