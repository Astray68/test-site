from django.contrib import admin
from .models import Category, Product, Promotion


class ProductInline(admin.TabularInline):
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_deleted')
    list_filter = ('is_deleted', )
    search_fields = ('name', )
    inlines = [ProductInline, ]

    def delete_model(self, request, obj):
        obj.my_delete()


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_deleted')
    list_filter = ('is_deleted', )
    search_fields = ('title', )

    def delete_model(self, request, obj):
        obj.my_delete()
