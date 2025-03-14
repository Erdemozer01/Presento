"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django_ckeditor_5.views import upload_file
from base.models import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path("ckeditor5/image_upload/", upload_file, name="ckeditor_upload_file"),
    path(r"images-handler/", include("galleryfield.urls")),
    path('', include('base.urls')),
    path('', include('post.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


try:
    site = Home.objects.latest('created')
    admin.site.site_title = site.name
    admin.site.site_header = site.name
    admin.site.index_title = site.name
    admin.site.name = site.name
except Home.DoesNotExist:
    pass