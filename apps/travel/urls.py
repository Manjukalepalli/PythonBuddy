from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.main),
    url(r'^Registration$',views.Registration),
    url(r'^travel$', views.travel),
    url(r'^login$',views.login),
    url(r'^addplan$', views.addplan),
    url(r'^addnewplan$',views.addnewplan),
    url(r'^show/(?P<travel_id>\d+)$', views.show),
    url(r'^add_plan_to_user/(?P<travel_id>\d+)$', views.add_plan_to_user)
   ]