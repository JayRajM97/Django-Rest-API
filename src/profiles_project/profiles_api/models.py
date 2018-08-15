from django.db import models
#Creating a cutom user model and override = Substituting Usermodel
from django.contrib.auth.models import AbstractBaseUser
#Allows us to add permissons on the specific users
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Helps Django to work with our custom user model"""
    def create_user(self, email, name, password= None):
        """Create a new user profile object"""
        if not email:
            raise ValueError("User Must have an email address.")
        email = self.normalize_email(email)
        #Creating a new user object
        user = self.model(email = email, name = name)
        user.set_password(password)
        user.save(using= self.db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with the given details."""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using= self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    #Dot String
    """Represents a "user profile" inside our system."""

    email = models.EmailField(max_length= 255, unique= True)
    name = models.CharField(max_length= 255)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Used to get full name of the User"""
        return self.name

    def get_short_name(self):
        """USed to get users short name"""
        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""
        return self.email




class ProfileFeedItem(models.Model):
    """Profile status update"""

    user_profile = models.ForeignKey('UserProfile', on_delete = models.CASCADE)
    status_text = models.CharField(max_length = 255)
    create_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
