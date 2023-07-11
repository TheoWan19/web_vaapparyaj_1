from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_pass_test


def customer_required(function-None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
	actual_decorator = user_pass_test(
		lambda u: u.is_active and u.is_customer,
		login_url=login_url,
		redirect_field_name=redirect_field_name
		)

		if function:
			return actual_decorator(function)
		return actual_decorator

		
def employee_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):

	actual_decorator = user_pass_test(
		lambda u: u.is_active and u.is_employee,
		login_url=login_url,
		redirect_field_name=redirect_field_name
	)

	if function:
		return actual_decorator(function)
	return actual_decorator	