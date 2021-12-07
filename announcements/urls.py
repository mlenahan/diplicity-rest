from django.urls import path, include
from announcements import views

urlpatterns = [
    path('announcements/', views.ListAnnouncementsView.as_view(), name='list-announcements'),
]