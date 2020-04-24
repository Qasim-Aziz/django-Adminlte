from django.conf.urls import url
from .views import *

urlpatterns= [
    url('home', userhome),
    url('login/', login_view),
    url('register/',register_view),
    url('logout/',logout_view)

    
]