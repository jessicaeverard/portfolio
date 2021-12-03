"""portfolio URL Configuration

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
import jobs.views #must import app views file
from django.conf import settings 
from django.conf.urls.static import static #must import new urls


urlpatterns = [
    path('admin/', admin.site.urls), #admin on end of url, this will direct you to the admin page
    path('', jobs.views.homepage, name='home'), #url with nothing on the end of app url, go to views file with named function
    path('jobs/<int:job_id>', jobs.views.detail, name="detail"), #when you go into jobs with an integer that will be its id. With this, when you type localhost:8000/jobs/1 - the number should come up in the terminal and into the database. This is used when wanting to display a specific job
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 