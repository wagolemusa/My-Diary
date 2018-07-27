from flask import Flask, jsonify, request, make_response, Blueprint
import re

def set_password(self, password):
  if not password:
      raise AssertionError('Password not provided')

  if not re.match('\d.*[A-Z]|[A-Z].*\d', password):
      raise AssertionError('Password must contain 1 capital letter and 1 number')

  if len(password) < 8 or len(password) > 50:
      raise AssertionError('Password must be between 8 and 50 characters')

  self.password_hash = generate_password_hash(password)