
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from landing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

