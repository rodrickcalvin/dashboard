from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.advert_list, name='advert_list'),
url('', include('social.apps.django_app.urls', namespace='social')),

]
