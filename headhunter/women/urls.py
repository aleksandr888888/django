from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('contacts/', contacts, name='contacts'),
    path('blog/', blog, name='blog'),
    path('enter/', enter, name='enter'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),


]