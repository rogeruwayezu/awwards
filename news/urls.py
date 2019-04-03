from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/new', views.create_profile, name='profileView'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'^post/new', views.create_post, name='postNew'),
    url(r'^index', views.index, name='allProjects'),
    url(r'^project/(\d+)', views.single_project, name='singleProject'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile/(\d+)', views.view_profile, name='profileView'),


    # url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    # url(r'^api/merch/$', views.MerchList.as_view())
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
