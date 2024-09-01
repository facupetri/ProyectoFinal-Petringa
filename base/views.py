from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from base.models import *

def index(request):
    return render(request, 'base/index.html')

def acerca(request):
    return render(request, 'base/acerca.html')

class Post_lista(ListView):
    model = Post
    context_object_name = 'Post'
    template_name = 'base/listarpost.html'
    paginate_by = 6

class PostCreateView(CreateView):
    model = Post
    fields = ['titulo', 'posteo']
    template_name = 'base/crear_post.html'
    success_url = reverse_lazy('ListarPosts')
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class SearchResultsView(ListView):
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