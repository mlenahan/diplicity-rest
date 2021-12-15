from rest_framework import serializers
from announcements.models import Announcement, AnnouncementImage
from django.contrib.auth.models import User

class AnnouncementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementImage
        fields = [
            'id',
            'image',
        ]

class AnnouncementSerializer(serializers.ModelSerializer):
    inline_images = AnnouncementImageSerializer(source='announcementimage_set', many=True)
    class Meta:
        model = Announcement
        fields = [
            'id',
            'title',
            'subtitle',
            'body',
            'created_at',
            'image',
            'inline_images',
        ]
