from django.contrib import admin
from news.models import New

class NewAdmin(admin.ModelAdmin):

    list_display = ['title','description','posted'] #все поля field.name in Blog._meta.fields
    #fields = []
    #exclude = []
    list_filter = ['posted']
    search_fields = ['title','description','posted']
    class Meta:
            model = New

admin.site.register(New,NewAdmin)
