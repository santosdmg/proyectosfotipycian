from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'spotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'', include('userprofiles.urls')),
    url(r'', include('artists.urls')),
    url(r'', include('tracks.urls')),
    url(r'', include('albums.urls')),

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
