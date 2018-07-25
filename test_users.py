from app import app 
import unittest 
import json
import os

class UsersTestCase(unittest.TestCase):



  def test_signup_user(self):
    tester = app.test_client(self)
    response = tester.post('/api/v2/entry', content_type="application/json")
    data=dict(full_name="wagole", username="refuge", email="homiemusa@gmail.com", password="wise12")
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Successfully Registered', response.data)


if __name__ == '__main__':
  unittest.main()