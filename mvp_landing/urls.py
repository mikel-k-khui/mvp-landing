"""mvp_landing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import (path, re_path)

# TODO: add lib for static assets per documentation -> https://docs.djangoproject.com/en/3.0/howto/static-files/
from django.conf import settings
from django.conf.urls.static import static

# views from components
from emails.views import (
    email_entry_get,
    email_entry_create_view
)

urlpatterns = [
    path('', email_entry_create_view),
    re_path(r'email/(?P<id>\d+)/$', email_entry_get),
    # url(r'email/(?P<id>\d+)/$', email_entry_get),
    # path('email/<int:id>/', email_entry_get)
    path('admin/', admin.site.urls),
]

# TODO: static asset setting for dev vs. prod
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)