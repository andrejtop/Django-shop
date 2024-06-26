from django.contrib import admin

from .models import Categories, Products

# admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'quantity', 'category')
    prepopulated_fields = {'slug': ('name',)}







