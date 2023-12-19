from django import forms
from webapp.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'tags', 'author')
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


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
