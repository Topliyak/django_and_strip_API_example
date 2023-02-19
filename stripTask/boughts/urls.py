from django.urls import path
from . import views

urlpatterns = [
	path('buy/<int:item_pk>', views.get_session_id, name='get_session_id'),
	path('item/<int:item_pk>', views.ItemDetail.as_view()),
	path('order/<int:order_pk>', views.get_order),
]
