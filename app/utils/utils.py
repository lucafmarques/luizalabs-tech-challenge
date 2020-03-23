import requests
from fastapi import status

from schemas.product import Product
from db import SessionLocal, engine, config

def db_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def valid_product(product_id: str):
    url = f"{config.PRODUCT_URL}/{product_id}"

    resp = requests.get(url)
    if resp.status_code != status.HTTP_200_OK:
        return {}, False

    return resp.json(), True
    