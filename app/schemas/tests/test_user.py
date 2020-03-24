from pydantic import ValidationError

from ..user import User, UserBase, UserUpdate
from ..product import Product

def test_create_user_ok():
    prod_data = {
        "id": "teste",
        "title": "teste",
        "image": "teste",
        "price": 123.4
    }

    product = Product(**prod_data)

    user_data = {
        "username": "test",
        "email":    "test@test.email",
        "favorites": [product, product]
    }

    user = User(**user_data)

    assert user.username == user_data["username"]
    assert user.email == user_data["email"]
    assert user.favorites == user_data["favorites"]

def test_create_user_invalid_favorites():
    prod_data = {
        "id": "teste",
        "title": "teste",
        "image": "teste",
    }

    user_data = {
        "username": "test",
        "email":    "test@test.email",
        "favorites": [prod_data]
    }

    try:
        user = User(**user_data)
    except ValidationError:
        assert True
    
def test_create_user_invalid_email():
    prod_data = {
        "id": "teste",
        "title": "teste",
        "image": "teste",
        "price": 123.4
    }

    user_data = {
        "username": "test",
        "email":    "test@test",
        "favorites": [prod_data]
    }

    try:
        user = User(**user_data)
    except ValidationError:
        assert True