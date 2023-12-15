from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from webapp.models import Article
from webapp.forms import ArticleForm
from django.views.generic import View, TemplateView, FormView


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, 'index.html', {'articles': articles})


class ArticleView(TemplateView):
    template_name = 'article_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=kwargs.get('pk'))
        return context


class ArticleCreateView(FormView):
    template_name = 'article_create.html'
    form_class = ArticleForm
    # success_url = reverse_lazy('index')

    # def get_success_url(self):
    #     return reverse('article_view', kwargs={'pk': self.article.pk})

    def form_valid(self, form):
        tags = form.cleaned_data.pop('tags')
        self.article = Article.objects.create(
            title=form.cleaned_data.get('title'),
            content=form.cleaned_data.get('content'),
            author=form.cleaned_data.get('author'),
        )
        self.article.tags.set(tags)
        return redirect('article_view', pk=self.article.pk)


class ArticleUpdateView(FormView):
    template_name = 'article_update.html'
    form_class = ArticleForm

    def dispatch(self, request, *args, **kwargs):
        self.article = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Article, pk=self.kwargs.get('pk'))

    def get_initial(self):
        # initial = {
        #     'title': self.article.title,
        #     'content': self.article.content,
        #     'author': self.article.author,
        #     'tags': self.article.tags.all()
        # }
        initial = {}

        for key in 'title', 'content', 'author':
            initial[key] = getattr(self.article, key)

        initial['tags'] = self.article.tags.all()

        return initial

    def form_valid(self, form):
        tags = form.cleaned_data.pop('tags')
        self.article.title = form.cleaned_data.get('title')
        self.article.content = form.cleaned_data.get('content')
        self.article.author = form.cleaned_data.get('author')
        self.article.tags.set(tags)
        self.article.save()
        return redirect('article_view', pk=self.article.pk)



class ArticleDeleteView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        return render(request, 'article_delete.html', {'article': article})

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        article.delete()
        return redirect('index')
