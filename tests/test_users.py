from app import app 
import unittest 
import json
import os

class UsersTestCase(unittest.TestCase):



  def test_signup_user(self):
    tester = app.test_client(self)
    response = tester.post('/api/v2/auth/signup', content_type="application/json")
    data=dict(full_name="wagole", username="refuge", email="homiemusa@gmail.com", password="wise12")
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Successfully Registered', response.data)

    """login user"""
  def test_login_user(self):
    tester = app.test_client(self)
    response = tester.post(
      'api/v2/auth/signup', data=json.dumps(
        dict(full_name="wagole", username="refuge", email="homiemusa@gmail.com", password="wise12")),
      content_type="application/json")
    response = tester.post('/api/v2/auth/login', data=json.dumps(
      dict(username="refuge", password="wise12")),
      content_type="application/json")
    self.assertEqual(response.status_code, 200)
      



if __name__ == '__main__':
  unittest.main()