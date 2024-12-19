from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from cloudinary.models import CloudinaryField

class UserSpace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    custom_url = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Space"

class StoredContent(models.Model):
    CONTENT_TYPES = [
        ('text', 'Text'),
        ('file', 'File'),
    ]
    userspace = models.ForeignKey(UserSpace, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content_type = models.CharField(choices=CONTENT_TYPES, max_length=50)
    text_content = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    # Changed to CloudinaryField for file storage
    file_content = CloudinaryField('file_content', 
                                 resource_type='auto',  # Allows any file type
                                 blank=True, 
                                 null=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Changed to CloudinaryField for image storage
    photo = CloudinaryField('profile-pic',
                          folder='profile-pics',  # Organizes images in Cloudinary
                          transformation={  # Optional: Add image transformations
                              'width': 300,
                              'height': 300,
                              'crop': 'fill'
                          },
                          blank=True,
                          null=True)
    bio = models.TextField(blank=True, null=True, default="No bio provided")
    
    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()