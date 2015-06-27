from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.movie_list),
	url(r'^movie/(?P<pk>[0-9]+)/$', views.movie_detail),
]
