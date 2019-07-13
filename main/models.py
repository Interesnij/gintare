from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models import Sum
from django.contrib.auth.models import User


class Feedback(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение', max_length=500)
    class Meta:

        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
    def __str__(self):
        return 'Имя: {}'.format(self.name)


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)

    def articles(self):
        return self.get_queryset().filter(content_type__model='movie').order_by('-articles__posted')
    def comments(self):
        return self.get_queryset().filter(content_type__model='comment').order_by('-comments__posted')

    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField(verbose_name="Голос", choices=VOTES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()
