from django.db import models

# Create your models here.
class PizzaModel(models.Model):
	name = models.CharField(max_length = 10)
	price = models.IntegerField()



class CustomerModel(models.Model):
	username= models.CharField(max_length = 20)
	userid = models.CharField(max_length= 10)
	
	password= models.CharField(max_length= 10)

	def __str__(self):
		return f"{self.username}  {self.password}"

class OrderModel(models.Model):
	username = models.CharField(max_length = 20)
	
	address = models.CharField(max_length = 100)
	ordereditems = 	models.CharField(max_length = 100)
	status = models.CharField(max_length= 10)