"""scraper_pj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from environment import get_env

urlpatterns = [
    path('admin/', admin.site.urls),
]
print(f'django.db.backends.{get_env().DB_DATABASE_TYPE}',)
print(get_env().DB_DATABASE)
print(get_env().DB_USE)
print(get_env().DB_PASSWORD)
print(get_env().DB_HOST)
print(get_env().DB_PORT)