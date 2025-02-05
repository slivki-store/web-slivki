from django.contrib import admin

from home.models import HomeBanner

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'is_home')
    search_fields = ('title',)
    list_filter = ('title', 'number', 'is_home')


admin.site.register(HomeBanner, BannerAdmin)
