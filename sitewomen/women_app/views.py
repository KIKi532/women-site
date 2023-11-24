from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import AddPostForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .utils import DataMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




class WomenHome(DataMixin, ListView):
    template_name = 'women_app/index.html'
    context_object_name = "posts"
    paginate_by = 6


    def get_context_data(self, *, object_list=None, **kwargs):
        return self.get_mixin_context(super().get_context_data(**kwargs),
                                      title='Головна сторінка',
                                      cat_selected=0
                                      )

    def get_queryset(self):
        return Women.objects.filter(is_published=Women.Status.PUBLISHED).select_related('cat')



@login_required
def about(request):
    return render(request, 'women_app/about.html',
                  {'title': 'Про сайт'})



class ShowPost(DataMixin, DetailView):
    template_name = 'women_app/post.html'
    context_object_name = 'post'
    model = Women
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'])

    def get_object(self, queryset=None):
        return get_object_or_404(Women, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women_app/addpage.html'
    title_page = 'Добавление статьи'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePage(LoginRequiredMixin, DataMixin, UpdateView):
    model = Women
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'women_app/addpage.html'
    success_url = reverse_lazy('home')
    title_page = 'Редактування статті'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise Http404("Цей пост не належить вам")
        return obj


def deletePage(request, slug):
    del_obj = Women.objects.get(slug=slug)
    del_obj.delete()
    return redirect('home')



def contact(request):
    return HttpResponse('Контакти')


class CategoryView(DataMixin, ListView):
    template_name = 'women_app/index.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 6


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context,
                                      title='Категория - ' + cat.name,
                                      cat_selected=cat.id,
                                      )

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=Women.Status.PUBLISHED).select_related('cat')




def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found hi</h1>")




class TagPostList(DataMixin, ListView):
    template_name = 'women_app/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title='Тег: ' + tag.tag)


    def get_queryset(self):
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

