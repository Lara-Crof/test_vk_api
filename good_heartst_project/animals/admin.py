from django.contrib import admin
from .models import MainAnimals, Category


@admin.register(MainAnimals)
class MainAnimalsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',
                    'is_publish', 'category', 'slug', 'category_id')
    list_filter = ('title',)
    search_fields = ('title', 'author', 'created_at')
    ordering = ['is_publish', 'created_at', ]
    list_editable = ('is_publish', )
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_filter = ('category',)
    search_fields = ('category',)


