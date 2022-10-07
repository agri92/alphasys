from django.urls import path
from student_management_payment import views

urlpatterns = [
    path('manage_payment', views.manage_payment, name="manage_payment"),
    path('add_payment', views.add_payment, name="add_payment"),
]
