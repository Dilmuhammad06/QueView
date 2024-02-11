from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='media/thumbnails/')
    video = models.FileField(upload_to='media/videos/')
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name
