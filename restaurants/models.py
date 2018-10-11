from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Restaurant(models.Model):
	owner= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	name = models.CharField(max_length=120)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	logo = models.ImageField(upload_to='restaurant_logos', null=True, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('restaurant-detail', kwargs={'restaurant_id':self.id})

class Item(models.Model):
	name=models.CharField(max_length=100)
	description=models.TextField()
	price=models.DecimalField(max_digits=10, decimal_places=3)
	restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=1)
