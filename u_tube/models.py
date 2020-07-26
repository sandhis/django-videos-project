from django.db import models
from django.utils.timezone import now

# Create your models here.
class Video(models.Model):
    title = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='videos/')
    thumbnail = models.FileField(upload_to='video_thumb/', default='')
    pub_date = models.DateTimeField(default=now())  

    def __str__(self):
        return self.title
