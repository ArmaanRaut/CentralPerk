from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from AUth.user_manager import UserManager

GENDER = ( ('Male', 'Male'), ('Female', 'Female'), ('other', 'other'), )

class User(AbstractBaseUser):
    username = models.CharField(max_length=20,unique=True, primary_key=True)
    full_name = models.CharField(max_length=50)
    birthdate = models.CharField(max_length=10)
    bio = models.TextField(max_length=300)
    gender = models.CharField(max_length=20, choices=GENDER)
    email = models.EmailField(max_length=255,unique=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    admin = models.BooleanField(default=False) # a superuser
    staff = models.BooleanField(default=False) # a admin user; non super-user
    active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.username

    def is_staff(self):
        return self.staff

    def is_admin(self):
        return self.admin
    
    def is_active(self):
        return self.active

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    objects = UserManager()