from django.contrib import admin
from .models import Item, OrderItem, Order, Payment

# Register your models here.


def make_being_delivered(modeladmin, request, queryset):
    queryset.update(being_delivered=True)


make_being_delivered.short_description = 'Deliver selected items'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'being_delivered']
    list_filter = ['ordered', 'being_delivered']
    actions = [make_being_delivered]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
