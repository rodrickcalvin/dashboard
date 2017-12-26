from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.advert_list, name='advert_list'),
]
