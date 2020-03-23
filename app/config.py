import os
import json

from pydantic import BaseModel

class AuthUser(BaseModel):
    username: str
    password: str

class Config(BaseModel):
    DB_URL: str = "localhost:5432"
    DB_USER: str = "admin"
    DB_PASSWORD: str = "7eef259c-e762-416d-ae00-dee029ab6d9b"
    ADMIN: AuthUser = AuthUser(
        username="dev", 
        password="dev"
    )
    SECRET_KEY: str = "development-key"
    PRODUCT_URL: str = "http://challenge-api.luizalabs.com/api/product/"

    def URL(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_URL}/luizalabs"


def read_config(path: str):
    if path:
        with open(path) as raw_config:
            data = json.load(raw_config)

        config = Config.parse_obj(data)
    else:
        config = Config.parse_obj({})

    return config

config = read_config(os.getenv('CONFIG_PATH'))
