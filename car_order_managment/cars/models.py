import uuid

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Color(TimeStampedModel):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    name = models.CharField(
        _('Цвет автомобиля'),
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Цвет')
        verbose_name_plural = _('Цвета')
        db_table = "colors"


class CarBrand(TimeStampedModel):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    name = models.CharField(
        _('Марка автомобиля'),
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Марка')
        verbose_name_plural = _('Марки')
        db_table = "car_brands"


class CarModel(TimeStampedModel):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    name = models.CharField(
        _('Модель автомобиля'),
        max_length=255,
        unique=True
    )
    car_brand = models.ForeignKey(
        'CarBrand',
        related_name='car_models',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Модель')
        verbose_name_plural = _('Модели')
        db_table = "car_models"


class Order(TimeStampedModel):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    color = models.ForeignKey(
        'Color',
        related_name='orders',
        on_delete=models.CASCADE
    )
    car_model = models.ForeignKey(
        'CarModel',
        related_name='orders',
        on_delete=models.CASCADE
    )
    amount = models.IntegerField(
        _("Количество автомобилей"),
        validators=[MinValueValidator(0), ]
    )
    data_order = models.DateTimeField()

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')
        db_table = "orders"
