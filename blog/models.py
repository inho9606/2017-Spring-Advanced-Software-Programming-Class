from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField('TITLE', max_length=50)
	description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
	content=models.TextField('CONTENT')
	create_date=models.DateTimeField('Create Date', auto_now_add=True)
	modify_date=models.DateTimeField('Modify Date', auto_now=True)
	class Meta:
		verbose_name = 'post'
		verbose_name_plural = 'posts'
		db_table = 'my_post'
		ordering = ('-modify_date',)
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=(self.pk,))

	def get_previous_post(self):
		return self.get_previous_by_modify_date()

	def get_next_post(self):
		return self.get_next_by_modify_date()
