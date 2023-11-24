from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Article(models.Model):
    # title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок", choices=status_choices)
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Контент')
    author = models.CharField(max_length=40, default='Неизвестный', verbose_name="Автор")
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return f'{self.id}. {self.title}'
