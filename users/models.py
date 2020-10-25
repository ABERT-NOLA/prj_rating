from django.db import models
from django.contrib.auth.models import User, AbstractUser
from PIL import Image
from django.utils.translation import gettext_lazy as _



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    contact = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)