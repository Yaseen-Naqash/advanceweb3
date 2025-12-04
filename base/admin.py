from django.contrib import admin
from .models import Product, ProductFeatures, Comment, Person, Rating
# Register your models here.

admin.site.register(ProductFeatures)
admin.site.register(Comment)
admin.site.register(Person)
admin.site.register(Rating)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['title', 'price', 'size' ,'created_at']

    search_fields = ['title', 'details', 'price']
    list_filter = ['size', 'created_at']

    # readonly_fields = ['price']
    # list_editable = ['siez']
    # fields = ['title', 'body']
    # exclude = []

    # fieldsets = [
    #     (
    #         "متن بلاگ",
    #         {
    #             "fields": ["title", "body"],
    #         },
    #     ),
    #     (
    #         "اطلاعات بلاگ",
    #         {
                
    #             "fields": ["views", "rate"],
    #         },
    #     ),
    #     (
    #         "افراد",
    #         {
                
    #             "fields": ["author", "readers"],
    #         },
    #     ),
    # ]
    

    pass

admin.site.register(Product, ProductAdmin)
 