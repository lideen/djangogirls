from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^credits/$', views.ContributorListView.as_view(), name='credits'),
]
