"""
URL configuration for E_Commerse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from . import views
#for file uploading .......................
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('login/',views.login),
    path('email/',views.email),
    path('resetpassword/<token>',views.resetpassword),
    path('register/',views.register),
    path('productdetails/',views.productdetails),
    path('customer/',include("CustomerApp.urls")),
    path('ecommerseadmin/',include("AdminApp.urls")),
]+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)