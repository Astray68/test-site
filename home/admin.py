from django.contrib import admin
from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_deleted', 'show_in_home')
    list_filter = ('is_deleted', )
    search_fields = ('title', )

    def delete_model(self, request, obj):
        obj.my_delete()
