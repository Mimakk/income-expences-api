from django.db import models

# Create your models here.

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionMixin)

from django.db import models 


class UserManager(BaseUserManager):
    
    def create_user(self, username, email, password=None):
        
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a email')
        
        user=self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
    
    def create_superuser(self, username, email, password=None):
        
        if password is None:
            raise TypeError('Users should have a password')
        
        user=self.create_user(self,username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user