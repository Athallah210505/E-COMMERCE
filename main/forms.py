from django.forms import ModelForm
from main.models import Project


class ProjectEntryForm(ModelForm):
    class Meta:
        model = Project  #bisa jadi salah disini
        fields = ["gold_name", "price", "quantity", "description"]
    