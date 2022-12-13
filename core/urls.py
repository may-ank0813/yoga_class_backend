from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.hello),
    path('user/' , include('core.user.urls')),
    path('enroll/' , include('core.batch.urls')),
]