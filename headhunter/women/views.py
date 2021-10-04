from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


# menu = ['News', 'Contacts', 'Blog', 'Information', 'Enter']

menu = [ {'title': 'About', 'url_name':'about'},
         {'title': 'News', 'url_name':'news'},
        {'title': 'Contacts','url_name':'contacts'},
        {'title': 'Blog', 'url_name' :'blog'},
        {'title': 'Enter', 'url_name' :'enter'}]

def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    d = {
        'posts': posts,
        'cats': cats,
        'menu':menu,
        'title':'Home page',
        'cat_selected':0,
    }
    return render(request, 'women/index.html', context=d)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About page'})

def news(request):
    return HttpResponse('news')

def contacts(request):
    return HttpResponse(f'<h1>contacts</h1>')

def blog(request):
    return HttpResponse(f'<h1>blog</h1>')

def enter(request):
    return HttpResponse(f'<h1>enter</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    d = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected':post.cat_id,
    }
    return render(request, 'women/post.html', context = d)

# def show_category(request, cat_id):
#     return HttpResponse(f'Category = {cat_id}')


def show_category(request,cat_id):
    posts = Women.objects.filter(cat_id = cat_id)
    cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()
    d = {
        'posts': posts,
        'cats': cats,
        'menu':menu,
        'title':'Category',
        'cat_selected':cat_id,
    }
    return render(request, 'women/index.html', context=d)

# def categories(request, cat):
#     if(request.POST):
#         print(request.POST)
#     return HttpResponse(f'<h1>Categories for name</h1><p>{cat}</p>')
#
# def archive(request, year):
#     if int(year) > 2020:
#        #raise Http404()
#        return redirect('home', permanent=False)
#     return HttpResponse(f'<h1>Archive for year</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')