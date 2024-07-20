from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManger()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name'] #Defining which fields are required, above we made username as required field

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name
    def get_short_name(self):
        """Retrive short name of user"""
        return self.name
    def __str__(self):
        """Return String Representation of a user"""
        return self.email
        
