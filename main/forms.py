from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product  #bisa jadi salah disini
        fields = ["gold_name", "price", "quantity", "description",]
    