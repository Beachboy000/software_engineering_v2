"""djangoProject1 URL Configuration

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
#from urlTest.views import showTemplate, post,main
from urlTest import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginPage),
    path('post/', views.post),
    path('goRegisterPage/', views.goRegistPage),
    path('regist/', views.regist),
    path('goMainPage/', views.goMainPage),
    path('goOurInfoPage/', views.goOurInfoPage),
    path('goDonatePage/', views.goDonatePage),
    path('goSearchPage/', views.goSearchPage),
    path('goHistoryPage/', views.goHistoryPage),
    path('goHelpPage/', views.goHelpPage),
    path('goReservePage/', views.goReservePage),
    path('borrow/', views.borrow),


]

"""
    path('urlTest/showTemplate/', showTemplate),
    path('urlTest/post/', post),
    path('urlTest/showTemplate/post', main),
    path('post/', post),
"""