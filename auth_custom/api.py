from http.client import HTTPException

from django.shortcuts import get_object_or_404
from ninja import Router

from auth_custom.schemas import TokenSchema, LoginSchema, RefreshTokenSchema
from auth_custom.sercvices.jwt_service import get_jwt_service
from users.models import User

auth_router = Router(tags=['Auth'])

jwt_service = get_jwt_service()


@auth_router.post("/auth/token", response=TokenSchema)
def login(request, data: LoginSchema):
    user = get_object_or_404(User, user_name=data.username, password=data.password)
    if user is None:
        return {"detail": "Неверные учетные данные"}, 401
    data_for_token = {
        "user_id": user.id,
        "user_role": user.role,
        "user_name": user.user_name,
    }
    access_token = jwt_service.create_access_token(
        {**data_for_token, "type": "access"}, expires_in=3600
    )
    refresh_token = jwt_service.create_access_token(
        {**data_for_token, "type": "refresh"}, expires_in=86400
    )
    jwt_service.add_tokens_to_user(access_token, data.username, refresh_token)

    return {"access_token": access_token, "refresh_token": refresh_token}


@auth_router.post("/auth/token/refresh", response=TokenSchema)
def refresh_token(request, data: RefreshTokenSchema):
    try:
        new_access_token = jwt_service.refresh_access_token(data.refresh_token)
        return {
            "access_token": new_access_token["access_token"],
            "refresh_token": data.refresh_token
        }
    except HTTPException as e:
        return {"detail": str(e)}, 401


@auth_router.get("/auth/validate")
def validate_token(request, token: str):
    try:
        payload = jwt_service.decode_access_token(token)
        return {"valid": True, "payload": payload}
    except HTTPException as e:
        return {"valid": False, "detail": str(e)}, 401
