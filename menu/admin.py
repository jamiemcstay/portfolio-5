from django.contrib import admin
from .models import MenuItem, Category


class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        # 'category',
        'price',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category, CategoryAdmin)
