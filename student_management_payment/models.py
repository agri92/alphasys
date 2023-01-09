from django.db import models
from student_management_app.models import Students
from django.db.models.functions import Coalesce
from django.db.models import Sum, Value, FloatField
from datetime import timedelta, datetime

# Create your models here.

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    payment_type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default='0.00')
    payment_method = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    @property
    def fecha_hoy(self):
        fecha_hoy = datetime.today()
        return fecha_hoy

    @property
    def total_pagado(self):
        total_pagado = Payment.objects.filter(student=self.student).aggregate(total=Coalesce(Sum('amount'), Value(0), output_field=FloatField()))
        return total_pagado

    @property
    def por_pagar(self):
        por_pagar = self.student.course_id.costo_total
        return por_pagar

    @property
    def proximo_pago(self):
        proximo_pago = self.created_at + timedelta(days=31)
        return proximo_pago

    @property
    def dias_vigentes(self):
        dias_vigentes = self.proximo_pago.date() - self.fecha_hoy.date()
        return dias_vigentes.days

    @property
    def Active(self):
        if self.proximo_pago.date() > self.fecha_hoy.date():
            return 'Pagado'
        elif self.proximo_pago.date() == self.fecha_hoy.date():
            return 'Por vencer'
        else:
            return 'Vencido'

