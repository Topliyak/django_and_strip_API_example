import stripe
from .. import models


def create_order_buying_session(order_id: int) -> dict:
	pass


def create_item_buying_session(item_id: int) -> dict:
	item = models.Item.objects.get(pk=item_id)

	session = stripe.checkout.Session.create(
		success_url="https://example.com/success",
		line_items=[{
			'price_data': {
				'currency': 'usd',
				'product_data': {
					'name': item.name,
				},
				'unit_amount': item.price,
			},
			'quantity': 1,
		}],
		mode="payment",
	)

	return session
