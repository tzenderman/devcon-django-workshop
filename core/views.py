from django.shortcuts import (
    get_object_or_404,
    render,
)

from models import BlogPost


def blog(request):
    posts = BlogPost.objects.all()
    return render(request, "blog/index.html", {"posts": posts})


def blog_post(request, blog_post_slug, **kwargs):
    preview = kwargs.get("preview", False)
    if preview and request.user.is_staff:
        post = get_object_or_404(BlogPost, slug=blog_post_slug)
    else:
        post = get_object_or_404(BlogPost, slug=blog_post_slug, published=True)

    return render(request, "blog/post.html", {"post": post})
