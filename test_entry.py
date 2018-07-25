from app import app 
import unittest 
import json
import os


class UserTestCase(unittest.TestCase):


  def test_home_endpoint(self):
    tester = app.test_client(self)
    response = tester.get('/', content_type="application/json")
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Welcome To Home Page', response.data)


if __name__ == '__main__':
  unittest.main()