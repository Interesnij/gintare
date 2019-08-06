from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.urls import reverse
from category.models import Category
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from main.models import LikeDislike
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField


class Movie(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Категория",null=True)
    title=models.CharField(max_length=100,verbose_name="Заголовок")
    description=models.CharField(max_length=300,blank=True,verbose_name="Краткое содержание")
    content=RichTextUploadingField(default='', verbose_name="Полное содержание")
    link=models.CharField(max_length=200,null=True,blank=True,verbose_name="Ссылка на видео в Youtube")
    posted=models.DateTimeField(default=timezone.now,verbose_name="Опубликовано")
    tags=TaggableManager(blank=True,verbose_name="Теги")
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=timezone.now)
    views=models.IntegerField(default=0,verbose_name="Просмотры")
    image = models.ImageField(upload_to="movies/%Y/%m/%d", verbose_name="Главное изображение")
    votes = GenericRelation(LikeDislike, related_query_name='articles')


    def get_absolute_url(self):
        return reverse('movies_detail',kwargs={"pk":self.pk})

    def get_moovies(self):
        get_moovie=Movie.objects.filter(category=self.category)
        return get_moovie

    def request(request):
        return {'request': request}

    class Meta:
        ordering=["-posted"]
        verbose_name="ролик"
        verbose_name_plural="ролики"

    def __str__(self):
        return self.title

class Comment(models.Model):
    class Meta:
        db_table = "comments"

    path = ArrayField(models.IntegerField())
    article_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, related_name="comment_user", on_delete=models.CASCADE)
    content = models.TextField('Комментарий')
    posted = models.DateTimeField('Дата комментария', default=timezone.now)
    votes = GenericRelation(LikeDislike, related_query_name='comments')

    def __str__(self):
        return self.content[0:200]

    def get_offset(self):
        level = len(self.path) - 1
        if level > 2:
            level = 2
        return level

    def get_col(self):
        level = len(self.path) - 1
        if level > 2:
            level = 2
        return 12 - level
