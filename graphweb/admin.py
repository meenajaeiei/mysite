from django.contrib import admin
from .models import Data,History


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'datetime')


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'filename')
