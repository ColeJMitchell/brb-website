"""
URL configuration for src project.

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
from django.urls import path
from pages.views import home
from pages.views import communities
from pages.views import aboutus
from pages.views import food
from pages.views import healthcare
from pages.views import schools
from pages.views import events
from pages.views import spanish_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('communities/', communities, name='communities'),
    path('aboutus/', aboutus, name='aboutus'),
    path('food/', food, name='food'),
    path('healthcare/', healthcare, name='healthcare'),
    path('schools/', schools, name='schools'),
    path('events/', events, name='events'),
    path('', home, name='home'),
    path('spanish_home/', spanish_home, name='spanish_home'),
]
