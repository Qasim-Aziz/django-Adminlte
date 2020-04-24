from django.conf.urls import url
from admind.views import index, home,display_emp, display_card,add_emp
urlpatterns= [
    url(r'^$' , index, name='index'),
    url(r'^home/$', home, name='home'),
    url(r'^home/display_emp/$', display_emp, name='home/display_emp'),
    url(r'^add_emp/$', add_emp, name='add_emp')
    

]