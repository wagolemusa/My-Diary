from app import app
import unittest
import os
import json

class UserTestCase(unittest.TestCase):

	"""Get all users """
	def test_get_all_users(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/get_all_users')
		self.assertEqual(response.status_code, 200)

	"""Test register User"""
	def test_register_user(self):
		tester = app.test_client(self)
		response = tester.post(
			'api/v1/auth/regester', data=json.dumps(
				dict(full_name="refuge", username="wise", email="musa@gmail.com", password="wise12", confirm_password="wise12")),
			content_type="application/json")
		self.assertEqual(response.status_code, 200)
			

if __name__ =='__main__':
	unittest.main()