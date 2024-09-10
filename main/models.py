from django.db import models

class MoodEntry(models.Model):
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()
    price = models.IntegerField()
    gold_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField()
    name = models.CharField(max_length=255)
    npm = models.CharField(max_length=255)
    kelas = models.CharField(max_length=255)
    
    

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5