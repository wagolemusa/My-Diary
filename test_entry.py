from app import app 
import unittest 
import json
import os


class UserTestCase(unittest.TestCase):

    #Test home end point
  def test_home_endpoint(self):
    tester = app.test_client(self)
    response = tester.get('/', content_type="application/json")
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Welcome To Home Page', response.data)

    """Test Post entry"""
  def test_post_entries(self):
    tester = app.test_client(self)
    response = tester.post('/api/v2/entry', content_type="application/json")
    data=dict(title="python", dates="04/08/2018", entries="I will have to code")
    self.assertIn(b'Successfuly Posted Entries', response.data)

    """Test show all entries"""
  def test_show_all_entries(self):
    tester = app.test_client(self)
    response = tester.get('/api/v2/get_entries',content_type="application/json")
    self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
  unittest.main()