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
from pages.views import communities_networks
from pages.views import communities_churches
from pages.views import communities_forums
from pages.views import aboutus
from pages.views import food
from pages.views import healthcare
from pages.views import schools
from pages.views import events
from pages.views import spanish_home
from pages.views import spanish_aboutus
from pages.views import spanish_schools

urlpatterns = [
    path('admin/', admin.site.urls),
    path('communities/networks', communities_networks, name='communities_networks'),
    path('communities/churches', communities_churches, name='communities_churches'),
    path('communities/forums', communities_forums, name='communities_forums'),
    path('aboutus/', aboutus, name='aboutus'),
    path('food/', food, name='food'),
    path('healthcare/', healthcare, name='healthcare'),
    path('schools/', schools, name='schools'),
    path('events/', events, name='events'),
    path('', home, name='home'),
    path('spanish_home/', spanish_home, name='spanish_home'),
    path('spanish_aboutus/', spanish_aboutus, name='spanish_aboutus'),
    path('spanish_schools/', spanish_schools, name='spanish_schools'),
]
