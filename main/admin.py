from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):

    list_display = ['name','email','message'] #все поля field.name in Blog._meta.fields
    #fields = []
    #exclude = []
    list_filter = ['name']
    search_fields = ['name']
    class Meta:
            model = Feedback

admin.site.register(Feedback,FeedbackAdmin)
