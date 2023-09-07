from django.contrib import admin
from .models import Category, SkinType, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'member_price',
        'display_skin_types',
        'image',
    )

    ordering = ('sku',)

    def display_skin_types(self, obj):
        return ", ".join([str(skin_type) for skin_type in obj.skin_types.all()])

    display_skin_types.short_description = 'Skin Types'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SkinTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SkinType, SkinTypeAdmin)
