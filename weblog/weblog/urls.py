from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('posts/', include(posts.urls))
]
