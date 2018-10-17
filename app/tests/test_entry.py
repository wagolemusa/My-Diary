import unittest 
from flask import app
import json
import os
import sys
import psycopg2
# from __init__ import *
sys.path.insert(0, os.path.abspath(".."))
from run import api_bp

def tear():
  dbcon = psycopg2.connect(dbname='refuges', user='postgres', password='refuge', host='localhost')
  dbcur.execute("delete from users where username = 'pussycat',")
  dbcur.execute("delete from entries where title = 'lakehub' and 'entries' = 'Am member',")
  dbcon.commit()

# data = {
#   "full_name": "nigahman",\
#   "username": "pussycat",\
#   "email": "pussycat@gmail.com",\
#   "password": "pussycat123"\
# }


data = {"fname": "kibish",\
        "username":"test", \
        "password":"Kev12345",\
        "lname":"kipkoech",\
        "cpassword":"Kev12345",\
        "email":"tests@gmail.com"\
        }

class TestCreateEntry(unittest.TestCase):
    def setUp(self):
        #creates table and test user
        # DatabaseModel.create_table()
        self.app = app.test_client()
        self.app.post('/api/v2/users/register', json=data)       
 
    def test_post(self):
        #test return status code for no provided token
        res = self.app.post('/api/v2/users/login', json={"username":"test", "password":"Kev12345"})
        token = res.get_json()["token"]
        response = self.app.post('/api/v2/entries', headers = {"x-access-token":token},\
        json={"title":"test", "entry":"successful"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "entry was successfully saved")

    def test_get(self):
        #test message when no token provided
        res = self.app.post('/api/v2/users/login', json={"username":"test", "password":"Kev12345"})
        token = res.get_json()["token"]
        response = self.app.get('/api/v2/entries')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "you are out of session")
        response2 = self.app.get('/api/v2/entries', headers = {"x-access-token":token})
        self.assertEqual(response2.status_code, 200)

    def tearDown(self):
        tear()

class TestEntryId(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.post('/api/v2/users/register', json=data)   

    def test_put(self):
        #test wrong method modification
        res = self.app.post('/api/v2/users/login', json={"username":"test", "password":"Kev12345"})
        token = res.get_json()["token"]        
        modify = self.app.post\
        ('/api/v2/entries/3', json={"title":"test","entry":"successful" }).status_code
        self.assertEqual(modify, 405)
        response = self.app.post\
        ('/api/v2/entries/3', json={"title":""}, headers = {"x-access-token":token}).status_code
        self.assertEqual(modify, 405)

    def test_delete(self):
        #test wrong entry route and method
        res = self.app.get('/api/v2/entries/delete_entry').status_code
        self.assertEqual(res, 404)
        response = self.app.delete('/api/v2/entries/3')
        self.assertEqual(response.get_json()["message"], "you are out of session")

    def test_get(self):
        #test succesful response
        res = self.app.post('/api/v2/users/login', json={"username":"test", "password":"Kev12345"})
        token = res.get_json()["token"]
        self.assertEqual(self.app.get('/api/v2/entries/8').get_json()["message"], "you are out of session")
        response = self.app.get('/api/v2/entries/8p', headers = {"x-access-token":token})
        self.assertEqual(response.status_code, 404)
            
    def tearDown(self):
        tear()

if __name__ == '__main__':
  unittest.main()




# class TestCreateEntry(unittest.TestCase):



#     def setUp(self):
#         #creates table and test user
#         self.app =  app.test_client()
#         self.app.post('/api/v2/users/register', json=data)       
 
#     def test_post(self):
#         #test return status code for no provided token
#         res = self.app.post('/api/v2/users/login', json={"username":"pussycat", "password":"pussycat123"})
#         token = res.get_json()["token"]
#         response = self.app.post('/api/v2/entries', headers = {"x-access-token":token},\
#         json={"title":"test", "entry":"successful"})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.get_json()["message"], "entry was successfully saved")

#     def test_get(self):
#         #test message when no token provided
#         res = self.app.post('/api/v2/users/login', json={"username":"pussycat", "password":"pussycat123"})
#         token = res.get_json()["token"]
#         response = self.app.get('/api/v2/entries')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.get_json()["message"], "you are out of session")
#         response2 = self.app.get('/api/v2/entries', headers = {"x-access-token":token})
#         self.assertEqual(response2.status_code, 200)

#     def tearDown(self):
#         tear()

# class EntriesTestCase(unittest.TestCase):
#   def setUp(self):
#     #creates table and test user
#     self.app = app.test_client()
#     self.app.post('/api/v2/users/register', json=data)      

#     #Test home end point
#   def test_home_endpoint(self):
#     # tester = app.test_client(self)
#     response = tester.get('/', content_type="application/json")
#     self.assertEqual(response.status_code, 200)
#     self.assertIn(b'Welcome To Home Page', response.data)

#   #   """Test Post entry"""
#   # def test_post_entries(self):
#   #   tester = app.test_client(self)
#   #   response = tester.post('/api/v2/entries', content_type="application/json")
#   #   data=dict(title="python", dates="04/08/2018", entries="I will have to code")
#   #   self.assertIn(b'Successfuly Posted Entries', response.data)

#   #   """Test show all entries"""
#   # def test_show_all_entries(self):
#   #   tester = app.test_client(self)
#   #   response = tester.get('/api/v2/entries',content_type="application/json")
#   #   self.assertEqual(response.status_code, 200)

#   # def test_show_an_entry(self):
#   #   tester = app.test_client(self)
#   #   response = tester.get('/api/v2/entries/2',content_type="application/json")
#   #   self.assertEqual(response.status_code, 200)

#   # def test_update_entries(self):
#   #   tester = app.test_client(self)
#   #   response = tester.put('/api/v2/entries/2', content_type="application/json")
#   #   data=dict(title="python", dates="04/08/2018", entries="I will have to code")
#   #   self.assertIn(b'Entries Successfuly Updated', response.data)

#   def tearDown(self):
#     tear()

# if __name__ == '__main__':
#   unittest.main()