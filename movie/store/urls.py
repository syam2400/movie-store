"""
URL configuration for movie project.

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
from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    # path('',views.home,name='home'),
    path('', views.movielistview.as_view(), name='home'),
    # path("add_movie", views.add_movie, name='add_movie'),
    path("add_movie", views.createview.as_view(), name='add_movie'),
    # path('view_movie/<int:p>/', views.view_movie, name='view_movie'),
    path('view_movie/<int:pk>/', views.detailview.as_view(), name='view_movie'),

    path("edit_movie/<int:k>/", views.edit_movie, name="edit_movie"),
    path('delete/<int:pk>/', views.delete.as_view(), name='delete'),
    path('update', views.update_movie, name='update'),
    # path('signup',views.sign_up,name='signup')

]
