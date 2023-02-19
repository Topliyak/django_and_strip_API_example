from django.http import JsonResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import DetailView
from django.conf import settings
from .services.payment import create_item_buying_session
from .services.order_former import get_items_in_order
from . import models


class ItemDetail(DetailView):
	model = models.Item
	pk_url_kwarg = 'item_pk'
	template_name = 'boughts/item_detail.html'
	extra_context = {'stripe_pk': settings.STRIPE_PK}


def get_order(request: HttpRequest, order_pk: int):
	context = {
		'items': get_items_in_order(order_pk),
		'stripe_pk': settings.STRIPE_PK,
	}

	return render(request, 'order.html', context)


def get_session_id(request: HttpRequest, item_pk: int):
	stripe_session_id = create_item_buying_session(item_pk)
	return JsonResponse(stripe_session_id)
