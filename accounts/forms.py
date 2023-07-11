from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import User, Customer, Employee
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model

class DateInput(forms.DateInput):
	input_type = 'date'

class CustomerSignUpForm(UserCreationForm):

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
	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_customer = True
		if commit:
			user.save()
		customer = Customer.objects.create(user=user, mobile=self.cleaned_data.get('mobile'), first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'), gender=self.cleaned_data.get('gender'), role=self.cleaned_data.get('role'), location=self.cleaned_data.get('location'))	
		return user	

class EmployeeSignUpForm(UserCreationForm):

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

	nif = forms.CharField(max_length=10, 
							 required=True, 
							 help_text='Enter Nif'
							 widget=forms.TextInput(attrs-{'class': 'form-control', 'placeholder': 'NIF'}),)

	ciu = forms.CharField(max_length=10, 
							 required=True, 
							 help_text='Enter Ciu'
							 widget=forms.TextInput(attrs-{'class': 'form-control', 'placeholder': 'CIU'}),)

	gender = forms.ChoiceField(choices=GENDER)

	role = forms.ChoiceField(choices=ROLE)

	birth_date = forms.DateField(widget=DateInput)

	designation = forms.CharField(max_length=100, 
							 required=True, 
							 help_text='Enter Designation'
							 widget=forms.TextInput(attrs-{'class': 'form-control', 'placeholder': 'Designation'}),)

	workplace = forms.CharField(max_length=100, 
							 required=True, 
							 help_text='Enter Workplace'
							 widget=forms.TextInput(attrs-{'class': 'form-control', 'placeholder': 'Workplace'}),)

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
	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_employee = True
		if commit:
			user.save()
		employee = Employee.objects.create(user=user, mobile=self.cleaned_data.get('mobile'), first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'), nif=self.cleaned_data.get('nif'), ciu=self.cleaned_data.get('ciu'), gender=self.cleaned_data.get('gender'), role=self.cleaned_data.get('role'), birth_date=self.cleaned_data.get('birth_date'), designation=self.cleaned_data.get('designation'), workplace=self.cleaned_data.get('workplace'))	
		return user			

class LoginForm(AuthenticationForm):
	username = forms.CharField(help_text='Enter Username', 
							   required=True,
							   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usermane'}))

	password = forms.CharField(help_text='Enter Password', 
							   required=True,
							   widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
