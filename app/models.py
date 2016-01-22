from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	category = models.CharField(default="books", max_length=40)
	description = models.CharField(max_length=1000)
	featured = models.BooleanField(default=False)
	multimedia = models.ImageField(upload_to="img", blank=True, verbose_name='Product Image')
	name = models.CharField(max_length=100)
	popularity = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	pub_date = models.DateTimeField(auto_now_add=True, verbose_name='date published')

	def __str__(self):
		return self.name
		return html

class Order(models.Model):

	PAYMENT_CHOICES = (	('paypal', 'paypal'),
						('credit card', 'credit card'),
						('bank transfer', 'bank transfer'),)


	city = models.CharField(max_length=250)
	first_name = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	order_date = models.DateTimeField(auto_now_add=True, verbose_name='date')
	payment = models.CharField(choices=PAYMENT_CHOICES, max_length=200)
	postal_code = models.IntegerField()
	street = models.CharField(max_length=250)
	total_amount = models.DecimalField(max_digits=10, decimal_places=2)
	user = models.ForeignKey(User)

	# Total amount should change every time we save
	# because orders can be modified via admin site


	def __str__(self):
		return 'Order No. %i' % self.id

	def address(self):
		return self.street + ", " + str(self.postal_code) + ", " + self.city


class BookOrder(models.Model):
	order = models.ForeignKey(Order)
	product = models.ForeignKey(Book)
	quantity = models.IntegerField()
