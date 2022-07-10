from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'show_in_footer', 'is_deleted',)
    list_filter = ('is_deleted', )
    search_fields = ('title', )

    def delete_model(self, request, obj):
        obj.my_delete()
