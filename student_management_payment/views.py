from django.shortcuts import render
from . forms import AddPaymentForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from student_management_payment.models import Payment

# Create your views here.
def view_collection(request,collection_id):
    collection=Payment.objects.get(id=collection_id)
    return render(request, "collection_template/view_collection_template.html", {"collection":collection,"id":collection_id})

def manage_collection(request):
    collection = Payment.objects.filter(payment_type='mensualidad').order_by('student', '-created_at')
    return render(request, "collection_template/manage_collection_template.html", {"collection":collection})

def manage_payment(request):
    payments = Payment.objects.all()
    return  render(request, "payment_template/manage_payment_template.html", {"payments":payments})

def add_payment(request):
    if request.method == 'POST':
        form=AddPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added Payment")
            return HttpResponseRedirect(reverse("add_payment"))
        else:
            messages.error(request, "Failed to Add Payment")
            return HttpResponseRedirect(reverse("add_payment"))
    else:
        form=AddPaymentForm(request.POST)
    return render(request, "payment_template/add_payment_template.html", {"form":form})