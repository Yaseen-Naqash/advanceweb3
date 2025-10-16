from django.contrib import admin
from .models import Blog, Writer, WebAdmin, User
# Register your models here.

class WriterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Writer, WriterAdmin)

class WebAdminAdmin(admin.ModelAdmin):
    pass
admin.site.register(WebAdmin, WebAdminAdmin)


class BlogAdmin(admin.ModelAdmin):

    list_display = ['views','title','rate' ,'created_at']

    search_fields = ['title', 'body', 'views']
    list_filter = ['author', 'created_at']

    readonly_fields = ['views']
    list_editable = ['rate']
    # fields = ['title', 'body']
    # exclude = []

    fieldsets = [
        (
            "متن بلاگ",
            {
                "fields": ["title", "body"],
            },
        ),
        (
            "اطلاعات بلاگ",
            {
                
                "fields": ["views", "rate"],
            },
        ),
        (
            "افراد",
            {
                
                "fields": ["author", "readers"],
            },
        ),
    ]
    

    pass

admin.site.register(Blog, BlogAdmin)
 