from django.contrib import admin

from .models import Hotel


# Подключение модели для отображения и управления в админпанели.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Поля отображения в админке.
    ordering = ('name',)  # Сортировка.


admin.site.register(Hotel, HotelAdmin)
