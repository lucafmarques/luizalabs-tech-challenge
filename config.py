import os
import json

from pydantic import BaseModel

class AuthUser(BaseModel):
    username: str
    password: str

class Config(BaseModel):
    DB_URL: str = "127.0.0.1:5432"
    DB_USER: str = "admin"
    DB_PASSWORD: str = "7eef259c-e762-416d-ae00-dee029ab6d9b"
    ADMIN: AuthUser
    SECRET_KEY: str
    PRODUCT_URL: str = "http://challenge-api.luizalabs.com/api/product/"

    def URL(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_URL}/luizalabs"


def read_config(path: str):
    with open(path) as raw_config:
        data = json.load(raw_config)

    return Config.parse_obj(data)

config = config = read_config(os.getenv('CONFIG_PATH'))
