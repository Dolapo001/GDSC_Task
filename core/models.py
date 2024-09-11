import cloudinary.models
from .validators import validate_image
from .managers import *
from common.models import *


class User(AbstractBaseUser, BaseModel):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    profile_picture = cloudinary.models.CloudinaryField('image', blank=True, null=True, validators=[validate_image])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

