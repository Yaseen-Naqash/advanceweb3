from django.db import models

# Create your models here.



class Blog(models.Model):
    
    title = models.CharField(max_length=127, null=True)
    body = models.TextField(max_length=2047, null=True, blank=True)
    views = models.IntegerField(null=True)
    rate = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    released_at = models.DateTimeField(null=True)
    is_active = models.BooleanField(null=True)

    author = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
    readers = models.ManyToManyField('Student', related_name='blogs') # add related_name to prevent errors

    image = models.ImageField(null=True)



    def __str__(self):
        return "title : " + self.title + " views : " + str(self.views)


class Student(models.Model):
    first_name = models.CharField(max_length=127, null=True)
    last_name = models.CharField(max_length=127, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name




    