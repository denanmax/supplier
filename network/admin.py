from django.contrib import admin
from django.utils.html import format_html

from network.models import Delivery, Manufacturer, Supplier, Product


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('debt', 'created_at', 'create_supplier_url', 'supplier', 'recipient')
    actions = ['nullify_debt']

    def nullify_debt(self, request, queryset):
        for item in queryset:
            item.debt = 0
            item.save()
        self.message_user(request, f'Задолженность обнулена')

    nullify_debt.short_description = 'Обнулить задолженность'

    def create_supplier_url(self, obj):
        """ Получение ссылки на поставщика """

        supplier = obj.supplier
        try:
            supplier_id = supplier.id
            url = f'{supplier_id}/change/'
            return format_html("<a href='{url}'>{name}</a>", url=url, name=obj.supplier)
        except AttributeError:
            pass

    create_supplier_url.short_description = 'Ссылка'


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city')
    list_filter = ('city',)
    list_per_page = 10


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city')
    list_filter = ('city',)
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'manufacturer', 'model')
    list_filter = ('released',)
    list_per_page = 10
