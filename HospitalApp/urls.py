
from django.contrib import admin
from django.urls import path
from HospitalApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('starter/',views.starter,name='starter'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('departments/',views.departments,name='departments'),
    path('doctors/',views.doctors,name='doctors'),
]
