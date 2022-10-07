from django import forms
from django.forms import ChoiceField
from .models import Students

class AddPaymentForm(forms.Form):
    
    student = forms.ModelChoiceField(label="Nombre", queryset=Students.objects.all() ,widget=forms.Select(attrs={"class":"form-control", "placeholder":"Nombre"}))
    amount = forms.FloatField(label="Importe", widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"0"}))
    payment_method_choices= [
        ("Efectivo","Efectivo"),
        ("Tarjeta Debito","Tarjeta Debito"),
        ("Tarjeta Crédito","Tarjeta Crédito"),
        ("Transferencia","Transferencia"),
        ("Deposito","Deposito")
    ]
    payment_method = forms.ChoiceField(label="Metodo de pago", choices=payment_method_choices, widget=forms.Select(attrs={"class":"form-control"}))
    payment_type_choices= [
        ("Mensualidad","Mensualidad"),
        ("Parcialidad","Parcialidad"),
        ("Inscripción","Inscripción"),
        ("Inscripción + Material","Inscripción + Material"),
        ("Material","Material"),
    ]
    payment_type = forms.ChoiceField(label="Tipo de pago", choices=payment_type_choices, widget=forms.Select(attrs={"class":"form-control"}))
    details = forms.CharField(label="Detalles",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Detalles"}), help_text="Opcional", required=False)
