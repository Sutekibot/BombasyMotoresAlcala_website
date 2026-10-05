from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Location, LocationInventory

admin.site.register(User, UserAdmin)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_type')
    search_fields = ('name',)

class LocationInventoryInline(admin.TabularInline):
    model = LocationInventory
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'model', 'name', 'category', 'manufacturer', 'is_active')
    search_fields = ('code', 'model', 'name')
    list_filter = ('is_active', 'manufacturer', 'category')
    inlines = [LocationInventoryInline]

@admin.register(LocationInventory)
class LocationInventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'location', 'stock', 'price')
    list_filter = ('location',)
    search_fields = ('product__name', 'product__code', 'product__modelo')
    list_editable = ('stock', 'price')