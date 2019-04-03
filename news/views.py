# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Profile, Post, Rating
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .email import send_welcome_email
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, PostForm

# Create your views here.


def home(request):
    '''
    View function to create and update the profile of the user
    '''
    all_projects = Post.objects.all()

    return render(request, 'all-news/home.html', {'all_projects': all_projects})


def index(request):
    '''
    View function to create and update the profile of the user
    '''

    all_projects = Post.objects.all()

    return render(request, 'all-news/all-projects.html', {'all_projects': all_projects})


def single_project(request, project_id):
    '''
    View function to create and update the profile of the user
    '''

    project = Post.objects.get(id=project_id)
    return render(request, 'all-news/single-project.html', {'project': project})


@login_required()
def create_profile(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = current_user
            new_profile.save()
            # print(new_profile.fields.profile_picture)
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'all-news/profile-new.html', {"form": form})


@login_required()
def view_profile(request, profile_id):
    '''
    function for displaying the profile of the logged in user
    '''
    try:
        current_user = request.user
        profile = Profile.objects.get(id=profile_id)
        my_projects = Post.objects.filter(user=current_user.id).all()
        return render(request, 'my-profile.html', {"profile": profile, "current_user": current_user, "my_projects": my_projects})
    except ValueError:
        raise Http404()


@login_required()
def create_post(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = current_user
            new_post.save()
            # print(new_profile.fields.profile_picture)
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'all-news/new-project.html', {"form": form})


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Post.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'all-news/search.html', {
            "message": message,
            "articles": searched_projects
        })

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html', {"message": message})


# def newsletter(request):
#     name = request.POST.get('your_name')
#     email = request.POST.get('email')

#     recipient = NewsLetterRecipients(name=name, email=email)
#     recipient.save()
#     send_welcome_email(name, email)
#     data = {'success': 'You have been successfully added to mailing list'}
#     return JsonResponse(data)


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)


class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Post.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
