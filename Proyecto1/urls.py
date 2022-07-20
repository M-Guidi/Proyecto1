from django.contrib import admin
from django.urls import include, path

urlpatterns = [
 path('Proyecto1App/', include('Proyecto1App.urls')),
 path('admin/', admin.site.urls),
]
