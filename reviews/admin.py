from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_posted', 'status', 'is_deleted')
    list_filter = ('is_deleted', )
    search_fields = ('name', )

    def delete_model(self, request, obj):
        obj.my_delete()
