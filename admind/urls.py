from django.conf.urls import url
from admind.views import index, home,display_emp, display_card
urlpatterns= [
    url('^$' , index, name='index'),
    url('^home/$', home, name='home'),
    url('^home/display_emp$', display_emp, name='home/display_emp'),
    

]