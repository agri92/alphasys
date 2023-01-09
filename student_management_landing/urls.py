from django.urls import path
from student_management_landing import views

urlpatterns = [
    path('home', views.landing, name="home"),
]
