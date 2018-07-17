from app import app 
import unittest
import os
import json

class EntriesTestCase(unittest.TestCase):



	"""Test all entries"""
	def test_all_entries(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/get_entries')
		self.assertEqual(response.status_code, 200)
		#response = self.client().get('/api/v1/get_entries')
		#self.assertEqual(response.status, 200)



if __name__ == '__main__':
	unittest.main()