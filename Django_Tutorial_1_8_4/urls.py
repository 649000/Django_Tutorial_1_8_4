"""Django_Tutorial_1_8_4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#TODO: This is the main URL governing the entire project.
#Add new URL for each app, by using the includes function
# Each app should have their own url file.
#polls.url where polls is the name of the app followed the name of the urlconf file.


#The url() function is passed four arguments, two required: regex and view, and two optional: kwargs, and name.
#name is used as an identifier, especially in your templates/html



urlpatterns = [
    #The regex does not end with $ which defines end of string match but rather it's opended.
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
