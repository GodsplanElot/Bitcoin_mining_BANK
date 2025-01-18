from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        default='profile_pictures/01.png',  # Path to your default avatar
        blank=True,
        null=True,
    )


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.profile_picture:
            img = Image.open(self.profile_picture.path)
            img = img.convert("RGB")  # Ensure it's in RGB format
            output_size = (300, 300)  # Desired size (300x300)
            img = img.resize(output_size, Image.Resampling.LANCZOS)
            img.save(self.profile_picture.path)

    def __str__(self):
        return f"{self.user.username}'s Profile"



