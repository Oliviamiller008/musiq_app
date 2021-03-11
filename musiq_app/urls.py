"""musiq_app URL Configuration

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
from musiq.views import homepage 
from musiq.views import question1
from musiq.views import question4
from musiq.views import question5

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage)
    path('question1', question1)
    path('question4', question4)
    path('question5', question5)
]
