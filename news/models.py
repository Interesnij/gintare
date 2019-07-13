from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils import timezone
from django.contrib.sitemaps import Sitemap

class New(models.Model):
	title=models.CharField(max_length=100,verbose_name="Заголовок")
	description=models.CharField(max_length=300,verbose_name="Краткое содержание")
	content=models.TextField(verbose_name="Полное содержание")
	posted=models.DateTimeField(default=timezone.now, db_index=True, verbose_name="Опубликована")
	image=models.ImageField(upload_to="new/list",verbose_name="Изображение")
	user=models.CharField(max_length=100, verbose_name="Автор новости")
	views=models.IntegerField(default=0,verbose_name="Просмотры")

	def save(self,*args,**kwargs):
		try:
			this_record=New.objects.get(pk=self.pk)
			if this_record.image != self.image:
				this_record.image.delete(save=False)
		except:
			pass
		super(New,self).save(*args,**kwargs)
	def delete(self,*args,**kwargs):
		self.image.delete(save=False)
		super(New,self).delete(*args,**kwargs)

	def get_absolute_url(self):
		return reverse('news_detail',kwargs={"pk":self.pk})

	class Meta:
		ordering=["-posted"]
		verbose_name="новость"
		verbose_name_plural="новости"
	def __str__(self):
		return self.title

class NewSitemap(Sitemap):
	changefreq = "daily"
	priority = 0.5

	def items(self):
		return New.objects.all()

class StaticSitemap(Sitemap):
    priority = 0.6
    changefreq = 'never'

    def items(self):
        return ['about', 'main', 'good_categories_edit', 'contact']

    def location(self, item):
        return reverse(item)
