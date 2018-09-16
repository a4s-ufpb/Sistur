from django.conf.urls import include, url
from django.contrib import admin
from api import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'sistur.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
  	url(r'^', include('api.urls')),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)