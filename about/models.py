from django.db import models
from cloudinary.models import CloudinaryField

class About(models.Model):
    """
    Stores a single about me text.
    """
    profile_image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Stores a single collabotatiion request message.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"