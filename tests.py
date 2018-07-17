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

	""" Test one Entry"""
	def test_one_entry(self):
		tester = app.test_client(self)
		response = tester.get('api/V1/view_entry/1')
		self.assertEqual(response.status_code, 200)

		

		""" Test post Entry"""
	#def post_entery(self, title, date, entry):
	#	return self.app.post(
	#		'/api/v1/post_entry',
	#		dics=entry(title=title, date=date, entry=entry)
	#	)
	#def test_post__entry(self):
	#	response = self.post_entry('hiphop', '23/08/2018', 'I love HipHop')
	#		self.assertEqual(response.status_code, 200)
	#def test_post_entry(self):
	#	tester = app.test_client(self)
	#	response = tester.post('/api/v1/post_entry')
	#	self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
	unittest.main()