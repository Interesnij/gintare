from django.contrib import admin
from movies.models import Movie, Comment

class MovieAdmin(admin.ModelAdmin):

    list_display = ['title','description','posted'] #все поля field.name in Blog._meta.fields
    #fields = []
    #exclude = []
    list_filter = ['posted']
    search_fields = ['title','description','posted']
    class Meta:
            model = Movie

class CommentAdmin(admin.ModelAdmin):

    list_display = ['article_id','author_id','content'] #все поля field.name in Blog._meta.fields
    #fields = []
    #exclude = []
    list_filter = ['posted']
    search_fields = ['article_id','author_id','content']
    class Meta:
            model = Comment

admin.site.register(Movie,MovieAdmin)
admin.site.register(Comment,CommentAdmin)
