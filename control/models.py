from django.db import models


# Создание модели(таблицы).
class Hotel(models.Model):
    name = models.CharField(max_length=100, blank=True,
                            null=True, verbose_name='Название')
    price = models.FloatField(blank=True, null=True, verbose_name='Цена')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')

    # Управление поведением модели и взаимодействием с бв.
    class Meta:
        managed = False  # Игнорирование создание существующей таблицы.
        db_table = 'hotel'  # Имя таблицы, которая уже есть в в бд.

        verbose_name = 'Гостиница'
        verbose_name_plural = 'Гостиницы'

    # Отображение в виде строки.
    def __str__(self):
        return self.name


class Users(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False,
                            verbose_name='Имя пользователя')
    phone_number = models.CharField(max_length=20, blank=False,
                                    null=False, verbose_name='№ телефона')
    email = models.EmailField(max_length=100, blank=True,
                              null=True, verbose_name='Электронная почта')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,
                              verbose_name='Гостиница')  # Связь с Hotel.
    booking_number = models.TextField(blank=False, null=False,
                                      verbose_name='Номер бронирования')

    class Meta:
        managed = False
        db_table = 'users'

        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name
