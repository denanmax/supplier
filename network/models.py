from django.db import models
from django.utils import timezone


class Manufacturer(models.Model):
    """ Производитель / Завод """

    title = models.CharField(max_length=200, verbose_name='Производитель', unique=True)
    email = models.EmailField(verbose_name='Имэйл')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=20, verbose_name='Улица')
    building = models.CharField(max_length=100, verbose_name='Номер дома')

    def __str__(self):
        return f'Manufacturer - {self.title} from {self.country} -{self.city}'

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Supplier(models.Model):
    """Поставщик"""

    supplier_choice = [
        ('self-employed', 'ИП'),
        ('retailer', 'розничная сеть')
    ]

    title = models.CharField(max_length=200, verbose_name='Поставщик', unique=True)
    email = models.EmailField(verbose_name='Имэйл')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=20, verbose_name='Улица')
    building = models.CharField(max_length=100, verbose_name='Номер дома')
    supplier = models.CharField(choices=supplier_choice, verbose_name='Статус поставщика')

    def __str__(self):
        return f'{self.title} from {self.country} -{self.city}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    """Продукт"""

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Производитель')
    title = models.CharField(max_length=200, verbose_name='Название')
    model = models.CharField(max_length=50, verbose_name='Модель')
    released = models.DateTimeField(default=timezone.now, verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.title} - {self.model}, Manufacturer - {self.manufacturer}, released - {self.released}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Delivery(models.Model):
    """Поставка"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Производитель')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик', null=True, blank=True,
                                 related_name='delivery_supplier')
    recipient = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Получатель', null=True, blank=True,
                                  related_name='delivery_recipient')
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (
            f'Delivery {self.product} Manufacturer -  {self.manufacturer} Supplier - {self.supplier}, '
            f'Recipient - {self.recipient}, created - {self.created_at}')

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'
