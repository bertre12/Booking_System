from django.db import models


# Создание модели(таблицы).
class Hotel(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name='Название')
    price = models.IntegerField(blank=True, null=True, verbose_name='Цена')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Игнорирование создание существующей таблицы.
        db_table = 'hotel'  # Имя таблицы, которая уже есть в в бд.

        verbose_name = 'Гостиница'
        verbose_name_plural = 'Гостиницы'
