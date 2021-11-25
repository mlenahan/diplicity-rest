from rest_framework import serializers
from announcements.models import Announcement
from django.contrib.auth.models import User


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = [
            'id',
            'title',
            'subtitle',
            'body',
            'created_at',
        ]
