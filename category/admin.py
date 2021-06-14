from django.contrib import admin
from .models import Category 
# from django.contrib.admin.models import ModelAdmin
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','slug']
    prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(Category,CategoryAdmin)