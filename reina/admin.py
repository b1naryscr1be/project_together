from django.contrib import admin

from .models import Situation


@admin.register(Situation)
class AdminSituation(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
