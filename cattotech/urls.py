"""
URL configuration for cattotech project.

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
from cattotech import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 

    
    path('newpassword/', views.newpassword),
    path('reset/', views.reset),
    path('otp/', views.OTP),
    
    path('', views.home, name="home"),
    path('pcbuilderpage/', views.pcbuilderpage),
    path('bloghome/', views.bloghome),
    path('guide1/', views.guide1),
    path('guide2/', views.guide2),
    path('guide3/', views.guide3),
    path('prebuilt1/', views.prebuilt1),
    path('prebuilt2/', views.prebuilt2),
    path('prebuilt3/', views.prebuilt3),


    path('product/',include("product.urls")),
    path('purchase/', views.purchase,name="purchase"),

]

