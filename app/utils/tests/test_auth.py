from datetime import timedelta
from uuid import uuid4

import jwt
from ..auth import create_access_token, authenticate_user, valid_token

class MockUser:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

def test_create_acess_token():
    TIME_DIFF = 10

    data = {
        "some_data": "test",
        "other_data": "test"
    }

    delta = timedelta(minutes=TIME_DIFF)

    resp = create_access_token(data=data, expires_delta=delta)
    token_data = jwt.decode(resp, key="development-key", algorithms="HS256")

    assert token_data["some_data"] == data["some_data"]
    assert token_data["other_data"] == data["other_data"]


def test_authenticate_user_correct_credentials():
    username = "test"
    password = "test"
    
    user = MockUser(username, password)
    resp = authenticate_user(user, username, password)
    
    assert resp == user

def test_authenticate_user_incorrect_credentials():
    username = "test"
    password = "test"

    user = MockUser(f"wrong_{username}", f"wrong_{password}")
    resp = authenticate_user(user, username, password)
    
    assert resp == False

def test_valid_token_valid():
    delta = timedelta(minutes=10)
    data = {
        "sub": "test",
    }

    token = create_access_token(data=data, expires_delta=delta)
    
    resp = valid_token(token)

    assert resp == True

def test_valid_token_invalid():
    delta = timedelta(minutes=10)
    data = {
        "invalid_key": "test",
    }

    token = create_access_token(data=data, expires_delta=delta)
    
    resp = valid_token(token)

    assert resp == False

def test_valid_token_broken():
    token = str(uuid4())
    
    resp = valid_token(token)

    assert resp == False




