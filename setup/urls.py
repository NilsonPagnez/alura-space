from django.contrib import admin
from django.urls import path, include
from gallery.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gallery.urls'))
]
