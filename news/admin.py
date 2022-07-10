from django.contrib import admin
from .models import New


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'slug', 'is_deleted', 'show_in_home')
    list_filter = ('is_deleted', )
    search_fields = ('title', )

    def delete_model(self, request, obj):
        obj.my_delete()
