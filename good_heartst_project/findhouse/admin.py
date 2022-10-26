from django.contrib import admin
from .models import FindHome


@admin.register(FindHome)
class FindHomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'creat_at', 'is_publish',
                    'actualish', 'type_animal', 'help_an')
    search_fields = ('creat_at', 'type_animal')
    list_filter = ('actualish',)
    list_editable = ('actualish', 'type_animal')
    ordering = ['actualish', ]
