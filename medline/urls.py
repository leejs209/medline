"""medline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import medline.views as medline
import users.views as users

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', medline.home, name='home'),
    path('contact', medline.contact, name='contact'),
    path('consult/form', medline.consultform, name='consultform'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', users.signup, name='signup'),
    path('consult/history', medline.consulthistory, name='consulthistory'),
    path('consult/reserved', medline.consultreserved, name='consultreserved'),
    path('consult/form/submit', medline.get_consultform, name='get_consultform'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)