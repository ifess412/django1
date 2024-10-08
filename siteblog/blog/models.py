from django.db import models
from django.urls import reverse

# Create your models here.


"""
Category
================
title, slug

Tag
================
title, slug

Post
================
title, slug, author, content, created_at, foto, views, category, tags

"""


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Категорія(ю)"
        verbose_name_plural = "Категорії"
        ordering = ["title"]


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["title"]


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано")
    foto = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    views = models.IntegerField(default=0, verbose_name="count_views")
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="posts"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"
        ordering = ["-created_at"]
