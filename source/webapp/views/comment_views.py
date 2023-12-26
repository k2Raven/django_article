from django.views.generic import CreateView, UpdateView, DeleteView
from webapp.models import Comment, Article
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from webapp.forms import CommentForm


class CommentCreateView(CreateView):
    template_name = 'comments/comment_create.html'
    model = Comment
    # fields = ['text', 'author']
    form_class = CommentForm

    # def get_success_url(self):
    #     return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})
    #
    # def form_valid(self, form):
    #     article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
    #     form.instance.article = article
    #     return super().form_valid(form)

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        # form.save_m2m()
        return redirect('webapp:article_view', pk=article.pk)


class CommentUpdateView(UpdateView):
    template_name = 'comments/comment_update.html'
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})


class CommentDeleteView(DeleteView):
    model = Comment
    # template_name = 'comments/comment_delete.html'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})
