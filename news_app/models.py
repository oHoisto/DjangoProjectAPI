from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    media_file = models.FileField(
        upload_to='news_media/',
        blank=True,
        null=True
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def is_image(self):
        if self.media_file:
            return self.media_file.name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))
        return False

    def is_video(self):
        if self.media_file:
            return self.media_file.name.lower().endswith(('.mp4', '.webm', '.ogg'))
        return False