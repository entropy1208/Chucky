from __future__ import absolute_import


from django.conf.urls import url


from . import views


from djangoratings.views import AddRatingFromModel


urlpatterns = [
    url(r'^category/(?P<slug>[-\w]+)/$',
        views.VideoCategoryDetailView.as_view(),
        name='video_category_detail'),
    url(r'^home/$',
        views.HomeView.as_view(),
        name='home'),
    url(r'^video/(?P<slug>[-\w]+)/$',
        views.VideoDetailView.as_view(),
        name='video_detail'),
    url(r'video/rate/(?P<object_id>\d+)/(?P<score>\d+)/', AddRatingFromModel(),
        {'app_label': 'videos',
         'model': 'video',
         'field_name': 'rating'},
        name='rate_video'),
]
