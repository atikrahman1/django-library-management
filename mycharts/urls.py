"""mycharts URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from dashboard.views import *

from user.views import *

from register.views import *
from mycharts import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home_screen_view, name="home"),
                  path('register', register_view, name="register"),
                  path('login', login_view, name="login"),
                  path('logout', logoutUser, name="logout"),
                  path('user/profile', user_profile, name="user_profile"),
                  path('user/book', book_operation, name="book_delete"),
                  path('search', search, name="search"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
