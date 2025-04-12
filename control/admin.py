from django.contrib import admin

from .models import Hotel, Users


# Подключение модели для отображения и управления в админпанели.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Поля отображения в админке.
    search_fields = ('name',)  # Поле поиска.
    ordering = ('name',)  # Сортировка.


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'phone_number', 'email', 'hotel', 'booking_number'
    )  # Поля для отображения в админке.
    search_fields = ('name', 'phone_number', 'email')  # Поля для поиска.
    ordering = ('name',)  # Сортировка.


# Регистрация моделей в админпанели.
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Users, UserAdmin)
