from django.contrib import admin
from django.contrib import admin
from .models import Oluvchi

@admin.register(Oluvchi)
class OluvchiAdmin(admin.ModelAdmin):
    list_display = ('yosh',)

