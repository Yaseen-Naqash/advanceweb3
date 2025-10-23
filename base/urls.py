from django.urls import path
from .views import home_page, single

urlpatterns = [
    path('', home_page, name='home_url'),
    path('single/',single, name='single_url')

]
