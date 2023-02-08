from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True)
    authors = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images")
