from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django_jalali.db import models as jmodels
from django.contrib.auth.hashers import make_password
# Create your models here.


phone_validator = RegexValidator(
    regex=r'^\d+$',
    message="Phone number must contain only digits"
)
class Product(models.Model):

    SIZE = [
        ('0','XXL'),
        ('1','XL'),
        ('2','L'),
        ('3','M'),

    ]
    
    title = models.CharField(max_length=127, null=True, verbose_name='عنوان')
    details = models.TextField(max_length=2047, null=True, blank=True, verbose_name='توضیحات')
    price = models.IntegerField(null=True, verbose_name='قیمت')
    size = models.CharField(max_length=1 ,choices=SIZE , null=True, verbose_name='سایز')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ساخت')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ به روزرسانی')
    is_active = models.BooleanField(null=True, verbose_name='منتشر شده')
    image = models.ImageField(null=True, blank=True, verbose_name='عکس')
    productFeatures = models.ManyToManyField('ProductFeatures', related_name='products')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def __str__(self):
        return self.title

class ProductFeatures(models.Model):
    title = models.CharField(max_length=127, null=True, verbose_name='عنوان')


class Person(AbstractUser):

    phone = models.CharField(max_length=13, null=True, validators=[phone_validator], verbose_name='تلفن')
    code = models.CharField(max_length=13, null=True, verbose_name='کد ملی')
    birthDate = jmodels.jDateTimeField(null=True, verbose_name='تاریخ تولد')


    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'شخص'
        verbose_name_plural = 'اشخاص'


    def __str__(self):
        return self.first_name + " " + self.last_name






