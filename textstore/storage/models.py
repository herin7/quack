from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class UserSpace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #
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
    
    # Updated max_length for text_content
    text_content = models.TextField(max_length=500, blank=True, null=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    
    # file_content is optional, so it’s okay to leave it blank or null
    file_content = models.FileField(upload_to='user_uploads/', blank=True, null=True)

    def __str__(self):
        return self.title
