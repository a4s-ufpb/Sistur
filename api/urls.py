from django.conf.urls import include, url
from django.contrib import admin
from api import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'sistur.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^addEvent/', views.addEvent, name='addEvent'),
    url(r'^addUser/', views.addUser, name='addUser'),
    url(r'^login/', views.logar, name='login'),
    url(r'^rest/events/', views.EventsRest.as_view()),
     url(r'^logout/', views.logout_view, name='logout'),
  	url(r'^', views.home, name='home'),
]

