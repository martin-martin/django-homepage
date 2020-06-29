from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.
class BlogList(generic.ListView):
    model = Post
    template_name = 'post_list.html'  # if not added to DIRS in settings.py, this would have to be 'blog/post_list.html'
    context_object_name = 'post_list'
