from django.conf.urls import url
from car import views
from django.contrib.auth import views as auth_views

app_name = 'api'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^parking/', views.parkingfunc, name='parking'),
    url(r'^search/', views.searchfunc, name='search'),
    # url(r'^login/', views.loginfunc, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'car/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'car/logout.html'}, name='logout'),
    # url(r'^index/', views.delfunc, name='.')
]
