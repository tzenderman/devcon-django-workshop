from django.conf.urls import (
    patterns,
    url,
)

import views

urlpatterns = [
    url(r'^(?P<blog_post_slug>[\w-]+)$', views.blog_post, name='blog-post'),
    url(r'^(?P<blog_post_slug>[\w-]+)/preview$', views.blog_post, {"preview": True}, name='blog-post-preview'),
    url(r'^$', views.blog, name='blog-home'),
]
