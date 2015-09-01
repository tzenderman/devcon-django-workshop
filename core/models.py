from django.core.urlresolvers import reverse
from django.db import models
from django.utils.timezone import now

import markdown
from django_markdown.models import MarkdownField


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

    def __unicode__(self):
        return u"Author - {}".format(self.full_name)

    @property
    def full_name(self):
        return u"{} {}".format(self.first_name, self.last_name).title()


class BlogCategory(models.Model):
    name = models.CharField(max_length=32, null=False)

    class Meta:
        verbose_name_plural = "Blog categories"

    def __unicode__(self):
        return u"Category - {}".format(self.name)


class BlogTag(models.Model):
    name = models.CharField(max_length=32, null=False)

    def __unicode__(self):
        return u"Tag - {}".format(self.name)


class BlogPost(models.Model):
    author = models.ForeignKey("Author", related_name="posts")
    title = models.CharField(max_length=32)
    body = MarkdownField()
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    categories = models.ManyToManyField("BlogCategory", related_name="posts")
    tags = models.ManyToManyField("BlogTag", related_name="posts")

    # SEO Stuff
    meta_title = models.CharField(max_length=70, null=True, blank=True, help_text="http://www.seomoz.org/learn-seo/title-tag")
    meta_description = models.CharField(max_length=155, null=True, blank=True, help_text="For tips, see http://www.seomoz.org/learn-seo/meta-description")

    published = models.BooleanField(default=False)
    publication_date = models.DateField(default=now)

    def __unicode__(self):
        return u"Post - {}".format(self.title)

    def get_absolute_url(self):
        if not self.published:
            return reverse("blog-post-preview", args=(self.slug,))

        return reverse("blog-post", args=(self.slug,))

    @property
    def formatted_body(self):
        return markdown.markdown(self.body)
