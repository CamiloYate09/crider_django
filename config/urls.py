"""Main URLs module."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
                  # Django Admin
                  path(settings.ADMIN_URL, admin.site.urls),
                  path('', include(('cride.circles.urls', 'circles'), namespace='circles')),
                  path('', include(('cride.circles.urls', 'users'), namespace='users')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
