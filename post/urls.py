from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import blog_view,detail_view


urlpatterns = [
    path('',blog_view ,name='post_list'),
    path('post/<slug:slug>/', detail_view, name="post_detail"),
]

    