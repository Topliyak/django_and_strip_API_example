from ..models import ItemInOrder, Item
from django.db.models.query import QuerySet


def get_items_in_order(order_pk: int) -> QuerySet[Item]:
	items = ItemInOrder.objects.filter(order=order_pk).values_list('item', flat=True)
	return items
