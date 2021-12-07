from announcements.models import Announcement
from announcements.serializers import AnnouncementSerializer
from rest_framework import generics


class ListAnnouncementsView(generics.ListAPIView):
    queryset = Announcement.objects.filter(published=True)
    serializer_class = AnnouncementSerializer
