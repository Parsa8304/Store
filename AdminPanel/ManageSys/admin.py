from django.contrib import admin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')
    search_fields = ('name',)
    list_filter = ('price', 'image')
    ordering = ('-price',)  # Orders by price in descending order


admin.site.register(Product, ProductAdmin)
