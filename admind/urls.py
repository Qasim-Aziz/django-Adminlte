from django.conf.urls import url
from .views import index, home
urlpatterns= [
    url('' , index, name='index'),
    url('home/', home, name='home')
]