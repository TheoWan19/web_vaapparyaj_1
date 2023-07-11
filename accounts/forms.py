from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import User, Customer, Employee
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model

class DateInput(forms.DateInput):
	input_type = 'date'

class Customer(UserCreationForm):

	GENDER = (
				('M', 'M'),
				('F', 'F'),
			)

	ROLE = (
				('CUSTOMER', 'CUSTOMER'),
				('EMPLOYEE', 'EMPLOYEE'),
			)

	email = forms.EmailField(max_length=255, 
							 required=True, 
							 help_text='Enter Email Address', 
							 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),)

	mobile = forms.CharField(max_length=12, 
							 required=True, 
							 help_text='Enter Phone Number'
							 widget=forms.TextInput(attrs-{'class': 'form-control', 'placeholder': 'Phone Number (+0 0000-0000-000)'}),)

	first_name = forms.CharField(max_length=100, 
							 required=True, 
							 help_text='Enter First Name'
							 widget=forms.TextInput(attrs-{'class': 'form-control', 'placeholder': 'First Name'}),)

	last_name = forms.CharField(max_length=100, 
							 required=True, 
							 help_text='Enter Last Name'
							 widget=forms.TextInput(attrs-{'class': 'form-control', 'placeholder': 'Last Name'}),)

	gender = forms.ChoiceField(choices=GENDER)

	role = forms.ChoiceField(choices=ROLE)

	location = forms.CharField(max_length=100, 
							 required=True, 
							 help_text='Enter Location'
							 widget=forms.TextInput(attrs-{'class': 'form-control', 'placeholder': 'Location'}),)

	password1 = forms.CharField(help_text='Enter Password', 
								required=True, 
								widget=forms.PasswordInput(attrs{'class': 'form-control', 'placeholder': 'Password'}),)

	password2 = forms.CharField(help_text='Enter Password Again', 
								required=True, 
								widget=forms.PasswordInput(attrs{'class': 'form-control', 'placeholder': 'Confirm Password'}),)

	check = forms.BooleanField(required=True)

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	@transaction.atomic	


