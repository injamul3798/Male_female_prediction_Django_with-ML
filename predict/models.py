from django.db import models

# Create your models here.
class PredResults(models.Model):
        long_hair =  models.FloatField()
        forehead_width_cm =  models.FloatField()
        forehead_height_cm =  models.FloatField()
        nose_wide =  models.FloatField()
        nose_long =  models.FloatField()
        lips_thin =  models.FloatField()
        distance_nose_to_lip_long =  models.FloatField()

        gender = models.CharField(max_length=7)

        def __str__(self):
            return self.gender

'''
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)
    

    def __str__(self):
        return self.name   '''

