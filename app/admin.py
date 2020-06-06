from django.contrib import admin
from app.models import Todo
# Register your models here.
@admin.register(Todo)
class todoAdmin(admin.ModelAdmin):
    list_display = ['name', 'done', 'created_at']