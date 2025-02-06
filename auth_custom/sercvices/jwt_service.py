import os
from datetime import datetime, timedelta
from http.client import HTTPException

import jwt
from django.shortcuts import get_object_or_404
from dotenv import load_dotenv

from users.models import User

load_dotenv()

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')


class JWTService:
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def create_access_token(self, data: dict, expires_in) -> str:
        """Создает JWT-токен с данными."""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(seconds=expires_in)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

    def decode_access_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError as e:
            raise HTTPException(e)
        except jwt.InvalidTokenError as e:
            raise HTTPException(e)

    def refresh_access_token(self, token) -> dict:
        payload = self.decode_access_token(token)
        if payload.get('type') != 'refresh':
            raise HTTPException('Invalid token type')

        updated_payload = {
            **payload,
            "type": "access"
        }
        new_access_token = self.create_access_token(updated_payload, expires_in=3600)
        return {"access_token": new_access_token}

    def add_tokens_to_user(self, token, user_name, refresh_token=None):
        user = get_object_or_404(User, user_name)
        user.token = token
        if refresh_token:
            user.refresh_token = refresh_token
        user.save()


def get_jwt_service() -> JWTService:
    return JWTService(JWT_SECRET_KEY, JWT_ALGORITHM)
