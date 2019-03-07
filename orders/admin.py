from django.contrib import admin
from .models import Order, OrderItem
from django.http import HttpResponse
from django.shortcuts import reverse
from django.utils.html import format_html
import csv
import datetime



def ExportToCSV(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
            filename=Orders-{}.csv'.format(datetime.datetime.now().strftime('%d/%m/%Y'))
    writer = csv.writer(response)

    fields = [field for field in opts.get_field() if not field.many_to_many and field.one_to_many]
    # Первая строка - оглавление
    writer.writerow([field.verbose_name for field in fields])
    # Заполняем информацией
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
ExportToCSV.short_description = 'Export CSV'


def OrderDetail(obj):
    return format_html('<a href="{}">Посмотреть</a>'.format(
        reverse('admin_order_detail_url', args=[obj.id])
    ))
OrderDetail.short_description = 'ИНФО'

def OrderPDF(obj):
    return format_html('<a href="{}">PDF</a>'.format(
        reverse('admin_order_pdf_url', args=[obj.id])
    ))
OrderPDF.short_description = 'В PDF'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated', OrderDetail, OrderPDF]
    readonly_fields = ['id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated', OrderDetail, OrderPDF]
    list_filter = ['paid', 'created', 'updated']
    # inlines = [OrderItemInline]
    actions = [ExportToCSV]


admin.site.register(Order, OrderAdmin)
