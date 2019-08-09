from django.db import models

# MODELS

class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return f"{self.name}"

class PortfolioEntry(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture_url = models.CharField(max_length=500)
    headline = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f"{self.headline}"

class AboutEntry(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    
    def __str__(self):
        return f"{self.title}"