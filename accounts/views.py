from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User
from .forms import CustomerSignUpForm, EmployeeSignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse 
from .decorators import customer_required, employee_required

# Create your views here.
class CustomerSignUpView(CreateView):
	model = User
	form_class = CustomerSignUpForm
	template_name = 'accounts/customer_signup.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'customer'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		if form.is_valid():
			messages.success(self.request, 'Account was created for ' + user.username)
			login(self.request, user)
			return redirect('login')
		else:
			print('Form is not valid')
			messages.error(self.request, 'Error Processing Your Request')
			context = {'form': form}
			return render(self.request, 'accounts/customer_signup', context)
		return redirect('login')	

class EmployeeSignUpView(CreateView):
	model = User
	form_class = EmployeeSignUpForm
	template_name = 'accounts/employee_signup.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'employee'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		if form.is_valid():
			messages.success(self.request, 'Account was created for ' + user.username)
			login(self.request, user)
			return redirect('login')
		else:
			print('Form is not valid')
			messages.error(self.request, 'Error Processing Your Request')
			context = {'form': form}
			return render(self.request, 'accounts/employee_signup', context)
		return redirect('login')

class LoginView(auth_views.LoginView):
	form_class = LoginForm
	template_name = 'accounts/login.html'

	def get_context_data(self, **kwargs):
		return super().get_context_data(**kwargs)

	def get_success_url(self):
		user = self.request.user
		if user.is_authenticated:
			if user.is_customer:
				messages.success(self.request, 'You Have Been Logged Successfull')
				return reverse('customer-home')	
			elif user.is_employee:
				messages.success(self.request, 'You Have Been Logged Successfull')
				return reverse('employee-home')
		else:
			messages.error(self.request, 'You Are Not Logged Successfull')
			return reverse('login')			

@login_required
@customer_required
def customer_home(request):
	return render(request, 'accounts/customer_home.html', {})

@login_required
@employee_required
def employee_home(request):
	return render(request, 'accounts/employee_home.html', {})	
    
