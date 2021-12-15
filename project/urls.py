from django.urls import path, include
from django.contrib import admin
from announcements.views import ListAnnouncementsView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'announcement', ListAnnouncementsView, basename='Announcement')

urlpatterns = [
    path('', include('announcements.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
