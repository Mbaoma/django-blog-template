from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        "title": "Saku's Blog",
        "author": "Sakura-chan",
        "content": "First post content",

    },
    {
        "title": "Saku's Bento",
        "author": "Sakura-chan",
        "content": "Obento ski des"
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
