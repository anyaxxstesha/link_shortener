from django.contrib import admin

from links.models import Link


@admin.register(Link)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_url', 'short_url', 'created_at')
    list_filter = ('id', 'created_at')
    search_fields = ('id',)
    ordering = ('-created_at',)
