from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):

	email = models.EmailField(max_length=255, unique=True)
	mobile = models.CharField('Phone Number', max_length=12, unique=True)
	is_customer = models.BooleanField(default=False)
	is_employee = models.BooleanField(default=False)

class Customer(models.Model):

	GENDER = (
				('M', 'M'),
				('F', 'F'),
			)

	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer')
	mobile = models.CharField('Phone Number', max_length=12, unique=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	gender = models.CharField(max_length=1, choices=GENDER)
	location = models.CharField(max_length=255)

	def __str__(self):
		return f"{self.last_name}-{self.user.mobile}".upper()

class Employee(models.Model):

	GENDER = (
				('M', 'M'),
				('F', 'F'),
			)
	
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='employee')
	mobile = models.CharField('Phone Number', max_length=12, unique=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	gender = models.CharField(max_length=1, choices=GENDER)
	nif = models.CharField('NIF', max_length=10, unique=True, null=False)
	ciu = models.CharField('CIU', max_length=10, unique=True, null=False)
	birth_date = models.DateField('Date Of Birth')
	designation = models.CharField(max_length=100)
	worlkplace = models.CharField(max_length=255)

	def __str__(self):
		return f"{self.last_name}-{self.nif}".upper()
	