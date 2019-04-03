# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
from django.db import models
from django.contrib.auth.models import User
# from multiselectfield import MultiSelectField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to='profiles/')

    @classmethod
    def get_profiles(cls):
        '''
        Fucntion that gets all the profiles in the app
        Return
        '''
        profiles = Profile.objects.all()
        return profiles


class Post(models.Model):
    title = models.TextField(max_length=100, null=True, blank=True)
    landing_image = models.ImageField(upload_to='photos/', null=True)
    site_link = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, related_name='posts')
    post_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-post_date']

    def save_post(self):
        '''Method to save an image in the database'''
        self.save()

    @classmethod
    def get_posts(cls):
        '''
        Method that gets all image posts from the database
        Returns:
            images : list of image post objects from the database
        '''
        posts = Post.objects.all()
        return posts

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects


# class Article(models.Model):
#     title = models.CharField(max_length=60)
#     post = models.TextField()
#     editor = models.ForeignKey(Editor)
#     tags = models.ManyToManyField(tags)
#     pub_date = models.DateTimeField(auto_now_add=True)
#     article_image = models.ImageField(upload_to='articles/')

#     @classmethod
#     def todays_news(cls):
#         today = dt.date.today()
#         news = cls.objects.filter(pub_date__date=today)
#         return news

#     @classmethod
#     def days_news(cls, date):
#         news = cls.objects.filter(pub_date__date=date)
#         return news

#     @classmethod
#     def search_by_title(cls, search_term):
#         news = cls.objects.filter(title__icontains=search_term)
#         return news


# class NewsLetterRecipients(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField()


# class MoringaMerch(models.Model):
#     name = models.CharField(max_length=40)
#     description = models.TextField()
#     price = models.DecimalField(decimal_places=2, max_digits=20)

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', null=True)
    post = models.ForeignKey(Post, related_name='ratings', null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    usability = models.FloatField(default=0.00, null=True)
    design = models.FloatField(default=0.00, null=True)
    creativity = models.FloatField(default=0.00, null=True)
    content = models.FloatField(default=0.00, null=True)
    mobile = models.FloatField(default=0.00, null=True)
