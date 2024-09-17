from django.db import models
import uuid 

class Product(models.Model): # Moodn
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.IntegerField()
    gold_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField()
    name = models.CharField(max_length=255)
    npm = models.CharField(max_length=255)
    kelas = models.CharField(max_length=255)
    

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5