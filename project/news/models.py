from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class News(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=150,)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 default=1, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('home', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новасть'
        verbose_name_plural = 'Новасти'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150,
                             db_index=True,
                             verbose_name='Категория',
                             )

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

