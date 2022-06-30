"""config URL Configuration

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
from django.urls import path,include

#config/urls.pyに全てのアプリのパスを書いているようでは煩雑になってしまう。
#各アプリの詳細なパスは各アプリごとにurls.pyを作って、それをincludeする仕様にすると良い。
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("student_management.urls")),

    path('accounts/', include('allauth.urls')),
]
