from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy


# Create your views here.
class BlogListView(ListView):
    template_name = 'home.html'
    model = Post


class BlogDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
