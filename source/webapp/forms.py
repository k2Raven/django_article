from django import forms
from webapp.models import Article, Comment
from django.utils.translation import gettext_lazy as _


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'tags', )
        widgets = {'tags': forms.CheckboxSelectMultiple}
        error_messages = {
            'title': {
                'required': _('Please enter'),
                'min_length': _('Заголовок слишком короткий')
            }
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title == content:
            raise forms.ValidationError(_('Заголовок и Контент не могут быть одинаковые'))
        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label=_('Найти'))
