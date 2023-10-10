from django.contrib import admin

from fallout_shelter.models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'photo', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('price', 'created_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

