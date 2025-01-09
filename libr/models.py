import datetime

from django.db import models

from users.models import User


class Author(models.Model):

    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', null=True, blank=True)
    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    death_date = models.DateField(verbose_name='Дата смерти', null=True, blank=True)

    def __str__(self):
        return f'Author: {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


class Book(models.Model):

    title = models.CharField(max_length=150, verbose_name='Название')

    authors = models.ManyToManyField(Author, verbose_name='Авторы', blank=True)
    year = models.PositiveIntegerField(verbose_name='Год издания', null=True, blank=True)
    genre = models.CharField(max_length=150, verbose_name='Жанр', null=True, blank=True)

    def __str__(self):
        return f'Book: {self.title}'

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'


class Reading(models.Model):

    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    start_date = models.DateTimeField(verbose_name='Дата выдачи книги', default=datetime.datetime.now())
    is_returned = models.BooleanField(verbose_name='Книга возвращена?', default=False)

    def __str__(self):
        return f'Reading: {self.book} / {self.user}'

    class Meta:
        verbose_name = 'запись о чтении книги'
        verbose_name_plural = 'записи о чтении книг'
