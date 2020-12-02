
# Django imports

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)


class CustomUserManager(BaseUserManager):
    """
     Este manager nos permitira crear
     usuarios y super usuarios
    """
    
    def create_user(self , **kwargs):
        """
         Crea un usuario normal
        """
        user = self.model(
            name=kwargs['name'],
            description=kwargs['description'],
            email=kwargs['email'],
            userPage=kwargs['userPage'],
        )
        user.set_password(kwargs['password'])
        user.save(using=self._db)
        return user


    def create_superuser(self , **kwargs):
        """
         Crea un super usuario
        """
        userInstance = self.create_user(**kwargs)
        userInstance.is_staff = True
        userInstance.is_superuser = True
        userInstance.save(using=self._db)
        return userInstance


class User(AbstractBaseUser,PermissionsMixin):

    """
     Este es un modelo perzonalizado
     de usuarios
    """

    objects = CustomUserManager()

    name = models.CharField(
        max_length=100,
        null=False,
        default=''
    )

    description = models.TextField(null=True , default='')
    email = models.EmailField(null=False , unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    userPage = models.URLField(null=True)

    profileImage = models.ImageField(
        upload_to='image',
        default='',
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name' , 'description' , 'userPage']


    def __str__(self):
        return self.email


    

    







