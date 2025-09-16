# my_blog_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static # <<< Yeh import kiya hua hai
from django.conf import settings         # <<< Yeh import kiya hua hai

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # PICHLE FIX KE LIYE
]

# Development mode mein static aur media files serve karne ke liye
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # >>> Yeh line add karein:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    