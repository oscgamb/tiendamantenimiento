from django.contrib import admin
from .models import categoriaProd, Producto

# Register your models here.
class CategoriaprodAdmin(admin.ModelAdmin):
    readonly_fields=("created","update")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","update")

admin.site.register(categoriaProd, CategoriaprodAdmin)
admin.site.register(Producto, ProductoAdmin)