from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    contact = models.CharField(max_length = 10, default = "Not entered")
    address = models.CharField(max_length=50, default = "Not entered")
    Gcode = models.CharField(max_length = 5, default = "Not entered")

    def __str__(self):
        return f'{ self.user.username } user'

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.image.path)