"""
URL configuration for videoflix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path,include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("__debug__/", include("debug_toolbar.urls")),
#     path('django-rq/', include('django_rq.urls')),
#     path('rq-dashboard/', include('rq_dashboard.urls')),
    
# ] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from content.views import video_list, stream
# from videoflix.settings import STATIC_ROOT, STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('django-rq/', include('django_rq.urls')),
    path('netflix/', video_list, name='video_list'),
    path('video/<int:pk>/', stream, name='stream'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   + static(settings.STATIC_URL_, document_root=settings.STATIC_ROOT)

