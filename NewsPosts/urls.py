"""NewsPosts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from User import views as UserViews
from rest_framework.authtoken.views import obtain_auth_token
from Posts import views as PostViews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViews.PostViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/hello', UserViews.HelloView.as_view(), name='hello'),
    path('user/api-token-auth', obtain_auth_token, name='api_token_auth'),
    path('user/register', UserViews.RegisterUser.as_view(), name='register'),
    path('', include(router.urls))
]
