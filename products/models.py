from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .constants import (
    MAX_PRICE, MIN_PRICE, TITLE_MAX_LENGHT
)

class Brand(models.Model):
    """ Модель брендов. """


    title = models.CharField(
        'Название бренда',
        max_length=TITLE_MAX_LENGHT
    )

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Category(models.Model):
    """ Модель категорий товара. """


    title = models.CharField(
        'Название категории',
        max_length=TITLE_MAX_LENGHT
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Product(models.Model):
    """ Модель карточки товаров. """


    title = models.CharField(
        'Название товара',
        max_length=TITLE_MAX_LENGHT,
    )
    description = models.TextField(
        'Описание товара',
        blank=True,
        null=True
    )
    price = models.PositiveIntegerField(
        'Цена',
        validators=(
            MinValueValidator(MIN_PRICE),
            MaxValueValidator(MAX_PRICE)
        )
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория товара',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    brand = models.ForeignKey(
        Brand,
        verbose_name='Бренд',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    is_home = models.BooleanField(
        'Показывать на главной',
        default=False
    )

    class Meta:
        verbose_name='Карточка товара'
        verbose_name_plural='Карточки товаров'
        ordering=('-pub_date',)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    """ Модель для фотографий для товара. """


    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='Товар',
    )
    image = models.ImageField(
        'Фотография',
        upload_to='product_images/',
    )

    def __str__(self):
        return f'Фотография для {self.product.title}'
