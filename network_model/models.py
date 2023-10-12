from django.core.exceptions import ValidationError
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Модель товаров (оборудования)"""

    name = models.CharField(max_length=150, verbose_name='Наименование товара')
    model = models.CharField(max_length=150, verbose_name='Модель товара')
    release_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Hierarchy(models.IntegerChoices):
    """Модель иерархии звена"""

    FACTORY = 0, 'Завод'
    RETAIL = 1, 'Розничная сеть'
    IP = 2, 'Индивидуальный предприниматель'


class Structure(models.Model):
    """Модель структуры сети"""

    name = models.CharField(max_length=150, verbose_name='Наименование')
    # контактная информация
    email = models.EmailField(max_length=150, verbose_name='Электронная почта')
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house_number = models.CharField(max_length=150, verbose_name='Номер дома')
    # список товаров
    product = models.ManyToManyField(Product, verbose_name='Товары')
    # иерархия
    hierarchy = models.IntegerField(choices=Hierarchy.choices, default=Hierarchy.FACTORY,  verbose_name='Уровень звена')
    supplier = models.ForeignKey('Structure', on_delete=models.PROTECT, **NULLABLE, verbose_name='Поставщик')
    debt = models.DecimalField(decimal_places=2, max_digits=15, **NULLABLE, verbose_name='Задолженность')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def clean(self):
        if self.supplier:
            supplier_hierarchy = Structure.objects.values('hierarchy').get(id=self.supplier_id)['hierarchy']
            if self.hierarchy - supplier_hierarchy not in [0, 1]:
                raise ValidationError(f'Недопустимый уровень иерархии звена')
        elif self.debt:
            raise ValidationError(f'Нет поставщика для отображения задолженности')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уровень сети'
        verbose_name_plural = 'Уровни сети'
