from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    ''' The table for categories '''
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Subject(models.Model):
    ''' The table for subjects '''
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subject_posts")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    banner_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Comments(models.Model):
    ''' The table for comments '''
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subjects")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_posts")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_date']
