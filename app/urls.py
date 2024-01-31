"""
URL configuration for job_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path

from app import views

urlpatterns = [
    
    path('', views.first),
    path('job_page/', views.job_page),
    path('about_page/', views.about_page),
    path('main_page/<int:job_id>/',views.main_page),
    path('main_page_job/<int:id>/',views.main_page_job),
    path('all_job/',views.all_job),
    path('fresher_only/',views.fresher_only),# means fresher and experience are mixed on ly job no intership
    path('intern_only/',views.intern_only),
     path('search_data/',views.search_data),
]
