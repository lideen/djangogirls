from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^credits/$', views.CreditReceiversView.as_view(), name='credits'),
]
