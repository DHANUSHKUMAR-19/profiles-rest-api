from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManger(BaseUserManager):
    """manager for User Profiles"""

    def creat_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have a email address")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)# it is a standard for saving objects in django
        return user
    def create_superuser(self,email,name,password=None):
        """Create a new Super user profile"""
        user=self.creat_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)# it is a standard for saving objects in django
        return user

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
