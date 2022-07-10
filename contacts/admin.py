from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'message', 'is_deleted')
    list_filter = ('is_deleted', )
    search_fields = ('email', )

    def delete_model(self, request, obj):
        obj.my_delete()
