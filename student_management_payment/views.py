from django.shortcuts import render
from . forms import AddPaymentForm

# Create your views here.
def manage_payment(request):
    return  render(request, "payment_template/manage_payment_template.html")

def add_payment(request):
    form=AddPaymentForm()
    return render(request, "payment_template/add_payment_template.html", {"form":form})

def add_payment_save(request):
    pass