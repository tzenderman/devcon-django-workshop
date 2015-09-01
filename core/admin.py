from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from models import (
    Author,
    BlogCategory,
    BlogPost,
    BlogTag,
)


class BlogPostAdmin(MarkdownModelAdmin):
    fieldsets = [
        (None, {"fields": ["author", "title", "body", "slug"]}),
        ("Categorizing", {"fields": ["categories", "tags"]}),
        ("SEO", {"fields": ["meta_title", "meta_description"]}),
        ("Publishing", {"fields": ["published", "publication_date"]})
    ]

admin.site.register(Author)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory)
admin.site.register(BlogTag)
