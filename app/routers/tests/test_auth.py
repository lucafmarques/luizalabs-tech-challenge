import jwt
from fastapi.testclient import TestClient

from ..auth import router

client = TestClient(router)

def test_gen_token_default_config():
    resp = client.post(
        "/token",
        data={"username": "dev", "password": "dev"}
    )

    body = resp.json()
    token_data = jwt.decode(body["access_token"], key="development-key", algorithms="HS256")
    assert resp.status_code == 201
    assert token_data["sub"] == "dev"
    


def test_gen_token_wrong_credentials():
    resp = client.post(
        "/token",
        data={"username":"wrong", "password": "credentials"}
    )

    assert resp.status_code == 401