from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='HOME' ),
    path('services',views.services,name='SERVICES' ),
    path('about',views.about,name='ABOUT' ),
    path('contact',views.contact,name='CONTACT' ),
]