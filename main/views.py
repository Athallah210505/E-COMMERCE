from django.shortcuts import render, redirect
from main.models import Product
from main.forms import ProductEntryForm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'gold_name' : 'Gold 24K',
        'description': '24K Gold is pure gold. Even though it is called pure gold, 100% purity is unattainable, therefore “pure gold” refers to gold that is between 99.7% and 99.9% gold. Also known as fine gold, pure gold hasn’t been made stronger with other metals, therefore it maintains its rich yellow hue and is a lot softer than other types of gold. Because of this (and because it is so expensive), 24 karat gold jewelry is very rare in the United States. It is, however, a lot more popular in China, India and other Asian countries—especially for investment purposes. ',
        'quantity': '1',
        'price' : 'Rp.10.000.000',
        'name' : 'Athallah Nadhif',
        'npm' : '2306275651',
        'kelas' : 'PBP B',
        'product_entries': product_entries
    }
    return render(request,"main.html", context)

def create_product_entry(request):
        form = ProductEntryForm(request.POST or None)
        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect("main:show_main")
        context = {
            "form": form
        }
        return render(request, "create_product.html", context)

def show_xml (request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data= Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data_id = Product.objects.filter(pk=id)  # Use the id argument passed to the function
    return HttpResponse(serializers.serialize("xml", data_id), content_type="application/xml")

def show_json_by_id(request, id):
    data_id = Product.objects.filter(pk=id)  # Use the id argument passed to the function
    return HttpResponse(serializers.serialize("json", data_id), content_type="application/json")
