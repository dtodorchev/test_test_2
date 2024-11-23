from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),  # Include profile app URLs
    path('album/', include('albums.urls')),  # Include album app URLs
]

