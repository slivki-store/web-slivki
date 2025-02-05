from django.contrib import admin

from .models import Brand, Category, Product


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'pub_date', 'is_home')
    search_fields = ('title',)
    list_filter = ('title', 'category', 'brand', 'pub_date', 'is_home')
    ordering = ('-pub_date',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
