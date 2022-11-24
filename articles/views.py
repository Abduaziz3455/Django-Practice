from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
# Create your views here.
from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):  # new
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'  # new


class ArticleDetailView(LoginRequiredMixin, DetailView):  # new
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'  # new


class ArticleUpdateView(LoginRequiredMixin, UpdateView):  # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_update.html'
    login_url = 'login'  # new

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, DeleteView):  # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'  # new

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    # permission
    def form_valid(self, form):  # new
        form.instance.author = self.request.user
        return super().form_valid(form)
