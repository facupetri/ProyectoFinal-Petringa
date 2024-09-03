from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from base.models import *

class IndexView(ListView):
    model = Post
    template_name = 'base/index.html'
    context_object_name = 'Post'
    ordering = ['-fecha_creacion']
    paginate_by = 6 

def acerca(request):
    return render(request, 'base/acerca.html')

class Post_lista(ListView):
    model = Post
    context_object_name = 'Post'
    template_name = 'base/listarpost.html'
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.all().order_by('-fecha_creacion')

class Post_detail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'base/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'posteo', 'imagen']
    template_name = 'base/crear_post.html'
    success_url = reverse_lazy('ListarPosts')
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class SearchResultsView(LoginRequiredMixin, ListView):
    model = Post
    template_name= 'base/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(autor__icontains=query)

def blog_view(request):
    posts = Post.objects.all()
    mid_index = len(posts) // 2
    first_column_posts = posts[:mid_index]
    second_column_posts = posts[mid_index:]

    context = {
        'first_column_posts': first_column_posts,
        'second_column_posts': second_column_posts,
    }
    return render(request, 'base/listarpost.html', context)