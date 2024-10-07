from django.db import models
import uuid 
from django.contrib.auth.models import User

class Product(models.Model): # model ini akan membuat table di database dengan nama Product
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.IntegerField()
    gold_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField()
    name = models.CharField(max_length=255)
    npm = models.CharField(max_length=255)
    kelas = models.CharField(max_length=255)
    
    def clean_product(self):
        self.gold_name = self.gold_name.strip()
        self.description = self.description.strip()
        self.price = self.price.strip()
        self.quantity = self.quantity.strip()
    

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5