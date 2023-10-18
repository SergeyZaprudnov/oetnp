from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from network_model.models import Product, Structure


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'debt')
    list_filter = ['city']
    actions = ['null_debt']

    def null_debt(self, request, queryset):
        """Функция очистки задолженности"""
        for network_object in queryset:
            network_object.debt = 0
            network_object.save()
        self.message_user(request, f'Задолженность перед поставщиком у выбранных объектов очищена.')

    def link(self, obj):
        url = reverse('admin:network_model_structure_change', args=[obj.supplier_id])
        return format_html('<a href="{}">{}</a>', url, obj.supplier)

    link.short_description = 'Поставщик'
    null_debt.short_description = 'Очистить задолженность перед поставщиком'
