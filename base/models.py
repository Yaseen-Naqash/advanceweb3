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
class Blog(models.Model):
    
    title = models.CharField(max_length=127, null=True, verbose_name='تیتر')
    body = models.TextField(max_length=2047, null=True, blank=True, verbose_name='متن بلاگ')
    views = models.IntegerField(null=True, verbose_name='نمایش')
    rate = models.FloatField(null=True, verbose_name='امتیاز')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ساخت')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ به روزرسانی')
    released_at = models.DateTimeField(null=True, verbose_name='تاریخ انتشار')
    is_active = models.BooleanField(null=True, verbose_name='منتشر شده')

    author = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, verbose_name='نویسنده', blank=True)
    readers = models.ManyToManyField('Person', related_name='blogs', blank=True, verbose_name='خواننده ها') # add related_name to prevent errors

    image = models.ImageField(null=True, blank=True, verbose_name='عکس')

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ ها'


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        print('hello world')
        return super().save(*args, **kwargs)


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


class Writer(Person):

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسنده ها'

class WebAdmin(Person):
    class Meta:
        verbose_name = 'منشی'
        verbose_name_plural = 'منشی ها'

class User(Person):
    pass



