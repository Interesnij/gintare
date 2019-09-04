from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from a_category.models import ACategory
from main.models import LikeDislike
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField


class AMovie(models.Model):
    category=models.ForeignKey(ACategory,on_delete=models.CASCADE,verbose_name="Категория статей",null=True)
    title=models.CharField(max_length=100,verbose_name="Заголовок")
    description=models.CharField(max_length=300,blank=True,verbose_name="Краткое содержание")
    content=RichTextUploadingField(default='', verbose_name="Полное содержание")
    posted=models.DateTimeField(default=timezone.now,verbose_name="Опубликовано")
    tags=TaggableManager(blank=True,verbose_name="Теги")
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=timezone.now)
    views=models.IntegerField(default=0,verbose_name="Просмотры")
    image = models.ImageField(upload_to="orel_movie/%Y/%m/%d", blank=True)
    votes = GenericRelation(LikeDislike, related_query_name='articles')


    def get_absolute_url(self):
        return reverse('a_detail',kwargs={"pk":self.pk})

    def get_moovies(self):
        get_moovie=AMovie.objects.filter(category=self.category)
        return get_moovie

    class Meta:
        ordering=["-posted"]
        verbose_name="статья"
        verbose_name_plural="статьи"

    def __str__(self):
        return self.title

class AComment(models.Model):
    class Meta:
        db_table = "Комменты для статей"

    path = ArrayField(models.IntegerField())
    article_id = models.ForeignKey(AMovie, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, related_name="a_comment_user", on_delete=models.CASCADE)
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
