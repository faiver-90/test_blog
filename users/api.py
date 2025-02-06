from ninja import NinjaAPI

from auth_custom.api import auth_router
from users.schemas import UserSchema, PartialUserSchema
from users.user_service import UserService

user_api = NinjaAPI()
user_api.add_router('/auth', auth_router)


@user_api.post("/create_user")
def create_user(request, data: UserSchema):
    return UserService.create_user(data.user_name, data.password)


@user_api.put("/update_user")
def update_user(request, user_name, data: PartialUserSchema):
    return UserService.update_user_by_user_name(user_name, data)


@user_api.post("/get_user_by_user_name")
def get_user_by_user_name(request, user_name):
    return UserService.get_user_by_user_name(user_name)


@user_api.delete("/delete_user")
def delete_user(request, user_id):
    return UserService.delete_user(user_id)
