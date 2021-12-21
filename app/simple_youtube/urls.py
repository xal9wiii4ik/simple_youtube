from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from simple_youtube import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
