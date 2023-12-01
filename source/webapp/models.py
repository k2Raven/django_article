from django.db import models


class TypeArticle(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок", unique=True)
    description = models.TextField(max_length=400, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.id}. {self.title}'


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Контент')
    author = models.CharField(max_length=40, default='Неизвестный', verbose_name="Автор")
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    type = models.ForeignKey('webapp.TypeArticle',
                             on_delete=models.RESTRICT,
                             verbose_name='Тип',
                             related_name='articles',
                             null=True)

    def __str__(self):
        return f'{self.id}. {self.title}'
