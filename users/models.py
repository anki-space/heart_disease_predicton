from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    dob = models.DateField(null=True,blank=True)
    Hospital_name = models.CharField(blank=True,max_length=100)

class Profile_result(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    temperature = models.FloatField()
    heart_rate = models.FloatField()
    cholesterol = models.FloatField()
    blood_sugar = models.FloatField()
    systolic = models.FloatField()
    diastolic = models.FloatField()
    symptoms = models.CharField(max_length=100,default='None')
    existing_conditions = models.CharField(max_length=100,default='None')
    family_history = models.CharField(max_length=100,default='No')
    smoking_status = models.CharField(max_length=100,default='Never')
    laboratory_results = models.CharField(max_length=100,default='None')
    prediction = models.CharField(max_length=100,default='None')
    created_at = models.DateTimeField(auto_now_add=True)
    