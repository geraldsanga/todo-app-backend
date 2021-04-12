from django.contrib.auth.models import AbstractUser
from django.models import Model

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='users/', null=True)
    phone_number = models.CharField(max_length=20)
    dob = models.DateField(null=True)
    