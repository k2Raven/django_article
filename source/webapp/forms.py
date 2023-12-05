from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label='Заголовок')
    content = forms.CharField(max_length=3000, required=True, label='Контент', widget=widgets.Textarea())
    author = forms.CharField(max_length=40, required=True, label='Автор')
