from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default="nonImage.png",blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.likes.count()
