from django.db import models
from django.urls import reverse

# Models

class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return f"{self.name}"

class BlogEntry(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    thumbnail_url = models.CharField(default=None, blank=True, null=True, max_length=500)
    pub_date = models.DateField()
    published = models.BooleanField(default=False)
    summary = models.TextField(default=None, blank=True, null=True)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.pub_date} - {self.title}"
