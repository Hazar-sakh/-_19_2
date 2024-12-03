from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новость'
        ordering = ['-created_at']




class Team(models.Model):
    title = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    age = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.title}, {self.city}'


class Player(models.Model):
    first_name = models.CharField(max_length=30, default='Ivan')
    patronymic = models.CharField(max_length=30, default='Ivanovich')
    family = models.CharField(max_length=30, default='Ivanov')
    city = models.CharField(max_length=30, default='Burevestnik')
    age = models.IntegerField(default=18, max_length=3)
    teams = models.ManyToManyField(Team, related_name='teams', default=None)

    def __str__(self):
        lst = list(self.first_name)
        return f'{self.family} {lst[0]}. - {self.city}'
