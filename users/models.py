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
    patient_id = models.CharField(max_length=20, blank=True)
    patient_name = models.CharField(max_length=100, blank=True)
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

 
    def save(self, *args, **kwargs):
        if not self.patient_id:
            last_id = Profile_result.objects.all().order_by('id').last()     
            if last_id is None or "Pid" not in str(last_id.patient_id) :
                new_id = 1        
            else:
                new_id = int(last_id.patient_id.split('_')[-1]) + 1
            self.patient_id = f"Pid_{new_id:04d}"
        super().save(*args, **kwargs)
