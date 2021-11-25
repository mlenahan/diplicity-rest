from django.contrib import admin
from .models import Announcement

@admin.action(description='Publish selected announcements')
def publish(model_admin, request, queryset):
    queryset.update(published=True)

@admin.action(description='Unpublish selected announcements')
def unpublish(model_admin, request, queryset):
    queryset.update(published=False)


class AnnouncementAdmin(admin.ModelAdmin):
    fields = ('title', 'subtitle', 'body')
    list_display = ('title', 'owner', 'created_at', 'published')
    actions = [publish, unpublish]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'owner', None) is None:
            obj.owner = request.user
        obj.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        user_is_manager = request.user.groups.filter(name='Manager').exists()
        if not user_is_manager:
            actions = dict()
        return actions

    def has_change_permission(self, request, obj=None):
        if obj:
            return request.user == obj.owner
        return True

admin.site.register(Announcement, AnnouncementAdmin)
