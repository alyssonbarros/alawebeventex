from django.test import TestCase
from alawebeventex.subscriptions.forms import SubscriptionForm


class SubscriptionTestForm(TestCase):
	def setUp(self):
		self.form = SubscriptionForm()

	def test_form_has_fields(self):
		"""Form must have 4 fields"""
		expected = ['name', 'cpf', 'email', 'phone']
		self.assertSequenceEqual(expected, list(self.form.fields))
