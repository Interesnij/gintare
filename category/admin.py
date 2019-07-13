from django.contrib import admin
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name','order'] #все поля field.name in Blog._meta.fields
    #fields = []
    #exclude = []
    #list_filter = ['posted']
    search_fields = ['name']
    class Meta:
            model = Category

admin.site.register(Category,CategoryAdmin)
