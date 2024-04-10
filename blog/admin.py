from django.contrib import admin
from .models import categoria, post

# Register your models here.
class CategortiaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')



admin.site.register(categoria, CategortiaAdmin)
admin.site.register(post)