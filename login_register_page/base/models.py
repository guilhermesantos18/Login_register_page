from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

class Usuario(User):
    username = User.username
    first_name = User.first_name
    last_name = User.last_name
    email = User.email
    password = User.password
    