from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    authors = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images")
    category = models.ManyToManyField(Category)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title)
