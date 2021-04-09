from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
# Create your models here.

class Trending(models.Model):
    image = models.CharField(max_length=2343, blank='True')
    title = models.CharField(max_length=233)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(max_length=20000)
    slug = models.SlugField(max_length=225,unique=True, blank='True')
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=233)
    

    def __str__(self):
        return self.title + '!!' + str(self.author)

    def save(self):
        value = self.title
        self.slug = slugify( value, allow_unicode=True)
        super().save()

    def get_absolute_url(self):
        return reverse('detail_view_trending', kwargs={'slug': self.slug})

class Latest(models.Model):
    image = models.CharField(max_length=2343, blank='True')
    title = models.CharField(max_length=233)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(max_length=20000)
    slug = models.SlugField(max_length=225,unique=True, blank='True')
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=233)

    def __str__(self):
        return self.title + '!!' + str(self.author)

   
    def save(self):
        value = self.title
        self.slug = slugify( value, allow_unicode=True)
        super().save()

    def get_absolute_url(self):
        return reverse('detail_view_latest', kwargs={'slug': self.slug})

class Featured(models.Model):
    image = models.CharField(max_length=2343, blank='True')
    title = models.CharField(max_length=233)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(max_length=20000)
    slug = models.SlugField(max_length=225,unique=True, blank='True')
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=233)

    def __str__(self):
        return self.title + '!!' + str(self.author)

    
    def save(self):
        value = self.title
        self.slug = slugify( value, allow_unicode=True)
        super().save()

    def get_absolute_url(self):
        return reverse('detail_view_featured', kwargs={'slug': self.slug})

class Deals(models.Model):
    image = models.CharField(max_length=2343, blank='True')
    link = models.CharField(max_length=2345, blank='True')
    name = models.CharField(max_length=233)
    description = models.CharField(max_length=233)
    rate = models.CharField(max_length=233)

    def __str__(self):
        return self.name 
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver