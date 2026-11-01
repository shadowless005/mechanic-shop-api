import os
import secrets


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///mechanic_shop_demo.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
