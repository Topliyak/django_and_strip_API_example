from django.db import models


class Item(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	price = models.IntegerField()

	def __str__(self):
		return self.name


class Order(models.Model):
	total_price = models.IntegerField(default=0)


class ItemInOrder(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)

	def __str__(self):
		return self.item.name
