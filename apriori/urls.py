from django.conf.urls import url
from apriori import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    ]