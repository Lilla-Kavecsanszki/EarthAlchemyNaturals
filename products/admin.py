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
        'skin_types',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SkinTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SkinType, SkinTypeAdmin)
