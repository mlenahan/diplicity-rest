from django.db import models


class Announcement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True, default='')
    body = models.TextField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
