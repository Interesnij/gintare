from django.db import models
from django.contrib.auth.models import User


class Guestbook(models.Model):
	user=models.ForeignKey(User, null=True, related_name="guest",
                                verbose_name='Пользователь', on_delete=models.CASCADE)
	posted=models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано")
	content=models.TextField(null=True,verbose_name="Содержание")
	class Meta:
			ordering=["-posted"]
			verbose_name="Запись гостевой книги"
			verbose_name_plural="Записи гостевой книги"

	def __str__(self):
		return self.content
