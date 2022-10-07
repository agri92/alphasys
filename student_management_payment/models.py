from django.db import models
from student_management_app.models import Students

# Create your models here.

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default='0.00')
    payment_method = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
