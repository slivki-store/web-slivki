from django.db import models

from products.constants import TITLE_MAX_LENGHT


class HomeBanner(models.Model):
    title = models.CharField(
        'Текст',
        max_length=TITLE_MAX_LENGHT,
        blank=True,
    )
    link = models.URLField(
        'Ссылка',
        blank=True,
    )
    photo = models.ImageField(
        'Фотография',
        upload_to='home_images/',
    )
    is_home = models.BooleanField(
        'Показывать на главной?',
        default=True,
    )
    number = models.PositiveSmallIntegerField(
        'Порядковый номер'
    )

    class Meta:
        verbose_name = 'Баннер главной'
        verbose_name_plural = 'Баннеры главной'
        ordering = ['number']
