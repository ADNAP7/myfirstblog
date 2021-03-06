"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from article import views
from my_blog import testdb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testdb',testdb.testdb),
    # path('',views.home),
    # path('<int:my_args>/',views.detail,name='detail'),        #r'^(?P<my_args>d+)/$'不知为何不行    '<int:my_args>/' 将访问的浏览器地址的参数传给函数detail
    path('test/',views.test),
    path('',views.home,name='home'),
    path('<id>/',views.detail,name='detail'),                                                       #{% url "detail" id=post.id %}将参数先由正则表达式取出，再传到函数detail
]
