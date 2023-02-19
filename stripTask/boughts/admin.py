from django.contrib import admin
from . import models


class ItemInOrderInline(admin.TabularInline):
	model = models.ItemInOrder


class OrderAdmin(admin.ModelAdmin):
	inlines = [ItemInOrderInline]


admin.site.register(models.Item)
admin.site.register(models.Order, OrderAdmin)
