# blog/models.py
from django.db import models
from django.contrib.auth.models import User # Django's built-in User model
from django.urls import reverse # For get_absolute_url

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True) # For SEO friendly URLs

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish') # unique based on publish date
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True) # Optional: for post thumbnails

    class Meta:
        ordering = ['-publish'] # Newest posts first

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # This helps in creating links to individual posts
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments') # Can also be CharField for non-logged-in users
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False) # Admin approval for comments

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Comment by {self.author.username if self.author else "Guest"} on {self.post.title}'
