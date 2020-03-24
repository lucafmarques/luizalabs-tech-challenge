from ..product import Product

def test_create_product():
    prod_data = {
        "id": "teste",
        "title": "teste",
        "image": "teste",
        "price": 123.4
    }

    prod = Product(**prod_data)

    assert prod.id == prod_data["id"]
    assert prod.title == prod_data["title"]
    assert prod.image == prod_data["image"]
    assert prod.price == prod_data["price"]



