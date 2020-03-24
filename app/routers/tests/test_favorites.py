# import pytest
# from fastapi.testclient import TestClient

# from .. import favorites

# @pytest.fixture(scope="module")
# def test_app():
#     client = TestClient(favorites.router)
#     yield client

# def test_add_favorite_missing_user(test_app, monkeypatch):
#     async def mock_fetch_user(email: str):
#         return None

#     monkeypatch.setattr(favorites.add_favorite, "get_user_by_email", mock_fetch_user)

#     resp = client.post(
#         "/fake@user.email/invalid_product_id",
#         headers={"token": "teste"}
#     )

#     assert resp.status_code == 400
