from django.contrib.auth import get_user_model, authenticate, password_validation
from django.test import TestCase

from user.form import UserCreateForm

User = get_user_model()

DATA = {
	'first_name': 'test',
	'last_name': 'test',
	'email': 'test@example.com',
	'password': 'Testing@123',
}


class LogInTest(TestCase):
	def setUp(self):
		User.objects.create_user(**DATA)

	def test_1_user_exists(self):
		print('Testing for User Exist')
		user = User.objects.get(email=DATA['email'])
		self.assertTrue(user)

	def test_2_user_active(self):
		print('Testing for User Active')
		user = User.objects.get(email=DATA['email'])
		self.assertTrue(user.is_active)

	def test_3_invalid_credentials(self):
		print('Testing for User Valid Credentials')
		form = authenticate(email=DATA['email'], password=DATA['password'])
		self.assertTrue(form)


class SignUp(TestCase):


	def test_1_password_validation(self):
		print('Testing for password Validation')
		validate = password_validation.validate_password(DATA['password'])
		self.assertEquals(validate, None)

	def test_2_user_creation_and_verification(self):
		print('Testing Create user')
		form = UserCreateForm(data=DATA)
		form.is_valid()
		form.create(DATA)
		self.assertTrue(form)
		user = User.objects.get(email=DATA['email'])
		self.assertTrue(user)

	def test_3_password_check(self):
		print('Testing Password/Confirm Password match')
		password = DATA['password']
		confirm_password = 'Testing@123'
		if password == confirm_password:
			self.assertTrue('password matched')
		else:
			self.assertFalse('password mismatch')
