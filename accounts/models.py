from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):

	GENDER = (
				('M', 'M'),
				('F', 'F'),
			)

	ROLE = (
				('CUSTOMER', 'CUSTOMER'),
				('EMPLOYEE', 'EMPLOYEE'),
			)

	email = models.EmailField(max_length=255, unique=True)
	mobile = models.CharField('Phone Number', max_length=12, unique=True)
	gender = models.CharField(max_length=1, choices=GENDER)
	role = models.CharField(max_length=8, choices=ROLE, unique=True)
	is_customer = models.BooleanField(default=False)
	is_employee = models.BooleanField(default=False)

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer')
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	location = models.CharField(max_length=255)

	def __str__(self):
		return f"{self.last_name}-{self.user.mobile}".upper()

class Employee(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='employee')
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	nif = models.CharField('NIF', max_length=10, unique=True, null=False)
	ciu = models.CharField('CIU', max_length=10, unique=True, null=False)
	birth_date = models.DateField('Date Of Birth')
	designation = models.CharField(max_length=100)
	worlkplace = models.CharField(max_length=255)

	def __str__(self):
		return f"{self.last_name}-{self.nif}".upper()
	