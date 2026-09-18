from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, location, LocationInventory

#User
admon.site.register(User, UserAdmin)

#Configuration of user
@admin.register(location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_type')
    search_fields = ('name',)

#View of locations
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'classification', 'total_stock', 'is_active')
    search_fields = ('code', 'name')
    list_filter = ('is_active', 'product_type')

#View of inventary
admin.register(LocationInventory)
class LocationInventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'location', 'stock', 'price')
    list_filter = ('location')
    search_fields = ('product__name', 'product__code')
    list_filter = ('stock', 'price')