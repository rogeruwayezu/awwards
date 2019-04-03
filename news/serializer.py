from rest_framework import serializers
from .models import Profile, Post


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'profile_picture')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'title', 'landing_image', 'site_link')
