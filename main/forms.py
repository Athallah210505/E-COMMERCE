from django.forms import ModelForm
from main.models import Product


class ProductEntryForm(ModelForm):
    class Meta:
        model = Product  #bisa jadi salah disini
        fields = ["gold_name", "price", "quantity", "description"]
    