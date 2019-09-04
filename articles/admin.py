from django.contrib import admin
from articles.models import AMovie, AComment

class AMovieAdmin(admin.ModelAdmin):

    list_display = ['title','description','posted']
    list_filter = ['posted']
    search_fields = ['title','description','posted']
    class Meta:
            model = AMovie

class ACommentAdmin(admin.ModelAdmin):

    list_display = ['article_id','author_id','content']
    list_filter = ['posted']
    search_fields = ['article_id','author_id','content']
    class Meta:
            model = AComment


admin.site.register(AMovie,AMovieAdmin)
admin.site.register(AComment,ACommentAdmin)
