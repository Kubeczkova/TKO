"""
URL configuration.

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
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

from django.conf.urls.static import static
from django.conf import settings

from tko.views import ContactView, NewArticleListView, AllArticleListView, EventListView, GalleryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include("shop.urls")),
    path('create-contact/', ContactView.as_view(), name='create-contact'),
    path('load-articles/', NewArticleListView.as_view(), name='load-articles'),
    path('load-all-articles/', AllArticleListView.as_view(), name='load-all-articles'),
    path('load-events/', EventListView.as_view(), name='load-events'),
    path('load-gallery/', GalleryView.as_view(), name='load-gallery'),
] + debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)