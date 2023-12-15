from django import forms
from django.forms import widgets
from webapp.models import Tag, Article
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
# from django.core.validators import MinLengthValidator


# @deconstructible
# class MinLengthValidator(BaseValidator):
#     message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
#     code = 'too_short'
#
#     def compare(self, a, b):
#         return a < b
#
#     def clean(self, x):
#         return len(x)
#
#
# def at_least_5(value):
#     if len(value) < 5:
#         raise forms.ValidationError('Заголовок слишком короткий')


class ArticleForm(forms.ModelForm):
    # title = forms.CharField(max_length=50, required=True,
    #                         validators=[MinLengthValidator(4, message='Заголовок слишком короткий'), ],
    #                         label='Заголовок')
    # content = forms.CharField(max_length=3000, required=True, label='Контент', widget=widgets.Textarea())
    # author = forms.CharField(max_length=40, required=True, label='Автор')
    # tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), label='Теги', required=False)
    class Meta:
        model = Article
        fields = ('title', 'content', 'tags', 'author')
        # exclude = ()
        widgets = {'tags': forms.CheckboxSelectMultiple}
        error_messages = {
            'title': {
                'required': 'Please enter',
                'min_length': 'Заголовок слишком короткий'
                      }
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title == content:
            raise forms.ValidationError('Заголовок и Контент не могут быть одинаковые')
        return cleaned_data

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) < 5:
    #         raise forms.ValidationError('Заголовок слишком короткий')
    #     return title
